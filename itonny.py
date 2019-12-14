from firebase import firebase
import RPi.GPIO as GPIO   
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

GPIO.output(20, GPIO.HIGH)
GPIO.output(16, GPIO.HIGH)
GPIO.output(21, GPIO.HIGH)

def returnMatches(a,b):
    return len(list(set(a) & set(b)))

print("Connectiog to firebase....")
firebase = firebase.FirebaseApplication('https://ambulance-80283.firebaseio.com/', None)
print("Connection to firebase successful.")
print("Collecting routes....")
ItonicsToKingsCollege = firebase.get('/routes/ItonicsToKingsCollege/-Lw-KKLIq9ZCCC9etLq8', None)
ItonicsToRBB = firebase.get('/routes/ItonicsToRBB/-Lw-JHJXTxjg0u00oDNI', None)
ItonicsToRoyalFutsal = firebase.get('/routes/ItonicsToRoyalFutsal/-Lw-JlBZa9c9yxvIb_fL', None)

try:
 while 1:
    user = firebase.get('/users/namastebb@gmail,com/',None)
    if(user['online']):
        currentRoute = firebase.get('/users/namastebb@gmail,com/routes',None)
        print("Routes collection successful.")
        match1 = (returnMatches(ItonicsToKingsCollege, currentRoute))
        match2 = (returnMatches(ItonicsToRBB, currentRoute))
        match3 = (returnMatches(ItonicsToRoyalFutsal, currentRoute))
        
        if(match1>3 or match2>3 or match3>3): 
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
                       
    else:
        GPIO.output(20, GPIO.HIGH)
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(21, GPIO.HGIH)
        print("Watiting for user....")
            
except KeyboardInterrupt:
    print("server going down....")
    GPIO.cleanup()
    print("GPIO cleaned.")
