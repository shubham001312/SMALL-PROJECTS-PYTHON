import datetime
import sys
sys.stdout.reconfigure(encoding='utf-8')
from datetime import time
import time as t
def flag_initiate():
        orange = "🟧"
        green = "📗"
        sudarshan = "🔵"
        white="🤍"
        print("Flag Initiated")
        print("Flag Name: " + "Indian Flag")
        upper = 0
        middle = 1
        lower = 0
        for i in range (3):
             for i in range (10):
                print(orange,end="")
                t.sleep(0.1)
                upper+=1
             print()
        for i in range (3):
             if i==0 or i ==2:
                 for i in range(10):
                     print(white,end="")
                     t.sleep(0.1)
             else:
                 for i in range (4):
                    print(white,end="")
                    t.sleep(0.1)
                 for i in range (4,6):
                   print(sudarshan,end="")
                   t.sleep(0.1)
                 for i in range (4):
                   print(white,end="")
                   t.sleep(0.1)
             print()
        for i in range (3):
             for i in range (10):
                print(green,end="")
                t.sleep(0.1)
             print()
        
flag_initiate()
print(f"JAI HIND JAI BHARAT",end="")
def final_salute():
    dot="."
    for i in range (30):
        print(dot,end="")
        t.sleep(0.1)
print() 
final_salute()