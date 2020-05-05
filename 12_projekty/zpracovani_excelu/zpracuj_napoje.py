import pandas as pd
napoje_df = pd.read_excel("lb_data.xlsx")

# vytahneme kódy a odpovídající typy
kod_typ = napoje_df.iloc[0:4, 11:13]

# orizneme jen zajimave sloupce a radky
napoje_cut_df = napoje_df.iloc[0:9, 2:8].reset_index(drop=True)

# projdeme radky tabulky
for index, polozka in napoje_cut_df.iterrows():
    filtr = kod_typ["Kód.1"] == polozka["Kód"]
    napoje_cut_df.at[index, "Reference"] = \
          polozka["Kód"] + \
          polozka["Číslo"][3:] + \
          kod_typ[filtr]["TYP"].values[0]

napoje_cut_df.to_excel("vysledek.xls")
