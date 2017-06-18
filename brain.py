# This robot is the friend that we all need

owner = 'Bongo'
behavior = ['good', 'bad']
mood = ['happy', 'sad']
name = ['Mila', 'Maya', 'Maria']
addictions = ['nicotine', 'shopping']


def behDecision(behavior, mood):

    '''
    Robot makes a decision based on the behavior
    '''

    for b in behavior:
        if b == 'good':
            print 'Your behavior is GOOD', name[0]
            for m in mood:
                if m == 'sad':
                    print 'But you are SAD'
            break

        else:
            print 'You behavior is bad'
            print 'Do NOT miss behave'
            print 'Adive with', owner


print behDecision(behavior, mood)
