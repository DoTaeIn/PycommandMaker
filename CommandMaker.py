prefix = "/"

def commandwithoneparameter(command):
    while True:
        commandInput = input("Input: ")
        if commandInput.startswith(prefix):
            stringcommandline = str(commandInput).replace("/", "")
            if stringcommandline in dict(command):
                pass
            else:
                print("no such command!")
                #def or function here

def commandwithmultipleparameter(commandcount, middlecommandlist):
    if commandcount >= 3:
        while True:
            commandInputmulti = input("Input: ")
            if commandInputmulti.startswith(prefix):
                commandInputmultistr = str(commandInputmulti)
                commandInputmultistr.replace("/", "")
                commandInputmultistrsplited = commandInputmultistr.split(" ", int(commandcount))
                lastparameter = commandInputmultistrsplited[2]

                if commandInputmultistrsplited[1] in dict(middlecommandlist):
                    dict(middlecommandlist).get(commandInputmultistrsplited[1])

                else:
                    print("Cannot run command --> " + commandInputmultistrsplited[1] + " no such command")
