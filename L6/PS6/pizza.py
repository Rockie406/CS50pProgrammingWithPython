import sys
import csv
from tabulate import tabulate
def main():
    cla_check(4, ".csv", 1)
    with open(sys.argv[1]) as file:
        rows = []
        for row in csv.DictReader(file):
            rows.append(row)
    print(tabulate(rows, headers = "keys", tablefmt = "grid"))

def cla_check(suffix_count, suffix_value, argument_count):
    if len(sys.argv) != (argument_count + 1):
        sys.exit(f"{argument_count} argument only")
    elif sys.argv[1][-suffix_count:] != suffix_value:
        sys.exit(".csv only")
    try:
        with open(sys.argv[1]) as file:
            pass
    except FileNotFoundError:
        sys.exit("file does not exit")
    except IndexError:
        sys.exit("")
#检验首先针对argv对应的list，无误则进一步检查list的内容
if __name__ == "__main__":
    main()

#wget https://cs50.harvard.edu/python/2022/psets/6/pizza/sicilian.csv
#wget https://cs50.harvard.edu/python/2022/psets/6/pizza/regular.csv