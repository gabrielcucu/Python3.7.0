from Lesson_1_Math import lesson_1_Math

# mate = lesson_1_Math()
# mate.Adunare(2,3)
# mate.OraExacta()
# mate.Calendarul()

from Lesson_2_Objects import Person
x:int = 0
isInteger :bool = True

while isInteger :
    countGabi = input()
    try:
        int(countGabi)
        isInteger = False
    except ValueError:
        print("Could not convert data to an integer.")
        
while x < int(countGabi):
    x = x + 1
    person = Person("Gabi",x)
    person.AboutPerson()
