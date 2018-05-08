import time, sys

from blink1.blink1 import Blink1

blink1_serials = Blink1.list()
print("blink(1) devices found: " + ','.join(blink1_serials))
try:
    b1 = Blink1()
except:
    print("no blink1 found")
    sys.exit()
print("blink(1) found")

b1.fade_to_rgb(1000, 64, 64, 64)
time.sleep(3)
b1.fade_to_rgb(1000, 255, 255, 255)
time.sleep(3)
b1.fade_to_rgb(1000, 255, 0, 0)
time.sleep(3)
b1.fade_to_rgb(1000, 0, 255, 0)
time.sleep(3)
b1.fade_to_rgb(1000, 0, 0, 255)
time.sleep(3)
b1.fade_to_rgb(1000, 0, 0, 0)
time.sleep(3)
print("playing full entire pattern")
b1.play()
print("waiting for 10 seconds")
time.sleep(10.0)
print("stopping pattern")
b1.stop()
b1.close()
