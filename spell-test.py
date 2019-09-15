from playsound import playsound

spellings = {
    'forgotten.mp3' : 'forgotten', 
    'forgetting.mp3' : 'forgetting',
    'beginning.mp3' : 'beginning', 
    'beginner.mp3' : 'beginner', 
    'preferred.mp3' : 'preferred', 
    'gardening.mp3' : 'gardening', 
    'gardener.mp3' : 'gardener', 
    'limiting.mp3' : 'limiting', 
    'limited.mp3' : 'limited', 
    'limitation.mp3' : 'limitation'
    }

def get_attempt(key):
    attempt = ""
    while attempt == "":
        playsound('audio/' +  key)
        attempt = raw_input()
    return attempt

marks = 0

for key, value in spellings.items():  
    attempt = get_attempt(key)
    if attempt == value:
        marks += 1
    else:
        print "oops you got it wrong, it should be " + value

print marks