from my_utils import ansi

# ===== FONT STYLES ==============================
def colorize(color: str, msg: str) -> None:
    print(f'{color}{msg}{ansi.RESET}')

def italic(plain: str) -> str:
    return f'{ansi.ITALIC}{plain}{ansi.RESET}'

def bold(plain: str) -> str:
    return f'{ansi.BOLD}{plain}{ansi.RESET}'

def dim(plain: str) -> str:
    return f'{ansi.DIM}{plain}{ansi.RESET}'

def colorize_red(msg: str) -> None:
    colorize(ansi.RED, msg)

def colorize_yellow(msg: str) -> None:
    colorize(ansi.YELLOW, msg)

def colorize_green(msg: str) -> None:
    colorize(ansi.GREEN, msg)

def colorize_blue(msg: str) -> None:
    colorize(ansi.BLUE, msg)

def colorize_bg_blue(msg: str) -> None:
    colorize(ansi.BG_BLUE, msg)


# ===== INFOS ====================================
def error(msg: str) -> None:
    colorize_red(msg)

def warning(msg: str) -> None:
    colorize_yellow(msg)

def success(msg: str) -> None:
    colorize_green(msg)

def info(msg: str) -> None:
    colorize_blue(msg)

def hint(msg: str) -> None:
    colorize_bg_blue(msg)