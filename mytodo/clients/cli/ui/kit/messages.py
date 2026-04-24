from . import style


def error(msg: str) -> None:
    print(style.error(msg))


def warning(msg: str) -> None:
    print(style.warning(msg))


def success(msg: str) -> None:
    print(style.green(msg))


def info(msg: str) -> None:
    print(style.info(msg))


def hint(msg: str) -> None:
    print(style.hint(msg))
