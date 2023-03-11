import re
import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip: str) -> bool:
    try:
        for ip_byte in ip.split("."):
            if int(ip_byte) > 255 or int(ip_byte) < 0:
                return False
    except ValueError:
        return False
    if re.search(r"^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$",
                 ip, flags=re.IGNORECASE):
        return True
    return False


if __name__ == "__main__":
    main()
