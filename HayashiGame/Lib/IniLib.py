import os
import configparser

# iniファイルからパラメータを取得する(パラメータをint型で欲しい場合は第4引数にTrueを設定する)
def iniSettingGet(iniPath, section, key, intFlag = False):
    # 指定したiniファイルが存在しない場合、エラー発生
    if not os.path.exists(iniPath):
        print("File not found.\n", iniPath)
        return None

    # iniの読み込みオープン
    config_ini = configparser.ConfigParser()
    config_ini.read(iniPath, encoding='utf-8')

    # iniの値取得
    read_obstacle = config_ini[section]
    getPara = read_obstacle.get(key)

    # パラメータを取得できなかったとき
    if getPara == None:
        print("Parameter error.\n", iniPath, section, key)
        return None

    # int型に変換する必要があるとき
    if intFlag:
        return iniStringToInt(getPara)
    else:
        return getPara

# iniファイルから取得したパラメータの型変換を実施する(string->int)
def iniStringToInt(inStr):
    try:
        return int(inStr)
    except:
        print("Parameter type conversion error.\n", inStr)
        return None

