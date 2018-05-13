import time, sys

from blink1.blink1 import Blink1

colors = ['black', 'white', 'yellow', 'blue', 'red', 'green']
i = 1

blink1_serials = Blink1.list()
print("blink(1) devices found: " + ','.join(blink1_serials))
try:
    b1 = Blink1()
except:
    print("no blink1 found")
    sys.exit()
print("blink(1) found")

patron = input("Numero de pasos: ")
tiempo = input("Tiempo por paso: ")

while i <= patron:
    temp = str(raw_input("color paso " + str(i) + ": "))
    if temp in colors:
        b1.writePatternLine(tiempo*1000, temp,  i)
        i = i + 1
    else:
        print("Color no reconocido")
    
print("Reproducionedo patron")
b1.play()
time.sleep(patron*tiempo + 1)

temp = str(raw_input("Desea salvar el patron? Y/N: "))
if temp == "Y":
   b1.savePattern()
elif temp == "N":
    j = 1
    while j <= 16:
        b1.writePatternLine(10, 'black',  j)
        j = j + 1

b1.stop()
b1.close()
