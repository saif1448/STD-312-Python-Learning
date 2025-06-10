
#class variable ---> which is common to every instance
# class method ---> which is common to every instance
# class method and class variable should be accessed via the Class name


class Person:
     species = "Human"  # not within the constructor # class variable

     @classmethod
     def info(cls):
        return cls.species

     @classmethod
     def show_class_string(cls):
         print("This method is a class method")

     def show_normal_string(self):
        print("It is a instance method")



p1 = Person()
p2 = Person()

Person.species = "Non human"

print(Person.info())
Person.show_class_string()

p1.show_normal_string()

