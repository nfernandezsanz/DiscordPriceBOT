import io
import os
from   configparser import ConfigParser

def read_bots():
    lista = list()
    config = ConfigParser() 
    config.read('config.ini') 
    bots = config.sections();
    print ("I have " + str(len(bots)) + " bots")

    for x in bots:
        bot   = dict()
        info = config.options(x)
        if('coin' in info and 'token' in info):
            try:
                coin      = str(config.get(x,'coin')).replace('"', "")
                token     = str(config.get(x,'token')).replace('"', "")
                bot[coin] = token
                lista.append(bot)
            except:
                print(str(x) + " has invalid information!")
        else:
            print(str(x) + " has invalid information!")
    return lista

