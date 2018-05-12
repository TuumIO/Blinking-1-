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

b1.writePatternLine( 1000, 'yellow',  1)
b1.writePatternLine( 1000, 'blue',  2)
b1.writePatternLine( 1000, 'red',  3)

print("playing pattern")
b1.play()
time.sleep(5)
print("stopping pattern")
b1.stop()
b1.close()
