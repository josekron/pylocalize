class LocalizeVo:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def printLocalizeVo(self):
        print (self.name," : ",self.value)
