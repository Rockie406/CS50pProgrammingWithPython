def main():
    suffix = input("What is the name of this file: ").lower().strip()
    if suffix.endswith(".gif"):
        print("image/gif")
    elif suffix.endswith(".jpg") or suffix.endswith(".jpeg"):
        print("image/jpeg")
    elif suffix.endswith(".png"):
        print("image/png")
    elif suffix.endswith(".pdf"):
        print("application/pdf")
    elif suffix.endswith(".txt"):
        print("text/plain")
    elif suffix.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")
main()

#check50 cs50/problems/2022/python/extensions
#submit50 cs50/problems/2022/python/extensions