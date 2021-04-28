import numpy as np 
import time
from colorama import *

start = time.time()
binary = np.random.randint(2, size=(2, 100))

test = 0 
def whileloop():
	while test == 0: 
		binary = np.random.randint(2, size=(2, 4))

		if binary[1] == "[0 0 0 0]":
			break
		else:
			print(f"found index 1 {binary[1]}")
#print(binary[1])
def works_1():
	while test == 0: 
		binary = np.random.randint(2, size=(2, 8))
		match = 1
		if not match in binary:
			print(f"done found {binary}")
			print('It took', time.time()-start, 'seconds.')
			break
		else : 
			print(binary[1])
def prYellow(skk):
	print("\033[93m {}\033[00m" .format(skk))

def works_1_ver2():
	for i in range(0,100000000000000000): 
		lengh = 20
		binary = np.random.randint(2, size=(2, lengh))
		match = 1
		if not match in binary:
			a = (f"Using 2x{lengh} matrix ; found {binary} \n  ",f"at {i} tries", time.time()-start, 'seconds.')
			print(prYellow(a))
			break
		else : 
			print(Fore.RED + "processing..."+ Fore.RESET)
			

works_1_ver2()			
# notes : 
# add time finish done 
# add speed thread process 		