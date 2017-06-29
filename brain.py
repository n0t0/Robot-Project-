# BRF


owner = 'Bongo'
friends = ['mila', 'maya', 'maria'] # list of friends
mood = ['good', 'bad', 'happy', 'sad', 'lazy'] # list of common moods
#behavior = ['good', 'bad']


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

    # ToDo:
    # pass the output to a list for comparison
    # Try emotion(mood)

    m = raw_input('How are you? ').lower()
    while m in mood:
        if m == 'good':
            print 'Happy face'
            print ':)'
            break
        elif m == 'bad' or 'sad':
            print "I'm sorry. Cheer up."
            break
        else:   # the rest of the list with moods goes here
            print 'Tell more about it'
            print 'What made you', m + '?'
            break
    else:
        print 'Emotion not detected'
        print 'Ask another question'

#print emotion()

# from physical import Physical

behavior = str(emotion())  # functions: behCheck(), emotion()


def behCheck(emotion):

    # Behavioral Check compares emotional and physical arguments
    # The result calls for -- implanting function

    '''     Robot makes a decision based on the behavior     '''
    for b in behavior:
        while behavior == 'good':
            print 'Good'
            break
        else:
            print 'Take action' # call another function
    #for b in behavior:
    #    print 'Hmm. We need to pass a few more arguments'


        #if b == 'good':
            #print 'Here a biscuit'
        #else:
            #print 'BAD'
    #elif behavior == 'negative':
    #    print 'Red flag'
    #    print 'You behavior is bad'
    #    print 'Do NOT miss behave'
    #    print 'Adsive with', owner
    #    break
    #else:
        #print 'Take action' # calls another functions

    #print emotion()

print behCheck(emotion)
