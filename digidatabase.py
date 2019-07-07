from pathlib import Path

from globalsb4 import folder

def getUserArray():
    pass

def setUserProperty():
    pass

def getUserFilePath(userId):
    return Path(folder) / "users" / (str(userId) + ".txt")

def userFileExists(userId):
    path = getUserFilePath(userId)
    return path.exists()

def saveUserFile(user, data):
    userFileString = "\n".join([data["nick"], 
                                data["display"],
                                str(data["currentheight"]) + data["chu"],
                                str(data["baseheight"]) + data["bhu"],
                                str(data["baseweight"]) + data["bwu"],
                                "1.0",
                                data["species"]]) + "\n"
    path = getUserFilePath(user.id)
    with open(path, "w") as f:
        f.write(userFileString)
    print(warn("Made a new user: {}!").format(user))
    print(data)

def loadUserFile():
    pass

def deleteUserFile(userId):
    path = getUserFilePath(userId)
    path.unlink()