import RPi.GPIO as GPIO
import time

ledPin = 11
buttonPin = 12

def setup():
    print ('Program is starting...')
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
def loop_stay():
    push_state = False
    LED_turnedON = False
    while True:
        if GPIO.input(buttonPin)==GPIO.LOW:
            push_state = True
        
        if(push_state == True):
            if(LED_turnedON == False):
                print ('led on ...')
                GPIO.output(ledPin,GPIO.HIGH)
                LED_turnedON = True
                
            else:
                print ('led off ...')
                GPIO.output(ledPin,GPIO.LOW)
                LED_turnedON = False
                
            push_state = False
            
        time.sleep(0.1)

def loop():
    while True:
        if GPIO.input(buttonPin)==GPIO.LOW:
            GPIO.output(ledPin,GPIO.HIGH)
            print ('led on ...')
        else :
            GPIO.output(ledPin,GPIO.LOW)
            print ('led off ...')
        time.sleep(0.05)

def destroy():
    GPIO.output(ledPin, GPIO.LOW)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        #loop()   # This will keep LED ON until it is pushed
        loop_stay() # Push to ON and Push to OFF
    except KeyboardInterrupt:
    #destroy() will be executed.
        destroy()