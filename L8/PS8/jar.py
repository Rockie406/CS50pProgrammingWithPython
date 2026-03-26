
class Jar:
    def __init__(self, capacity):
        if int(capacity) < 0:
            raise ValueError(">0 only")
        else:
            self.capacity = int(capacity)
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
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity
    
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        self._size = size

#可以不要？    
def main():
    #如果把.seposit放到Jar(())后面，因为前者没有return，故jar会编程NONE。
    #__init__也没有return，为什么jar = Jar(input("Capacity: "))不导致jar编程NONE
    #因为__init__隐含一个__new__，可实现return
    jar = Jar(input("Capacity: "))
    jar.deposit(3)
    print(jar)
    




if __name__ == "__main__":
    main()