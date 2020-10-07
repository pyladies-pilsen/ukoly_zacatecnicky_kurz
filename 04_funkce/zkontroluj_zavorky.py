
def zkontroluj_zavorky(retezec):
    """
    Zkontroluje jestli jsou závorky
    správně spárované.

    :param retezec: string se závorkami
    :return: True pokud jsou, False jinak
    """
    otevreno = 0
    for c in retezec:
        if c == "(":
            otevreno = otevreno + 1  # stejne jako otevreno += 1
        elif c == ")":
            otevreno -= 1

        if otevreno < 0:
            return False

    if otevreno != 0:
        return False

    return True

retezec = str(input("Zadejte retezec, jehoz zavorky, chete zkontrolovat \n: "))
print(zkontroluj_zavorky(retezec))
