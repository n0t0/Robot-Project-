# Ra (Robot Adviser)


owner = 'Bongo'
name = ['Mila', 'Maya', 'Maria']
behavior = ['good', 'bad']
mood = ['happy', 'sad']

def hello():
    user = raw_input('What is your name? ')
    if user in name:
        print 'Hi', user
        print raw_input('How are you? ')
    else:
        print 'Hi {}. Nice to meet you. My owner is {}'.format(user, owner)
        print 'Analysing...'
        print 'Implanting...'
        print 'Added to database'

print hello()

print '===='*40
print '||||'*40
print '===='*40

# from physical import Physical

def behDecision(behavior, mood):

    '''
    Robot makes a decision based on the behavior
    '''

    for b in behavior: # needs a while loop
        if b == 'good':
            print 'Your behavior is GOOD', name[0]
            for m in mood:
                if m == 'sad':
                    print 'But you are SAD'
            break

        else:
            print 'You behavior is bad'
            print 'Do NOT miss behave'
            print 'Adsive with', owner


print behDecision(behavior, mood)
