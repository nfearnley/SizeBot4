from pathlib import Path

from globalsb4 import folder

from DPNGourmet import warn


def getUserArray():
    pass


def setUserProperty():
    pass


def getUserFilePath(userId):
    filename = f"{userId}.txt"
    return Path(folder) / "users" / filename


def userFileExists(userId):
    path = getUserFilePath(userId)
    return path.exists()


def saveUserFile(user, data):
    userFileString = (
        f"{data['nick']}\n"
        f"{data['display']}\n"
        f"{data['currentheight']}{data['chu']}\n"
        f"{data['baseheight']}{data['bhu']}\n"
        f"{data['baseweight']}{data['bwu']}\n"
        "1.0\n"
        f"{data['species']}\n")
    path = getUserFilePath(user.id)
    with open(path, "w") as f:
        f.write(userFileString)
    print(warn(f"Made a new user: {user}!"))
    print(data)


def loadUserFile():
    pass


def deleteUserFile(userId):
    path = getUserFilePath(userId)
    path.unlink()
