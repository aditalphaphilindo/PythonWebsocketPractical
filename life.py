class LifeTime:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Halo, test from " + abc.name)


p1 = LifeTime("Adit", 22)

