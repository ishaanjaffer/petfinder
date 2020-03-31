'''
Dog class
'''
class Dog:

    def __init__(self, name, birthdate, breed, color):
        self.name = name
        self.birthdate = birthdate
        self.breed = breed
        self.color = color

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getBirthdate(self):
        return self.birthdate

    def setBirthdate(self, birthdate):
        self.birthdate = birthdate

    def getBreed(self):
        return self.breed

    def setBreed(self, breed):
        self.breed = breed

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def __str__(self):
        return "Dog, " + self.name + ", " + self.birthdate + ", " + self.breed + ", " + self.color + ","

'''
Cat class
'''
class Cat:

    def __init__(self, name, birthdate, breed, color):
        self.name = name
        self.birthdate = birthdate
        self.breed = breed
        self.color = color

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getBirthdate(self):
        return self.birthdate

    def setBirthdate(self, birthdate):
        self.birthdate = birthdate

    def getBreed(self):
        return self.breed

    def setBreed(self, breed):
        self.breed = breed

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def __str__(self):
        return "Cat, " + self.name + ", " + self.birthdate + ", " + self.breed + ", " + self.color + ","

'''
Fish class
'''     
class Fish:

    def __init__(self, name, birthdate, type, color):
        self.name = name
        self.birthdate = birthdate
        self.type = type
        self.color = color

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getBirthdate(self):
        return self.birthdate

    def setBirthdate(self, birthdate):
        self.birthdate = birthdate

    def getType(self):
        return self.type

    def setType(self, type):
        self.type = type

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def __str__(self):
        return "Fish, " + self.name + ", " + self.birthdate + ", " + self.type + ", " + self.color + ","

'''
Bird class
''' 
class Bird:

    def __init__(self, name, birthdate, type, color):
        self.name = name
        self.birthdate = birthdate
        self.type = type
        self.color = color

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getBirthdate(self):
        return self.birthdate

    def setBirthdate(self, birthdate):
        self.birthdate = birthdate

    def getType(self):
        return self.type

    def setType(self, type):
        self.type = type

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def __str__(self):
        return "Bird, " + self.name + ", " + self.birthdate + ", " + self.type + ", " + self.color + ","
