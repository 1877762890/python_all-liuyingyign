from day13.task.Person import Person
from day13.task.demo5 import AgeException

p=Person()
p.setAge(20)

p1=Person()
p1.setAge(0)


try:
    p.compare(p1)
except AgeException as e:
    print(e)





