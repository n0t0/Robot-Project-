from brain import hello
import brain as br
# from db import physical

# TODO: Pass hello() input results from brain.py to class Physical

# br.hello()
# br.emotion_detect()

# Physical Characteristics


class Physical(object):
    """Represents a human?/user phisycal appearance."""

    skin_color = ['black', 'yellow', 'white', 'red', 'green']
    hair_color = ['black']
    weight = []
    height = []
    eyes_color = ['red']
    skills = ['running', 'swimming', 'jumping', '   driving']
    addictions = ['nicotine', 'alcohol', 'shopping']

    def __init__(self, owner, username, sex, age):
        self.owner = owner
        self.username = username
        self.sex = sex
        self.age = age

    def __str__(self):
        print ('User: ')
        # print (br.ask_for_name())
        print (br.hello())
        return 'Skin: %s\nSkills: %s\nSex: %s\nAge: %s\n' % (Physical.skin_color[self.owner],
                                                             Physical.skills[self.username],
                                                             self.sex, self.age)


human = Physical(2, 2, 'male', 20)
print (human)

human.outsideClass = 'string'
print (human.outsideClass)

human.weight = 180
print (human.weight)


#
# def physicalChars(self, color, height, weight, hair, eyes):
#     print 'COLOR:\t %s\n HEIGHT:\t %s\n EYES:\t %s\n' % (self.color, self.height, self.eyes)

# def greeting(self):
#     print 'Hi {}'.format(self.username)
#     print 'How are you?'


# username.physicalChars()
# username.color = 'black'
# username.eyes = 'red'
#
#
#
# owner = 'Bongo'
# username = 'Maya' # take input from hello()
# physicalChars = 'black'
#
# maya = Physical(username, owner, physicalChars)
#
# print maya.physicalChars
# # print maya.greeting()
# print maya.skills
