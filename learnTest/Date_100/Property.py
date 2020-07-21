class Person(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return "名字是:%s,年龄是:%d" % (self.__name,self.__age)

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def setage(self, age):
        self.__age = age

    def play(self):
        if self.__age <= 16:
            print('%s正在玩飞行棋.' % self.__name)
        else:
            print('%s正在玩斗地主.' % self.__name)


def main():
    person=Person("吉姆",20)
    print(person)
    person.play()
    print(person.age)
    person.setage=12
    print(person.age)
    person.hah="222"
    print(person.hah)
    #person.name="1" #AttributeError: can't set attribute


if __name__ == '__main__':
    main()