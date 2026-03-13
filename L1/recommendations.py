def recommend(game):
    print("you might like " + game)


def main():
    ### if not不仅有更好的可读性，还提高了程序的分辨效果。
    # 如此前difficulty和playernumber都出错时，只会提示其中一个，现在生成的提示可以一一对应输入的错误
    difficulty = input("Casual or Difficult? ")
    if not (difficulty == "Casual" or difficulty == "Difficult"):
        print("Enter a valid level of difficulty")
        return
    player_number = input("Single_player or Multiple_player? ")
    if not (player_number == "Single_player" or player_number == "Multiple_player"):
        print("Enter a valid number of players")

    if difficulty == "Casual" and player_number == "Single_player":
        recommend("1+1")
    if difficulty == "Casual" and player_number == "Multiple_player":
        recommend("1+2")
    if difficulty == "Difficult" and player_number == "Single_player":
        recommend("2+1")
    if difficulty == "Difficult" and player_number == "Multiple_player":
        recommend("2+2")
            
    
main()


