# BRF ~ Bsto Robo Frnd
# r0b0t0

owner = 'Bongo'
home = 'Gipsy Mahala'
friends = ['mila', 'maya', 'maria'] # list of friends
mood = ['good', 'bad', 'happy', 'sad', 'lazy'] # list of common moods
#behavior = ['good', 'bad']


def hello():
    user = input('What is your name?\n').lower()
    if user in friends:
        print ('Hi'), user.upper()
        # mv ln24 def emotion_detect(): function checking for user's state
        # pass emotion_detect() as an argument to behDecision()
    else:
        print ('Hi {}. It is nice to meet you! My owner is {}'.format(user, owner.upper()))
        print ('Analysing...')    # func needed (Amazon Rekognition)
        print ('Implanting...')  # func needed (Amazon Polly)
        print ('Added to database')   # lambda func to DynamoDB

print (hello())


def emotion_detect():

    # ToDo:
    # pass the output to a list for comparison
    # Try emotion(mood)

    m = input('How are you?\n').lower()
    while m in mood:
        if m == 'good':    # list all good moods
            print ('Happy face. :)')
            print ('Do you want to play a game?')   # input/sync with games
            break
        elif m == 'bad':    # list all bad moods
            print ("I'm sorry. Cheer up.")
            break
        else:   # the rest of the list with moods goes here
            print ('Tell more about it')
            print ('What made you'), m + ('?')
            break
    else:
        print ('Emotion not detected')
        print ('Ask another question')

print (emotion_detect())

# from physical import Physical

# behavior = str(emotion_detect())  # functions: behCheck(), emotion_detect()

# def behCheck(emotion):
#
#     # Behavioral Check compares emotional and physical arguments
#     # The result calls for -- implanting function
#
#     '''     Robot makes a decision based on the behavior     '''
#     for b in behavior:
#         while behavior == 'good':
#             print 'Good'
#             break
#         else:
#             print 'Take action' # call another function
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

    #print emotion_detect()

# print behCheck(emotion)
