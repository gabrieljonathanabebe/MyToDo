from my_utils import ansi


# ===== FONT STYLES ==============================
def colorize(color: str, msg: str) -> str:
    return f"{color}{msg}{ansi.RESET}"


def italic(plain: str) -> str:
    return f"{ansi.ITALIC}{plain}{ansi.RESET}"


def bold(plain: str) -> str:
    return f"{ansi.BOLD}{plain}{ansi.RESET}"


def dim(plain: str) -> str:
    return f"{ansi.DIM}{plain}{ansi.RESET}"


def red(msg: str) -> str:
    return colorize(ansi.RED, msg)


def yellow(msg: str) -> str:
    return colorize(ansi.YELLOW, msg)


def green(msg: str) -> str:
    return colorize(ansi.GREEN, msg)


def blue(msg: str) -> str:
    return colorize(ansi.BLUE, msg)


def bg_blue(msg: str) -> str:
    return colorize(ansi.BG_BLUE, msg)


# ===== INFOS ====================================
def error(msg: str) -> str:
    return red(msg)


def warning(msg: str) -> str:
    return yellow(msg)


def success(msg: str) -> str:
    return green(msg)


def info(msg: str) -> str:
    return blue(msg)


def hint(msg: str) -> str:
    return bg_blue(msg)
