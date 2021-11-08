def devmode():
    if int(open("cfg","r").read().split("\n")[0]) == 0:
        return False
    elif int(open("cfg","r").read().split("\n")[0]) == 1:
        return True
def rolecolors():
    if int(open("cfg","r").read().split("\n")[1]) == 0:
        return False
    elif int(open("cfg","r").read().split("\n")[1]) == 1:
        return True
def prefix():
    if open("cfg","r").read().split("\n")[3] != "":
        return open("cfg","r").read().split("\n")[3]
    elif open("cfg","r").read().split("\n")[3] == "":
        open("cfg","a").write(input("please enter a prefix :: "))
        return open("cfg","r").read().split("\n")[3]
def loadconfig():
    class cfg :
        class settings:
            devmode = devmode()
            rolecolors = rolecolors()
        TOKEN = open("cfg","r").read().split("\n")[2]
        PREFIX = prefix()
    return cfg