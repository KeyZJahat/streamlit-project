import sys
import time

# Warna ANSI untuk mencantikkan paparan terminal
PINK = "\033[95m"
BLUE = "\033[94m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"


def print_slow(text, delay=0.04):
    """Mencetak teks satu per satu dengan kesan menaip."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def show_cake():
    cake = f"""
{YELLOW}         i  i  i  i  i{RESET}
{YELLOW}         |  |  |  |  |{RESET}
{PINK}       ___||__||__||___{RESET}
{PINK}      |                |{RESET}
{CYAN}    __|________________|__{RESET}
{CYAN}   |                      |{RESET}
{GREEN}  |________________________|{RESET}
{GREEN} |                          |{RESET}
{BLUE}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}
"""
    print(cake)


def celebrate():
    # Seni ASCII Selamat Hari Lahir
    banner = f"""{BOLD}{CYAN}
  _   _                           ____  _rt_hk_day!  
 | | | | __ _ _ __  _ __  _   _  | __ )(_)_ __| |_| |__   __| | __ _ _   _ 
 | |_| |/ _` | '_ \| '_ \| | | | |  _ \| | '__| __| '_ \ / _` |/ _` | | | |
 |  _  | (_| | |_) | |_) | |_| | | |_) | | |  | |_| | | | (_| | (_| | |_| |
 |_| |_|\__,_| .__/| .__/ \__, | |____/|_|_|   \__|_| |_|\__,_|\__,_|\__, |
             |_|   |_|    |___/                                      |___/ 
{RESET}"""

    print_slow(banner, delay=0.002)
    time.sleep(0.5)

    show_cake()
    time.sleep(0.5)

    messages = [
        f"{YELLOW}🎉 Selamat Hari Lahir! 🎂{RESET}",
        f"{GREEN}Semoga panjang umur, dimurahkan rezeki, dan sentiasa bahagia! ✨{RESET}",
        f"{PINK}Semoga segala impian dan cita-citamu menjadi kenyataan tahun ini. 🚀{RESET}",
    ]

    for msg in messages:
        print_slow(msg, delay=0.05)
        time.sleep(0.3)

    print("\n" + f"{RED}🎈 " * 12 + f"{RESET}\n")


if __name__ == "__main__":
    celebrate()
