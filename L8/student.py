class Student:
    #定义class的各attribute
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name")
        
        #if patronus and patronus not in ["Stag", "Otter", "Jack Russell terrier"]:
            #raise ValueError("Invalid patronus")
        self.name = name
        #self.patronus = patronus
    
    #定义object被调用__str__（如print时）的行为
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    '''def charm(self):
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🦦"
            case "Jack Russell terrier":
                return "🐶"
            case _:
                return "🪄"'''
    
    # Getter for house
    @property
    #和上面的charm一样，定义了method/properties被call时的行为
    def house(self):
        return self._house
    
    # Getter for house
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house
    


def main():
    #简单的input print
    #def构建函数包含这俩函数
    #用tuple包含name和house
    #tuples are immutable, meaning we cannot change those values. 
    #Immutability is a way by which we can program defensively. 
    #You might decide to utilize this in some
    #cases where you want to provide more flexibility at the cost of the security of your code
    student = get_student()
    #print("EXPECTO PATRONUM")
    print(student)

def get_student():
    #Any time you create a class and you utilize that blueprint to create something, 
    #you create what is called an “object” or an “instance”. In the case of our code, student is an object.
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)



if __name__ == "__main__":
    main()