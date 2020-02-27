import random
import statistics
import math
'''
Import your own temperature lists here...
'''
import a3


randomtempgen = [] # Random Temperature Generator standard deviation list.

def actuatortrigger(num, fpos, fneg, sensdef = 3): # Categorizes temperature based on range, and calls features.
	if num > sensdef:
		fpos(num)
	elif - sensdef <= num <= sensdef: # Sensativity modification.
		print("Saving Energy and", end = ' ')
	elif num < sensdef:
		fneg(num)
	else:
		print("Error")

def aircon(num):
	print("Cooling down and", end = ' ')
	'''
	Add Air conditioning command...
	'''

def heater(num): 
	print("Heating up and", end = ' ')
	'''
	Add heating command...
	'''

def hvac(thresh, sensorval):
	actuatortrigger(sensorval - thresh, aircon, heater) # actuatortrigger(Adjusted_temperature, print_call, print_call).

def stdcalc(stdlist):
	mean = sum(stdlist) / len(stdlist)
	std = math.sqrt(((1 / (len(stdlist) - 1))) * (sum(pow(x - (mean), 2) for x in stdlist)))
	return std

'''
Random Temperature Test Generator - Generates random numbers up to specified range for test purposes.
'''
print("-= Random Temperature Generator =-")
def randomsensor(min, max, thresh): # Random temperature simulation generator.
	return min + (max - min) * random.random() + thresh

for i in range(10): # Calls randomsensor 10 times.
	sensorval = randomsensor(-10, 10, 70) # randomsensor(minimum_temperature_range, maximum_temperature_range, threshold)
	randomtempgen.append(sensorval)
	print("Sensing...", round(sensorval, 5), hvac(70, sensorval)) # "Sensing..." random_temperatures, hvac(threshold, random_temperatures).

'''
Inputted List Data Handle - Stream or add data from list using the code for analysis.
'''
print("-= Inputted List Values =-")
for sensorval in a3.data[:10]:
	print("Sensing...", round(sensorval, 5), hvac(70, sensorval)) # "Sensing...", inputted_list, hvac(threshold, inputted_list).


'''
Basic Statistical function calls...
'''
print("-= Statistics Based on Data =-")
print("The standard deviation is", round((math.sqrt(((1 / (len(randomtempgen) - 1))) * (sum(pow(x - (sum(randomtempgen) / len(randomtempgen)), 2) for x in randomtempgen)))), 5)) # Standard deviation of random_temperatures with a for loop.
print("The standard deviation is ", round(stdcalc(randomtempgen), 5)) # Finds Standard deviation with function call.
print("The standard deviation is ", round(statistics.stdev(randomtempgen), 5)) # Standard deviation of random_temperatures.
print("The standard deviation of A3 data is", round(statistics.stdev(a3.data), 5)) # Standard deviation of inputted_list.


'''
2.b. What happens when the value fluctuates around the threshold?
	-- The way this function is handled could lead to some odd results particularly around the threshhold. 
	This is around zero or 70 once the 70 is added. The data particularly loses meaning when you consider 
	the introduction of exponentially small decimal places away from the threshold. The function we are 
	using becomes meaningless because we don't have a middle of the road handler that can determine if the 
	Standard deviation is at the threshold.
'''