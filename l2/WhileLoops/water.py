from soil import sample
def main():
    moisture = sample()
    print(f"the moisture is {moisture}%")
    days = 0

    while moisture > 20:
        days += 1
        moisture = sample()
        print(f"Day{days}: the moisture is {moisture}%")

    print("Time to water! ")

main()