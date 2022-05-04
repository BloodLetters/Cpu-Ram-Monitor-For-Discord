import json


def getTitle(type):
    if type == 1:
        file = open("Config.json", 'r')
        data = json.load(file)
        return data['Title']['Name']
    elif type == 2:
        file = open("Config.json", 'r')
        data = json.load(file)
        return data['Title']['Url']
    else:
        print("Error!. type must 1 or 2")


def getAuthor(type):
    if type == 1:
        file = open("Config.json", 'r')
        data = json.load(file)
        return data['Author']['Name']
    elif type == 2:
        file = open("Config.json", 'r')
        data = json.load(file)
        return data['Author']['Link']
    else:
        print("Error!. Author Type only can set to 1, 2 or 3")


def getFields(hard, type):
    if hard == "cpu":
        if type == 1:
            file = open("Config.json", 'r')
            data = json.load(file)
            return data['Fields']['1']['name']
        if type == 2:
            file = open("Config.json", 'r')
            data = json.load(file)
            return data['Fields']['1']['value']
    if hard == "ram":
        if type == 1:
            file = open("Config.json", 'r')
            data = json.load(file)
            return data['Fields']['2']['name']
        elif type == 2:
            file = open("Config.json", 'r')
            data = json.load(file)
            return data['Fields']['2']['value']


def getThumbnail():
    file = open("Config.json", 'r')
    data = json.load(file)
    return data['Thumbnail']


def getDescription():
    file = open("Config.json", 'r')
    data = json.load(file)
    return data['Description']


def getFooter():
    file = open("Config.json", 'r')
    data = json.load(file)
    return data['Footer']


def getMessageID():
    file = open("Config.json", 'r')
    data = json.load(file)
    return data['MessageID']


def getChannelID():
    file = open("Config.json", 'r')
    data = json.load(file)
    return data['ChannelID']


def getToken():
    file = open("Config.json", 'r')
    data = json.load(file)
    return data['Token']