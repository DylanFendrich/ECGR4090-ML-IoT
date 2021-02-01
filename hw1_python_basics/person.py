class person:
    #part C
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    
    #part D
    def __repr__(self):
        return "{:} is {:} years old and {:} cm tall.".format(self.name, self.age, self.height)

        
        
#part C continued
new_person = person(name='Joe', age=34, height=184)
print("{:} is {:} years old.".format(new_person.name, new_person.age))

#part D continued
print(new_person)
        