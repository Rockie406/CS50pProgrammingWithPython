def main():
    amount_due = 50
    while True:
        if amount_due > 0:
            print(f"Amount Due: {amount_due}")
        else:
            print(f"Change Owed: {-amount_due}")
            break

        insert_coin = input("Insert Coin: ")
        if insert_coin == "5" or insert_coin == "10" or insert_coin == "25":
            amount_due -= int(insert_coin)
            

main()