# BRF


owner = 'Bongo'
friends = ['mila', 'maya', 'maria'] # list of friends
behavior = ['good', 'bad']
mood = ['good', 'bad', 'happy', 'sad'] # list of common moods


def hello():
    user = raw_input('What is your name? ').lower()
    if user in friends:
        print 'Hi', user.upper()
        # mv ln24 def emotion(): function checking for user's state
        # pass emotion() as an argument to behDecision()
    else:
        print 'Hi {}. Nice to meet you. My owner is {}'.format(user, owner.upper())
        print 'Analysing...'    # func needed (Amazon Rekognition)
        print 'Implanting...'   # func needed (Amazon Polly)
        print 'Added to database'   # lambda func to DynamoDB

print hello()


def emotion():
    m = raw_input('How are you? ').lower()
    while m in mood:
        if m == 'good':
            print 'Happy face'
            print ':)'
            break
        elif m == 'bad' or 'sad':
            print "I'm sorry. Cheer up."
            break
        else:
            print 'Tell more about it'
            print 'What made you', m + '?'
            break
    else:
        print 'Emotion not detected'
        print 'Ask another question'

print emotion()

# from physical import Physical
def behDecision(emotion):

    # Behavioral Decision compares emotional and physical arguments
    # The result calls for -- implanting function

    '''
    Robot makes a decision based on the behavior
    '''

    if m in emotion == 'good':
        print 'Your behavior is good'
    #elif:
    #    print 'You behavior is bad'
    #    print 'Do NOT miss behave'
    #    print 'Adsive with', owner
    else:
        print 'Take action' # calls another functions


print behDecision(emotion)
