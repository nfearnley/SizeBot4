from time import strftime, localtime

from colored import fg, back, fore, style


def load(message):
    return (fg(238) + message + style.RESET)


def time():
    return (fore.MAGENTA + strftime("%d %b %H:%M:%S | ", localtime()) + style.RESET)


def warn(message):
    return (time() + fore.YELLOW + message + style.RESET)


def crit(message):
    return (time() + back.RED + style.BOLD + message + style.RESET)


def test(message):
    return (time() + fore.BLUE + message + style.RESET)


def msg(message):
    return (time() + fg(51) + message + style.RESET)


banner = (
    ' .d8888b.  d8b                   888888b.            888       d8888\n'
    'd88P  Y88b Y8P                   888  "88b           888      d8P888\n'
    'Y88b.                            888  .88P           888     d8P 888\n'
    ' "Y888b.   888 88888888  .d88b.  8888888K.   .d88b.  888888 d8P  888\n'
    '    "Y88b. 888    d88P  d8P  Y8b 888  "Y88b d88""88b 888   d88   888\n'
    '      "888 888   d88P   88888888 888    888 888  888 888   8888888888\n'
    'Y88b  d88P 888  d88P    Y8b.     888   d88P Y88..88P Y88b.       888\n'
    ' "Y8888P"  888 88888888  "Y8888  8888888P"   "Y88P"   "Y888      888')
