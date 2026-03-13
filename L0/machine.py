emotion = "v.v"
def main():
    global emotion
    say("is anyone here? ")
    emotion = ":D"
    say("oh, hi!")

def say(sth):
    print(sth + emotion)

main()