"""
This script watches specified file and uploads changes to gist
"""

__author_ = "Tomáš Zítka, tozitka@gmail.com"
import os
import sys
from os.path import join as pjoin
import time
from datetime import datetime, timedelta
import argparse
import pathlib

from simplegist.simplegist import Simplegist
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


class MyGist:
    def __init__(self, name, description, content,
                 username="",
                 api_token=""):
        self.name = name
        self.description = description
        self.content = content
        self.gist_connection = Simplegist(
                    username=username,
                    api_token=api_token)
        gist_info = self.gist_connection.create(name=self.name,
                    description=self.description,
                    public=True,
                    content=self.content)
        self.gist_link = gist_info["Gist-Link"]
        self.url = self.gist_link
        self.clone_link = gist_info["Clone-Link"]
        self.embed_script = gist_info["Embed-Script"]
        self.id = gist_info["id"]
        self.created_at = gist_info['created_at']

    def update(self, name=None, description=None, content=None):
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if content is not None:
            self.content = content
        self.gist_connection.profile().edit(
            id=self.id,
            description=self.description,
            name=self.name,
            content=self.content)


class GistUpdater(PatternMatchingEventHandler):
    def __init__(self, gist, **kwargs):
        super(GistUpdater, self).__init__(**kwargs)
        self.gist = gist
        self.last_modified = datetime.now()

    def on_any_event(self, event):
        if datetime.now() - self.last_modified < timedelta(seconds=10):
            return
        with open(event.src_path, mode="r", encoding="utf-8") as f:
            content = f.read()
        self.gist.update(content=content)
        # print(content)
        self.last_modified = datetime.now()


parser = argparse.ArgumentParser(
    description='Run watcher on file that uploads contents to Gist',
    epilog='(c) 2020 by T. Zitka , tozitka@gmail.com')

parser.add_argument("file", help="Path to watched file")
parser.add_argument("-n", "--name", help="Name of the Gist, if not provided, name of file is used")
parser.add_argument("-d", "--description", help="Description of the Gist, if not provided deafult is generated")


def main(argv):
    if argv is None:
        argv = sys.argv[1:]

    args = parser.parse_args(argv)

    path = pathlib.Path(args.file)

    if args.name is None:
        name = "Code from " + path.name
    else:
        name = args.name

    if args.description is None:
        desc = "Code streamed from " + path.name + " started on " + str(datetime.now())

    if path.exists() and path.is_file():
        with open(path, mode="r", encoding="utf-8") as f:
            contents = f.read()

    gist = "gg"
    gist = MyGist(name=name, description=desc, content=contents)
    print("Created Gist at url " + gist.url)
    print("Name:", name)
    print("Description:", desc)
    print("Contents:\n" + 10*"--", "\n" + contents, "\n" + 10*"--")

    event_handler = GistUpdater(gist, patterns=[str(path)])
    observer = Observer()
    observer.schedule(event_handler, str(path.parent))
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == '__main__':
    main(sys.argv[1:])

