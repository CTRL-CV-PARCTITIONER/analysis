from colorama import Fore, Style

reset_color = Style.RESET_ALL

Fore_colors = [
    Fore.BLACK,
    Fore.RED,
    Fore.GREEN,
    Fore.YELLOW,
    Fore.BLUE,
    Fore.MAGENTA,
    Fore.CYAN,
    Fore.WHITE,
    Fore.LIGHTBLACK_EX,
    Fore.LIGHTRED_EX,
    Fore.LIGHTGREEN_EX,
    Fore.LIGHTYELLOW_EX,
    Fore.LIGHTBLUE_EX,
    Fore.LIGHTMAGENTA_EX,
    Fore.LIGHTCYAN_EX,
    Fore.LIGHTWHITE_EX,
]

_type = [
    "txt",
    "csv",
    "xlsx",
    "xls",
    "json",
    "html",
]

_sqlParam = {
    "username": "",
    "password": "",
    "host": "127.0.0.1",
    "port": "3306",
    "database": "",
    "mode": "append",
    "table": "",
    "save": ""
}