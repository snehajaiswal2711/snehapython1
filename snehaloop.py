
import random
i=0

while(i<=100):
    n=input("press r to roll a dice:")
    if(n=='r'):
        r=random.randint(1,6)
        i=i+r
        print("u got  ",r)
        print("u r on",i)
        if(i==3):
            i=34
            print("go to 34")
        if(i==8):
            i=37
            print("go to 37")
        if(i==11):
            i=2
            print("go to 2")
        if(i==25):
            i=4
            print("go to 4")
        if(i==40):
            i=68
            print("go to 68")
        if(i==38):
            i=9
            print("go to 9")
        if(i==52):
            i=81
            print("go to 81")
        if(i==65):
            i=46
            print("go to 46")
        if(i==76):
            i=97
            print("go to 97")
        if(i>100):
            print("congrats")
        if(i==89):
            i=70
            print("go to 70")
        if(i==93):
            i=64
            print("go to 64")
            
        
