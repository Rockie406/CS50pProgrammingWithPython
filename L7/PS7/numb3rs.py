import re
import sys


def main():
    print(validate(input("IPV4 Address: ").strip()))


def validate(ip):
    # split更简单吧，所以题干说“you r welcome, but not required, to use re and/or sys”
    # 三位数没问题，问题在怎么实现255
    # "09"这种也是不允许的
    # 写完复杂版，在尝试对{1}能否删除 可以删除
    if re.search(
        r"^([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$",
        ip,
    ):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
