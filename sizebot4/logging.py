from time import strftime, localtime

from colored import fg, bg, back, fore, style


def time_string():
    now_string = strftime("%d %b %H:%M:%S | ", localtime())
    return f"{fore.MAGENTA}{now_string}{style.RESET}"


def banner(banner):
    print(f"{bg(24)}{fg(202)}{style.BOLD}{banner}{style.RESET}")


def log(message, timestamp=True):
    if (timestamp):
        message = f"{time_string()}{message}"
    print(message)


def info(message):
    log(f"{fore.CYAN}{message}{style.RESET}", timestamp=False)


def warn(message):
    log(f"{fore.YELLOW}{message}{style.RESET}")


def crit(message):
    log(f"{back.RED}{style.BOLD}{message}{style.RESET}")


def test(message):
    log(f"{fore.BLUE}{message}{style.RESET}")
