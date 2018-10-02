import datetime

class Person(object):
    def __init__(self, name):
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]
    def __str__(self):
        return self.name
    def __lt__(self, other):
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    def setBirthday(self, month, day, year):
        self.birthday = datetime.date(year, month, day)
    def getAge(self):
        return (datetime.date.today() - self.birthday).days
    def getLastName(self):
        return self.lastName
    def isStudent(obj):
        return isinstance(obj, Student)

class MITPerson(Person):
    nextIdNum = 0

    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1
    def getIdNum(self):
        return self.idNum
    def __lt__(self, other):
        return self.idNum < other.idNum
    def speak(self, utterance):
        return self.getLastName() + " says: " + utterance

class Professor(MITPerson):
    def __init__(self, name, department):
        MITPerson.__init__(self, name)
        self.department = department
    def speak(self, utterance):
        newUtterance = 'In course ' + self.department + ' we say '
        return MITPerson.speak(self, newUtterance, utterance)
    def lecture(self, topic):
        return self.speak("it is obvious that " + topic)


class Student(MITPerson):
    pass

class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
    def getClass(self):
        return self.year
    def speak(self, utterance):
        return MITPerson.speak(self, "Dude, " + utterance)

class Grad(Student):
    pass

class TransferStudent(Student):
    pass
