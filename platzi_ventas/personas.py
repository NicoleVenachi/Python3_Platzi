class Person:
    def __init__(self, name, age):
        sel.name = name
        self.age = age
    def say_hello(self):
        print('Hello, my name iis {}, and i\'m {} years old'.format(self.name, self.age))

if __name__ == '__main__':
    person = Person('Nicole', 21)
    print('Age: {}'.format(person.age))
    person.say_hello()
