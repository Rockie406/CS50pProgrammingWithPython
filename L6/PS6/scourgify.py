from pizza import cla_check
import sys
import csv
def main():
    cla_check(4, ".csv", 2)
    with open(sys.argv[1]) as file:
        rows = []
        for row in csv.DictReader(file):
            last, first = row["name"].split(", ")
            house = row["house"]
            new_row = {"house": house, "last": last, "first": first}
            rows.append(new_row)
    with open(sys.argv[2], "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for new_row in rows:
            writer.writerow(new_row)




if __name__ == "__main__":
    main()
