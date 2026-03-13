def main():
    The = input("What is the answer to the Great Question of Life, the Universe and Everything").lower().strip()
    #case-insensitively method needed
    if (The == "42" or The == "forty-two" or The == "forty two"):
        print("yes")
    else:
        print("no")

main()

#submit50 cs50/problems/2022/python/deep