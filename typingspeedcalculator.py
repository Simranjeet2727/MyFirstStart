from time import *
import random as r

def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1
        except:
            error = error + 1        
    return error

def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_roundoff = round(time_delay,2)
    speed = len(userinput)/ time_roundoff
    return round(speed)

while True:
    ck = input ("Ready to test: yes/no: ")
    if ck == "yes":
        test = ["I like to do programming.","It is difficult but interesting to learn.","It shows errors and results very frequently.","People love to become a programmer in any language."]
        test1 = r.choice(test)
        print("------------------------")
        print("     ***** Typing speed *****")
        print(test1)
        print("\n\n")
        time_1 = time()
        testinput=input("Start typing: ")
        time_2 = time()

        print("Speed: ",speed_time(time_1,time_2,testinput)," w/sec")
        print("Error: ",mistake(test1,testinput))
    elif ck == "no":
        print(" Thank you ")
        break

    else:
        print("wrong input")      