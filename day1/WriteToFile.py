from jproperties import Properties


from configparser import ConfigParser





# def setVal(key,value):
#     p = Properties()
#     p[key] = value
#
#     with open("config.properties", "wb") as f:
#         p.store(f, encoding="utf-8")
#

def getVal(key):
    configs = Properties()
    with open('config.properties', 'rb') as read_prop:
        configs.load(read_prop)
    val = configs.get(key)
    return val


def getValue(header,key):
    config =  ConfigParser()
    config.read('config.ini')
    val = config[header][key]
    return val

def setVal(header,key,value):
    config = ConfigParser()
    config.add_section(header)
    config.set(header, key,value)
    with open("config.ini",'w') as configFile:
        config.write(configFile)




setVal("Token","Token","arvind")

print(getValue("Token","token"))