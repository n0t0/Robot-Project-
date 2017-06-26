from brain import hello

class Physical():

    skills = ['running', 'swimming', 'jumping']
    addictions = ['nicotine', 'shopping']


    def __init__(self, name, owner, physicalChars):
        self.owner = owner
        self.name = name

    def greeting(self):
        print 'Hi {}'.format(self.name)
        print 'How are you?'


    def physicalChars(self, color, height, weight, hair, eyes):
        print 'COLOR:\t %s\n HEIGHT:\t %s\n EYES:\t %s\n' % (self.color, self.height, self.eyes)


owner = 'Bongo'
name = 'Maya'
physicalChars = 'black'

maya = Physical(name, owner, physicalChars)

print maya.physicalChars
print maya.greeting()
print maya.skills
