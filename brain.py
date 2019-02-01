# BRF ~ Best Robo Friend
# r0b0t0

owner = 'Bongo'
home = 'Gipsy Mahala'
friends = ['mila', 'maya', 'maria']  # list of friends (token to facebook)
mood = ['good', 'bad', 'happy', 'sad', 'lazy']  # list of common moods
# behavior = ['good', 'bad']
new_friends = []


def hello():
    '''
    Greet the person. 
    Add to database if BRF made a new friend.
    '''
    user = input('What is your name?\n').lower()
    if user in friends:
        print('Hi', user.upper(), '!')
        # check database
        # add friends list to dynamodb
        # api token to facebook
        # vault

        # mv ln24 def emotion_detect(): function checking for user's state
        # pass emotion_detect() as an argument to behDecision()
    else:
        print ('Hi {}. It is nice to meet you! My owner is {}'.format(
            user.title(), owner.upper()))
        print ('Analysing...')    # func needed (Amazon Rekognition)
        print ('Implanting...')  # func needed (Amazon Polly)
        new_friends.append(user)
        print ('Added to database')   # lambda func to DynamoDB
        print (new_friends)


# hello()


def emotion_detect():
    '''
    This function should be triggered after hello().
    Every 5 minutes.
    When a person takes an action.
    '''

    # ToDo:
    # pass the output to a list for comparison
    # Try emotion(mood)

    m = input('How are you?\n').lower()
    while m in mood:
        if m == 'good':    # list all good moods
            print ('Happy face. :)')
            print ('Do you want to play a game?')   # input/sync with games
            # supermario docker imageb
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


# emotion_detect()

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
# for b in behavior:
#    print 'Hmm. We need to pass a few more arguments'

# if b == 'good':
# print 'Here a biscuit'
# else:
# print 'BAD'
# elif behavior == 'negative':
#    print 'Red flag'
#    print 'You behavior is bad'
#    print 'Do NOT miss behave'
#    print 'Adsive with', owner
#    break
# else:
# print 'Take action' # calls another functions

# print emotion_detect()

# print behCheck(emotion)
