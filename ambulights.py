from firebase import firebase 
import RPi.GPIO as GPIO # GPIO library to interface with the GPIO pins  

GPIO.setmode(GPIO.BCM) # use the bcm pin configuration
GPIO.setwarnings(False) # supress the warnings


GPIO.setup(16, GPIO.OUT) # configure pins to be used as output for route 1
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

GPIO.output(20, GPIO.HIGH) # configure pins to be used as input for route 2
GPIO.output(16, GPIO.HIGH)
GPIO.output(21, GPIO.HIGH)

def returnMatches(a,b): # function to compare two lists and return the length of matche
    return len(list(set(a) & set(b)))


print("Connectiog to firebase....")
firebase = firebase.FirebaseApplication('https://ambulance-80283.firebaseio.com/', None) # connect to the firebase database
print("Connection to firebase successful.")
print("Collecting routes....")
# get the routes from firebase
ItonicsToKingsCollege = firebase.get('/routes/ItonicsToKingsCollege/-Lw-KKLIq9ZCCC9etLq8', None)
ItonicsToRBB = firebase.get('/routes/ItonicsToRBB/-Lw-JHJXTxjg0u00oDNI', None)
ItonicsToRoyalFutsal = firebase.get('/routes/ItonicsToRoyalFutsal/-Lw-JlBZa9c9yxvIb_fL', None)

try:
 while 1:# loop to run the program continuously
    user = firebase.get('/users/namastebb@gmail,com/',None) # get the ambulance user data from firebase
    if(user['online']): #
        currentRoute = firebase.get('/users/namastebb@gmail,com/routes',None) #
        print("Routes collection successful.")
        # compare the current route with the routes in firebase
        match1 = (returnMatches(ItonicsToKingsCollege, currentRoute))
        match2 = (returnMatches(ItonicsToRBB, currentRoute))
        match3 = (returnMatches(ItonicsToRoyalFutsal, currentRoute))
        
        if(match1>3 or match2>3 or match3>3): # compare the lenght of the matches to see if the user is on a route
            if (match1 > match2) and (match1 > match3):
                GPIO.output(20, GPIO.LOW)
                GPIO.output(16, GPIO.HIGH)
                GPIO.output(21, GPIO.HIGH)
                print("route1")
            elif (match2 > match1) and (match2 > match3):
                GPIO.output(20, GPIO.HIGH)
                GPIO.output(16, GPIO.LOW)
                GPIO.output(21, GPIO.HIGH)
                print("route2")
            else:
                GPIO.output(20, GPIO.HIGH)
                GPIO.output(16, GPIO.HIGH)
                GPIO.output(21, GPIO.LOW)
                print("route3")
                       
    else: # if the user is not online, the program will wait for the user to log in
        GPIO.output(20, GPIO.HIGH)
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(21, GPIO.HGIH)
        print("Watiting for user....")
            
except KeyboardInterrupt: # if the user presses ctrl + c, the program will exit
    print("server going down....")
    GPIO.cleanup()
    print("GPIO cleaned.")
