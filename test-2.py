import numpy as np 
import matplotlib.pyplot as plt
from colorama import *
import time
import random
import sys

start = time.time()



def data_ana():
    x = np.random.randint(2, size=(2, 2))
    y = np.random.randint(2, size=(2, 2))
    print(x,y)
    plt.figure(figsize=(10, 10))
    plt.title('random bin 0 1 ~by echo')
    plt.plot(x,y)
    plt.show()

def prYellow(skk):
    print("\033[93m {}\033[00m" .format(skk))

def works_1_ver2():
    for i in range(0,100000000000000000): 
        lengh = 5 #lenght of 0x..
        binary = np.random.randint(2, size=(2, lengh))
        match = 1
        if not match in binary:
            timeing = time.time()-start
            a = (f"Using 2x{lengh} matrix ; found {binary} \n  ",f"at {i} tries", time.time()-start, 'seconds.')
            print(prYellow(a))
            plt.figure(figsize=(10, 10))
            plt.title(f'random bin 0 1 (2x{lengh} matrix )~by echo')
            randomlist = random.sample(range(10, 30), lengh)
            plt.plot(binary)
            plt.xlabel("the sweet 0")
            #plt.ylabel("list")
            plt.show()
            break
        else : 
            print(Fore.RED + "processing..."+ Fore.RESET)
def testing():
    import sys 
    test = sys.argv[1]
    print(test)
works_1_ver2()
#testing()            