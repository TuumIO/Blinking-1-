import time
from blink1.blink1 import Blink1

blink1_serials = Blink1.list()
print("blink(1) devices found: " + ','.join(blink1_serials))

b1 = Blink1()
b1.fade_to_rgb(1000, 64, 64, 64)
time.sleep(3)
b1.fade_to_rgb(1000, 255, 255, 255)
blink1.close()
