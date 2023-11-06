# main.py
from my_package.person import Person
from my_package.student import Student
from my_package.teacher import Teacher

if __name__ == "__main__":
    instance_a = Person("Krishna", 22)
    instance_b = Teacher("Austin", 40, "Python")
    instance_c = Student("Nani", 22, 1234)

greeting = instance_a.greet()
teaching = instance_b.teach()
study = instance_c.study()

print(greeting)
print(instance_a.name)
print(teaching)
print(study)