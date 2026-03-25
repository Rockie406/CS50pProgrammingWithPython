
class Jar:
    def __init__(self, capacity):
        if int(capacity) < 0:
            raise ValueError("<0 only")
        else:
            self.capacity = capacity
        self.size = 0
    
    def __str__(self):
        #For instance, if there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"
        return self.size * "🍪"
    
    def deposit(self, n):
        if n > self.capacity:
            raise ValueError("Would exceed the capacity")
        else:
            self.size += n
    
    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Aren't that many cookies")
        else:
            self.size -= n

    #只有取值时会发生getter
    @property
    def capacity(self):
        return self.capacity
    
    @property
    def size(self):
        return self.size
    
def main():
    ...
    




if __name__ == "__main__":
    main()