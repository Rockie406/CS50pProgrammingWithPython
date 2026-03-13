def main():
    song = "Adieu, adieu, to "
    name_count = 0
    while True:
        try:
            name = input("Name: ").strip()
            name_count += 1
            if name_count == 1:
                song = song + name
            elif name_count == 2:
                song = song + " and " + name
            elif name_count == 3:
                song = song.replace(" and", ",")
                song = song + ", and " + name
            elif name_count > 3:
                song = song.replace(" and", "")
                song = song + ", and " + name

        except EOFError:
            print(song)
            break

            
        
        
    
    #难点在于and随时保持n-1位
if __name__ == "__main__":
    main()