#in this we'll be taking input from user for the time (in seconds), and starts a countdown to zero
#displaying every second live

import time

seconds = int(input('enter time in seconds: '))

#countdown loop
while seconds>0:
    print(f"time left: {seconds} seconds")
    time.sleep(1)
    seconds -= 1
    
print("Times up")