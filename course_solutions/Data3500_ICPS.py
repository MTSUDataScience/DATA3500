#########################
####### SOLUTION ########
#########################

### git clone
### git status
### git add
### git commit -m "message here"
### git push (login first time)


import pandas as pd
import numpy as np
import math

    
def solution1_1():
  print('The formula for this problem is: 100 * 1.1 ** 7')
  print('The answer to this problem is:', 100 * 1.1 ** 7)

def solution1_2():
  print('The code you will want to type is: print(\'After 7 years I have $\', (100 * 1.1 ** 7))')
  print('The answer to this problem is: After 7 years I have $',(100 * 1.1 ** 7))

def solution1_3():
  print('The formula for this problem is: bmi = weight / height ** 2')
  height = 1.79
  weight = 65.2
  bmi = weight / height ** 2
  print('The answer to this problem is:', bmi)

def solution1_4():
  print('Create savings with the code savings = 100')
  print('Create growth_multiplier with the code growth_multiplier = 1.1')
  print('Create result with the code results = savings * growth_multiplier ** 7')
  savings = 100
  growth_multiplier = 1.1
  result = savings * growth_multiplier ** 7
  print('')
  print('The value of result is:',result)  

def solution1_5():
  print('Create desc with the code desc = \'compound interest\'')
  print('Create profitability with the code profitability = \'True\'')
  desc = 'compound interest'
  profitability = 'True'
  print('')
  print('desc is equal to:',desc)
  print('profitability is equal to:',profitability)

def solution1_6():
  print('Calculate year1 as year1 = savings * growth_multiplier')
  print('Check the type of year1 with print(type(year1))')
  print('Calculate doubledesc as doubledesc = desc + desc')
  print('Display the value of doubledesc with print(doubledesc)')
  savings = 100
  growth_multiplier = 1.1
  desc = 'compound interest'
  year1 = savings * growth_multiplier
  print('')
  print('year1 is type:',type(year1))
  doubledesc = desc + desc
  print('doubledesc is equal to:',doubledesc) 

def solution1_7():
  print('The fix is: \'I started with \' + str(savings) + \' and now have \' + str(result) + \'.\'')
  savings = 100
  result = 100 * 1.10 ** 7
  print('The output will now look like:','I started with ' + str(savings) + ' and now have ' + str(result) + '.')
  print('')
  pi_string = '3.1415926'
  print('Convert pi_string to a float with: pi_float = float(pi_string)')
  print('You can check the type of pi_float with: print(type(pi_float))')
  pi_float = float(pi_string)
  print('')
  print('pi_float is of type:', type(pi_float))

def solution1_8():
  print('Create the room size variables one at a time as: hall = 11.25, kit = 18.0, liv = 20.0, bed = 10.75, bath = 9.5')
  print('Create the list of lists as: house = [["hallway", hall],["kitchen", kit],"living room", liv],["bedroom", bed],["bathroom", bath]]')
  print('')
  hall = 11.25
  kit = 18.0
  liv = 20.0
  bed = 10.75
  bath = 9.50
  house = [['hallway', hall],
           ['kitchen', kit],
           ['living room', liv],
           ['bedroom', bed],
           ['bathroom', bath]]
  print('Printing the new list displays:', house)
  print('The type of house is:', type(house)) 
  
def solution1_9():
  print('Select and print the second element with: print(areas[1])')
  print('Print the last element from the list with: print(areas[-1])')
  print('Print the area of the living room with: print(areas[5])')
  areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
  print('')
  print('The second element is:', areas[1])
  print('The last element is:', areas[-1])
  print('The area of the living room is:', areas[5]) 

def solution1_10():
  print('Create and sum your new variable with: eat_sleep_areas = areas[3] + areas[-3]')
  print('You do not have to use backwards indexing if you do not want to.')
  print('Print your new variable with: print(eat_sleep_areas)')
  print('')
  areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
  eat_sleep_areas = areas[3] + areas[-3]
  print('The new variable should look like:', eat_sleep_areas) 

def solution1_11():
  print('One solution to creating downstairs is: downstairs = areas[0:6]')
  print('Another solution is: downstairs = areas[:6]')
  print('One solution to creating upstairs is: upstairs = areas[6:10]')
  print('Another solution is: upstairs = areas[6:]')
  print('One final option is: upstairs = areas[-4:]')
  print('')
  areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
  downstairs = areas[:6]
  upstairs = areas[-4:]
  print('Downstairs should look like:', downstairs)
  print('Upstairs should look like:', upstairs) 

def solution1_12():
  print('We can correct bathroom with: areas[-1] = 10.50')
  print('We can change bedroom to master bedroom with: areas[6] = \'master bedroom\'')
  print('')
  areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
  areas[-1] = 10.50
  areas[6] = 'master bedroom'
  print('Our new list looks like:', areas)  

def solution1_13():
  print('You can add the elements with: areas_1 = areas + [\'poolhouse\', 24.5]')
  print('You can add the garage elements with: areas_2 = areas_1 + [\'garage\', 15.45')
  print('')
  areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
  areas_1 = areas + ['poolhouse', 24.5]
  areas_2 = areas_1 + ['garage', 15.45]
  print('areas_1 now looks like:', areas_1)
  print('areas_2 now looks like:', areas_2)  

def solution1_14():
  print('You can use print and type together as: print(type(var1))')
  print('You can use len and print together as: print(len(var1))')
  print('You can create out2 as: out2 = int(var2)')
  print('')
  var1 = [1, 2, 3, 4]
  var2 = True
  print('The solution to print and type is:', type(var1))
  print('The solution to len and print is:', len(var1))
  out2 = int(var2)
  print('out2 is:', out2)  

def solution1_15():
  print('You can create full as: full = first + second')
  print('You can sort full as: full_sorted = sorted(full, reverse = True)')
  print('You can print full_sorted with: print(full_sorted)')
  print('')
  first = [11.25, 18.0, 20.0]
  second = [10.75, 9.50]
  full = first + second
  print('full looks like:', full)
  full_sorted = sorted(full, reverse = True)
  print('full_sorted becomes:', full_sorted)        

def solution1_16():
  print('We can use upper() by: place_up = place.upper()')
  print('we can print each variable with: print(place) and print(place_up)')
  print('We can calculate the number of o\'s with: print(place.count(\'o\'))')
  print('')
  place = 'poolhouse'
  place_up = place.upper()
  print('The use of upper results in:', place_up)
  print('place looks like:', place)
  print('place_up looks like:', place_up)
  print('The number of o\'s in place is:', place.count('o'))

def solution1_17():
  print('We can obtain index of value 20 with: print(areas.index(20.0))')
  print('We can count how often 9.50 appears with: print(areas.count(9.50))')
  print('')
  areas = [11.25, 18.0, 20.0, 10.75, 9.50]
  print('The index of 20.0 is:', areas.index(20.0))
  print('The number of times 9.50 appears is:', areas.count(9.50))

def solution1_18():
  print('We can append the first value with: areas.append(24.5)')
  print('We append the second value with: areas.append(15.45')
  print('We print this list with: print(areas)')
  print('We reverse the order of the list with: areas.reverse()')
  print('We print the list again wtih: print(areas)')
  print('')
  areas = [11.25, 18.0, 20.0, 10.75, 9.50]
  areas.append(24.5)
  areas.append(15.45)
  print('After appending both values, areas becomes:', areas)
  areas.reverse()
  print('After reversing the oder we have:', areas) 

def solution1_19():
  print('We import the math package with: import math')
  print('We calculate C with: C = 2 * r * math.pi')
  print('We calculate A with: A = math.pi * r ** 2')
  print('')
  r = 0.43
  C = 2 * r * math.pi
  A = math.pi * r ** 2
  print('The value of C is:', C)
  print('The value of A is:', A)

def solution1_20():
  print('Import numpy with: import numpy as np')
  print('Create a numpy array as: np_baseball = np.array(baseball)')
  print('Print the type with: print(type(np_baseball))')
  print('')
  baseball = [180, 215, 210, 210, 188, 176, 209, 200]
  np_baseball= np.array(baseball)
  print('np_baseball looks like:', np_baseball)
  print('The type of np_baseball is:', type(np_baseball))

def solution1_21():
  print('Create a Numpy array with: np_height_in = np.array(height_in)')
  print('We print this new array with: print(np_height_in')
  print('Convert this array to meters with: np_height_m = np_height_in * 0.0254')
  print('We print the final array with: print(np_height_m)')
  print('')
  height_in = [74, 74, 72, 72, 73, 69, 69, 71, 76, 71, 73, 73, 
             74, 74, 69, 70, 73, 75, 78, 79, 76, 74, 76, 72, 
             71, 75, 77, 74, 73, 74, 78, 73, 75, 73, 75, 75, 
             74, 69, 71, 74, 73, 73, 76, 74, 74, 70, 72, 77, 
             74, 70, 73, 75, 76, 76, 78, 74, 74, 76, 77, 81, 
             78, 75, 77, 75, 76, 74, 72, 72, 75, 73, 73, 73, 
             70, 70, 70, 76, 68, 71, 72, 75, 75, 75, 75, 68, 
             74, 78, 71, 73, 76, 74, 74, 79, 75, 73, 76, 74, 
             74, 73, 72, 74, 73, 74, 72, 73, 69, 72, 73, 75, 
             75, 73, 72, 72, 76, 74, 72, 77, 74, 77, 75, 76, 
             80, 74, 74, 75, 78, 73, 73, 74, 75, 76, 71, 73, 
             74, 76, 76, 74, 73, 74, 70, 72] 
  np_height_in = np.array(height_in)    
  print('np_height_in as a Numpy array looks like:', np_height_in, sep='\n')
  np_height_m = np_height_in * 0.0254
  print('np_height_m as a Numpy array looks like:', np_height_m, sep='\n')     

def solution1_22():
  print('We create our new numpy array in meters as: np_height_m = np.array(height_in) * 0.0254')
  print('We create our new numpy array in kilograms as: np_weight_kg = np.array(weight_lb) * 0.453592')
  print('We create bmi as: bmi = np_weight_kg / np_height_m ** 2')
  print('We print our final bmi numpy array as: print(bmi)') 
  print('') 
  height_in = [74, 74, 72, 72, 73, 69, 69, 71, 76, 71, 73, 73, 
             74, 74, 69, 70, 73, 75, 78, 79, 76, 74, 76, 72, 
             71, 75, 77, 74, 73, 74, 78, 73, 75, 73, 75, 75, 
             74, 69, 71, 74, 73, 73, 76, 74, 74, 70, 72, 77, 
             74, 70, 73, 75, 76, 76, 78, 74, 74, 76, 77, 81, 
             78, 75, 77, 75, 76, 74, 72, 72, 75, 73, 73, 73, 
             70, 70, 70, 76, 68, 71, 72, 75, 75, 75, 75, 68, 
             74, 78, 71, 73, 76, 74, 74, 79, 75, 73, 76, 74, 
             74, 73, 72, 74, 73, 74, 72, 73, 69, 72, 73, 75, 
             75, 73, 72, 72, 76, 74, 72, 77, 74, 77, 75, 76, 
             80, 74, 74, 75, 78, 73, 73, 74, 75, 76, 71, 73, 
             74, 76, 76, 74, 73, 74, 70, 72]   
  weight_lb = [180, 215, 210, 210, 188, 176, 209, 200, 231, 180,
             188, 180, 185, 160, 180, 185, 189, 185, 219, 230, 
             205, 230, 195, 180, 192, 225, 203, 195, 182, 188, 
             200, 180, 200, 200, 245, 240, 215, 185, 175, 199, 
             200, 215, 200, 205, 206, 186, 188, 220, 210, 195, 
             200, 200, 212, 224, 210, 205, 220, 195, 200, 260, 
             228, 270, 200, 210, 190, 220, 180, 205, 210, 220, 
             211, 200, 180, 190, 170, 230, 155, 185, 185, 200, 
             225, 225, 220, 160, 205, 235, 250, 210, 190, 160, 
             200, 205, 222, 195, 205, 220, 220, 170, 185, 195, 
             220, 230, 180, 220, 180, 180, 170, 210, 215, 200, 
             213, 180, 192, 235, 185, 235, 210, 222, 210, 230, 
             220, 180, 190, 200, 210, 194, 180, 190, 240, 200, 
             198, 200, 195, 210, 220, 190, 210, 225, 180, 185]
  np_height_m = np.array(height_in) * 0.0254
  np_weight_kg = np.array(weight_lb) * 0.453592  
  print('np_height_m looks like:', np_height_m, sep='\n')   
  print('np_weight_kg looks like:', np_weight_kg, sep='\n')
  bmi = np_weight_kg / np_height_m ** 2
  print('bmi looks like:', bmi, sep='\n')   

def solution1_23():
  print('We convert our height list to a Numpy array in meters with: np_height_m = np.array(height_in) * 0.0254')
  print('We convert our weight list to a Numpy array in kgs with: np_weight_kg = np.array(weight_lb) * 0.453592')
  print('Create our bmi array with: bmi = np_weight_kg / np_height_m ** 2')
  print('Create light with: light = bmi < 21')
  print('Print light with: print(light)')
  print('Subset bmi with light and print with: print(bmi[light])')
  print('')
  height_in = [74, 74, 72, 72, 73, 69, 69, 71, 76, 71, 73, 73, 
             74, 74, 69, 70, 73, 75, 78, 79, 76, 74, 76, 72, 
             71, 75, 77, 74, 73, 74, 78, 73, 75, 73, 75, 75, 
             74, 69, 71, 74, 73, 73, 76, 74, 74, 70, 72, 77, 
             74, 70, 73, 75, 76, 76, 78, 74, 74, 76, 77, 81, 
             78, 75, 77, 75, 76, 74, 72, 72, 75, 73, 73, 73, 
             70, 70, 70, 76, 68, 71, 72, 75, 75, 75, 75, 68, 
             74, 78, 71, 73, 76, 74, 74, 79, 75, 73, 76, 74, 
             74, 73, 72, 74, 73, 74, 72, 73, 69, 72, 73, 75, 
             75, 73, 72, 72, 76, 74, 72, 77, 74, 77, 75, 76, 
             80, 74, 74, 75, 78, 73, 73, 74, 75, 76, 71, 73, 
             74, 76, 76, 74, 73, 74, 70, 72]   

  weight_lb = [180, 215, 210, 210, 188, 176, 209, 200, 231, 180,
             188, 180, 185, 160, 180, 185, 189, 185, 219, 230, 
             205, 230, 195, 180, 192, 225, 203, 195, 182, 188, 
             200, 180, 200, 200, 245, 240, 215, 185, 175, 199, 
             200, 215, 200, 205, 206, 186, 188, 220, 210, 195, 
             200, 200, 212, 224, 210, 205, 220, 195, 200, 260, 
             228, 270, 200, 210, 190, 220, 180, 205, 210, 220, 
             211, 200, 180, 190, 170, 230, 155, 185, 185, 200, 
             225, 225, 220, 160, 205, 235, 250, 210, 190, 160, 
             200, 205, 222, 195, 205, 220, 220, 170, 185, 195, 
             220, 230, 180, 220, 180, 180, 170, 210, 215, 200, 
             213, 180, 192, 235, 185, 235, 210, 222, 210, 230, 
             220, 180, 190, 200, 210, 194, 180, 190, 240, 200, 
             198, 200, 195, 210, 220, 190, 210, 225, 180, 185]
  np_height_m = np.array(height_in) * 0.0254
  np_weight_kg = np.array(weight_lb) * 0.453592
  bmi = np_weight_kg / np_height_m ** 2
  light = bmi < 21         
  print('light looks like:', light, sep='\n')
  print('bmi subset with light looks like:', bmi[light], sep='\n') 

def solution1_24():
  print('We convert our height list to a Numpy array with: np_height_m = np.array(height_in)')
  print('We convert our weight list to a Numpy array iwith: np_weight_kg = np.array(weight_lb)')
  print('We print out weight at index 50 with: print(np_weight_lb[50]')
  print('We print a sub-array that contains elements at index 100 up to and including index 100 with: print(np_height_in[100:111]')
  print('')
  height_in = [74, 74, 72, 72, 73, 69, 69, 71, 76, 71, 73, 73, 
             74, 74, 69, 70, 73, 75, 78, 79, 76, 74, 76, 72, 
             71, 75, 77, 74, 73, 74, 78, 73, 75, 73, 75, 75, 
             74, 69, 71, 74, 73, 73, 76, 74, 74, 70, 72, 77, 
             74, 70, 73, 75, 76, 76, 78, 74, 74, 76, 77, 81, 
             78, 75, 77, 75, 76, 74, 72, 72, 75, 73, 73, 73, 
             70, 70, 70, 76, 68, 71, 72, 75, 75, 75, 75, 68, 
             74, 78, 71, 73, 76, 74, 74, 79, 75, 73, 76, 74, 
             74, 73, 72, 74, 73, 74, 72, 73, 69, 72, 73, 75, 
             75, 73, 72, 72, 76, 74, 72, 77, 74, 77, 75, 76, 
             80, 74, 74, 75, 78, 73, 73, 74, 75, 76, 71, 73, 
             74, 76, 76, 74, 73, 74, 70, 72]   

  weight_lb = [180, 215, 210, 210, 188, 176, 209, 200, 231, 180,
             188, 180, 185, 160, 180, 185, 189, 185, 219, 230, 
             205, 230, 195, 180, 192, 225, 203, 195, 182, 188, 
             200, 180, 200, 200, 245, 240, 215, 185, 175, 199, 
             200, 215, 200, 205, 206, 186, 188, 220, 210, 195, 
             200, 200, 212, 224, 210, 205, 220, 195, 200, 260, 
             228, 270, 200, 210, 190, 220, 180, 205, 210, 220, 
             211, 200, 180, 190, 170, 230, 155, 185, 185, 200, 
             225, 225, 220, 160, 205, 235, 250, 210, 190, 160, 
             200, 205, 222, 195, 205, 220, 220, 170, 185, 195, 
             220, 230, 180, 220, 180, 180, 170, 210, 215, 200, 
             213, 180, 192, 235, 185, 235, 210, 222, 210, 230, 
             220, 180, 190, 200, 210, 194, 180, 190, 240, 200, 
             198, 200, 195, 210, 220, 190, 210, 225, 180, 185]
  np_weight_lb = np.array(weight_lb)
  np_height_in = np.array(height_in)       
  print('index 50 looks like:', np_weight_lb[50], sep='\n')
  print('sub-array 100 through 110 looks like:', np_height_in[100:111], sep='\n')

def solution1_25():
  print('We create np_baseball with: np_baseball = np.array(baseball)')
  print('We can print the type of np_baseball with: print(type(np_baseball))')
  print('We can see the shape of np_baseball with: print(np_baseball.shape)')
  print('')
  baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]
  np_baseball = np.array(baseball)
  print('np_baseball as a Numpy array looks like:', np_baseball, sep='\n')  
  print('The type of np_baseball is:', type(np_baseball))
  print('The shape of np_baseball is:', np_baseball.shape)        
    
def solution1_26():
  print('We create np_baseball with: np_baseball = np.array(baseball)')
  print('We can see the shape of np_baseball with: print(np_baseball.shape)')
  print('We can print the 8th row with: print(np_baseball[7,:])')
  print('We can select the entire 2nd column with: np_weight_lb = np_baseball[:,1]')
  print('We can print the heiht of the 12th player with: print(np_baseball[11,0])')
  print('')
  baseball = [[74, 180],
            [74, 215],
            [72, 210],
            [72, 210],
            [73, 188],
            [69, 176],
            [69, 209],
            [71, 200],
            [76, 231],
            [71, 180],
            [73, 188],
            [73, 180],
            [74, 185],
            [74, 160],
            [69, 180]]
  np_baseball = np.array(baseball)
  np_weight_lb = np_baseball[:,1]
  print('np_baseball as a Numpy array looks like:', np_baseball, sep='\n')  
  print('The shape of np_baseball is:', np_baseball.shape)   
  print('The 8th row looks like:', np_baseball[7,:])
  print('The second column looks like:', np_weight_lb, sep='\n') 
  print('The height of the 12th player is:', np_baseball[11,0])  

def solution1_27():
  print('We create np_baseball with: np_baseball = np.array(baseball)')
  print('We create np_updated with: np_updated = np.array(updated)')  
  print('We can see the addition with: print(np_baseball + updated)')
  print('We can create conversion with: conversion = np.array([0.0254, 0.453592, 1])')
  print('We can print the converted values with: print(np_baseball * conversion)')
  print('')
  baseball = [[74, 180, 23.87],
              [74, 215, 21.96],
              [72, 210, 29.76],
              [72, 210, 22.88],
              [73, 188, 27.54],
              [69, 176, 41.91],
              [69, 209, 19.98],
              [71, 200, 24.55],
              [76, 231, 24.91],
              [71, 180, 28.23],
              [73, 188, 29.17],
              [73, 180, 24.69],
              [74, 185, 21.83],
              [74, 160, 22.76],
              [69, 180, 25.12]]
  updated = [[1.2303559 , -11.16224898, 1],
            [1.02614252,  16.09732309, 1],
            [1.1544228 ,   5.08167641, 1],
            [1.42614252,   9.09732309, 1],
            [1.1244228 ,   5.08167641, 1],   
            [1.53614252,   6.09732309, 1],
            [1.1944228 ,   5.08167641, 1],   
            [1.86614252,  11.24732309, 1],
            [1.2244228 ,   5.26167641, 1],   
            [1.85614252,  14.09732309, 1],
            [1.1549278 ,   8.08167641, 1],   
            [1.02837593,  19.09732309, 1],
            [1.1775937 ,   1.98167641, 1],   
            [1.17393793,  17.37732309, 1],
            [1.1125222 ,   5.11167641, 1]]            
  conversion = np.array([0.0254, 0.453592, 1])
  np_baseball = np.array(baseball)
  np_updated = np.array(updated)
  print('The new array after addition looks like:', np_baseball + updated, sep='\n')
  print('The converted array looks like:', np_baseball * conversion, sep='\n')

def solution1_28():
  print('We create np_height_in with: np_height_in = np_baseball[:,0]')    
  print('We print the mean with: print(np.mean(np_height_in))')
  print('We print the median with: print(np.median(np_height_in))')
  print('')
  baseball = [[74, 180, 23.87],
              [74, 215, 21.96],
              [72, 210, 29.76],
              [72, 210, 22.88],
              [73, 188, 27.54],
              [9969, 176, 41.91],
              [69, 209, 19.98],
              [71, 200, 24.55],
              [76, 231, 24.91],
              [71, 180, 28.23],
              [73, 188, 29.17],
              [73, 180, 24.69],
              [74, 185, 21.83],
              [74, 160, 22.76],
              [69, 180, 25.12]]  
  np_baseball = np.array(baseball)
  np_height_in = np_baseball[:,0]
  print('The mean value is:', np.mean(np_height_in))
  print('The median valie is:', np.median(np_height_in)) 

def solution1_29():
  print('We create np_positions with: np_positions = np.array(positions)')    
  print('We create np_heights with: np_positions = np.array(heights)')
  print('We extract GK heights with: gk_heights = np_heights[np_positions ==\'GK\']')    
  print('We extract other heights with: other_heights = np_heights[np_positions !=\'GK\']')  
  print('We create and display GK median height with: print(\'Median height of goalkeepers: \' + str(np.median(gk_heights)))')  
  print('We create and display other median height with: print(\'Median height of other: \' + str(np.median(other_heights)))')                  
  print('')
  positions = ['GK', 'M', 'A', 'GK', 'GK', 'D', 'A', 'GK', 'D', 'M',
              'M', 'GK', 'A', 'A', 'A', 'D', 'D', 'M', 'D', 'A',
              'GK', 'A', 'M', 'M', 'D', 'A', 'M', 'D', 'A', 'M']
  heights = [191, 187, 188, 194, 192, 190, 177, 187, 171, 159,
            185, 199, 185, 174, 177, 171, 159, 172, 171, 179,
            195, 185, 184, 188, 174, 179, 176, 168, 166, 161]
  np_positions = np.array(positions)
  np_heights = np.array(heights)
  gk_heights = np_heights[np_positions == 'GK']
  other_heights = np_heights[np_positions != 'GK']
  print('gk_heights looks like:', gk_heights, sep='\n')
  print('other_heights looks like:', other_heights, sep='\n')
  print('Median height of goalkeepers: ' + str(np.median(gk_heights)))
  print('Median height of other: ' + str(np.median(other_heights)))

def solution2_1():
    print('We can get the index of Germany with: ind_ger = countries.index(\'germany\')')
    print('We can print the capital of Germany with: print(capitals[ind_ger])')
    print('We create a dictionary with: europe = {\'spain\':\'madrid\',...,\'norway\':\'oslo\'}')
    print('We can see our dictionary with: print(europe)')
    print('We can see the keys with: print(europe.keys())')
    print('We can see the value of key norway with: print(europe[\'norway\'])')
    print('')
    countries = ['spain', 'france', 'germany', 'norway']
    capitals = ['madrid', 'paris', 'berlin', 'oslo']
    ind_ger = countries.index('germany')
    print('ind_ger looks like:', ind_ger)
    print('The capital of Germany is:', capitals[ind_ger])
    europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }
    print('europe looks like:', europe)
    print('The keys are:', europe.keys())
    print('The value that belongs to key norway is:', europe['norway'])

def solution2_2():
    print('We add italy and rome to europe with: europe[\'italy\'] = \'rome\'')
    print('We print italy in europe with: print(\'italy\' in europe)')
    print('We add poland and warsaw with: europe[\'poland\'] = \'warsaw\'')
    print('We print the updated europe with: print(europe)')
    print('')
    europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }
    europe['italy'] = 'rome'
    print('italy in europe looks like:', 'italy' in europe)
    europe['poland'] = 'warsaw'
    print('the updated europe looks like:', europe, sep='\n')
    
def solution2_3():
    print('We can update the capital of germany with: europe[\'germany\'] = \'berlin\'')
    print('We can remove australia with: del(europe[\'australia\'])')
    print('We can see the updated europe with: print(europe)')
    print('')
    europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
              'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
              'australia':'vienna'}
    europe['germany'] = 'berlin'
    del(europe['australia'])
    print('The updated europe looks like:', europe, sep='\n')
    
def solution2_4():
    print('We can print the capital of france with: print(europe[\'france\'][\'capital\'])')
    print('We create data with: data = {\'capital\':\'rome\',\'population\':59.83}')
    print('We add data to euope under key \'italy\' with: europe[\'italy\'] = data')
    print('We can print updated europe with: print(europe)')
    print('')
    europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
               'france': { 'capital':'paris', 'population':66.03 },
               'germany': { 'capital':'berlin', 'population':80.62 },
               'norway': { 'capital':'oslo', 'population':5.084 } } 
    print('The capital of france is:', europe['france']['capital'])
    data = {'capital':'rome','population':59.83}
    print('data looks like:', data)
    europe['italy'] = data
    print('The updated europe looks like:', europe, sep='\n') 

def solution2_5():
    print('You create my_dict with: my_dict = {\'country\':names, \'drives_right\':dr, \'cars_per_cap\':cpc}')
    print('We convert this to a DataFrame with: cars = pd.DataFrame(my_dict)')
    print('We print out cars with: print(cars)')
    print('We set new row labels with: cars.index = row_labels')
    print('')
    names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
    dr =  [True, False, False, False, True, True, True]
    cpc = [809, 731, 588, 18, 200, 70, 45] 
    my_dict = {'country':names, 'drives_right':dr, 'cars_per_cap':cpc}
    cars = pd.DataFrame(my_dict)
    row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG'] 
    print('cars looks like:', cars, sep='\n')
    cars.index = row_labels
    print('The updated cars now looks like:', cars, sep='\n')

def solution2_6():
    print('We import driving with: cars = pd.read_csv(\'Data/driving.csv\', index_col = 0)')
    print('My driving file is located in the subfolder Data, your file may be elsewhere.')
    print('We print cars with: print(cars)')
    print('')
    cars = pd.read_csv('Data/driving.csv', index_col = 0)
    print('Cars looks like:', cars, sep='\n')     

def solution2_7():
    print('We import driving with: cars = pd.read_csv(\'Data/driving.csv\', index_col = 0)')
    print('We print out country as a Series with: print(cars[\'country\')')
    print('We print out country as a DataFrame with: print(cars[[\'country\']])')
    print('We print out country and drives_right as a DataFrame with: print(cars[[\'country\', \'drives_right\']])')
    print('We print the first 3 observations with: print(cars[0:3])')
    print('We print the 4th, 5th, and 6th observations with: print(cars[3:6])')
    print('')
    cars = pd.read_csv('Data/driving.csv', index_col = 0)
    print('country as a Series looks like:', cars['country'], sep='\n')
    print('country as a DataFrame looks like:', cars[['country']], sep='\n')
    print('country and drives_right as a DataFrame look like:', cars[['country', 'drives_right']], sep='\n')
    print('The first 3 observations are:', cars[0:3], sep='\n')
    print('The 4th, 5th, and 6th observations are:', cars[3:6], sep='\n')

def solution2_8():
    print('We print the observation for Hong Kong with: print(cars.loc[\'HK\'])')
    print('We print observations for the United Kingdom and Luxembourg as a DataFrame with: print(cars.loc[[\'UK\',\'LU\']])')
    print('We print drives right for Italy with: print(cars.loc[\'IT\', \'drives_right\'])')
    print('We print the DataFrame of Russia and Italy for columns country and drives_right with: print(cars.loc[[\'RU\', \'IT\'], [\'country\',\'drives_right\']])')
    print('We print drives_right as a Series with: print(cars.iloc[:,[2]])')
    print('We print drives_right as a DataFrame with: print(cars.loc[:,\'drives_right\'])')
    print('We print cars_per_cap and drives_right as a DataFrame with: print(cars.loc[:,[\'cars_per_cap\', \'drives_right\']])')
    print('')
    cars = pd.read_csv('Data/driving.csv', index_col = 0)
    print('Hong Kong looks like:', cars.loc['HK'], sep='\n')
    print('United Kingdom and Luxembourg look like:', cars.loc[['UK', 'LU']], sep='\n')
    print('drives_right for Italy looks like', cars.loc['IT', 'drives_right'], sep='\n')
    print('The DataFrame looks like:', cars.loc[['RU', 'IT'],['country', 'drives_right']], sep='\n')
    print('drives_right as a Series looks like:', cars.iloc[:, [2]], sep='\n')
    print('drives_right as a DataFrame looks like:', cars.loc[:, 'drives_right'], sep='\n')
    print('cars_per_cap and drives_right as a DataFrame looks like:', cars.loc[:,['cars_per_cap', 'drives_right']], sep='\n')
     
def solution2_9():
    print('We can import data with: cars = pd.read_csv(\'Data/driving.csv\', index_col = 0)')
    print('Extract drives_right with: dr = cars[\'drives_right\']')
    print('Subset cars with: sel = cars[dr]')
    print('Print the results with: print(sel)')
    print('Create sel in one line with: sel = cars[cars[\'drives_right\']]')
    print('Create cpc with: cpc = cars[\'cars_per_cap\']')
    print('Create many_cars with: many_cars = cpc > 500')
    print('Create lots_of_cars with: lots_of_cars = cars[many_cars]')
    print('Print lots_of_cars with: print(lots_of_cars)')
    print('Create medium with: medium = cars.loc[(cars[\'cars_per_cap\'] > 100) & (cars[\'cars_per_cap\'] < 500)]')
    print('')
    cars = pd.read_csv('Data/driving.csv', index_col = 0)
    dr = cars['drives_right']
    print('dr looks like:', dr, sep='\n')
    sel = cars[dr]
    print('sel looks like:', sel, sep='\n')
    cpc = cars['cars_per_cap']
    many_cars = cpc > 500
    lots_of_cars = cars[many_cars]
    print('lots_of_cars looks like:', lots_of_cars, sep='\n')
    medium = cars.loc[(cars['cars_per_cap'] > 100) & (cars['cars_per_cap'] < 500)]
    print('medium looks like:', medium, sep='\n')    
    
def solution2_10():
    print('The first line of the while loop is: while addition != 10:')
    print('The second line is: print(\'adding...\')')
    print('The third line is: addition = addition + 1')
    print('The fourth line is: print(addition)')
    print('')
    print('The first line of the new while loop is: while addition != 10:')
    print('The second line is: print(\'adding...\')')
    print('The third line is: if addition < 4:')
    print('The fourth line is: addition = addition + 1')
    print('The fifth line is: else:')
    print('The sixth line is: addition = addition + 2')
    print('The last line is: print(addition)')
    addition = 0
    print('The first while loop looks like:')
    while addition != 10:
        print('adding...')
        addition = addition + 1
        print(addition)
    print('The second while loop looks like:')
    addition = 0
    while addition != 10:
        print('adding...')
        if addition < 4:
            addition = addition + 1
        else:
            addition = addition + 2
        print(addition) 
        
def solution2_11():
    print('The first line is: for x in work:')
    print('The second line is: print(\'the \' + x[0]) + \' is \' + str(x[1]) + \' sqm.\'')
    print('')
    work = [["office", 11.25], 
         ["breakroom", 18.0], 
         ["boardroom", 20.0], 
         ["corner office", 18.75], 
         ["bathroom", 7.50]]
    for x in work:
        print('the ' + x[0] + ' is ' + str(x[1]) + ' sqm.')        

def solution2_12():
    cars = pd.read_csv('Data/driving.csv', index_col = 0)
    print('The first line of the for loop is: for l, r in cars.iterrows():')
    print('The second line is: print(l)')
    print('The third line is: print(r)')
    print('')
    print('The first line is now: for l, r in cars.iterrows():')
    print('The second line is: print(l + \': \' + str(r[\'cars_per_cap\']))')
    print('')
    print('We can add a column by changing the second line to: cars.loc[l, \'C_NAME\'] = r[\'country\'].upper()')
    print('')
    print('We do this using apply with: cars[\'C_NAME_APPLY\'] = cars[\'country\'].apply(str.upper)')
    for l, r in cars.iterrows():
        print(l)
        print(r)
    print('')
    for l, r in cars.iterrows():
        print(l + ': ' + str(r['cars_per_cap']))
    print('')
    for l, r in cars.iterrows():
        cars.loc[l, 'C_NAME'] = r['country'].upper()
    print(cars)
    print('')
    cars['C_NAME_APPLY'] = cars['country'].apply(str.upper)
    print(cars)        

def solution2_13():
    print('We solve this with: square_num = [i**2 for i in range(0,10)]')
    print('')
    print('We solve the nested problem with: nested = [[c for c in range(0,5)] for r in range(0,5)]')
    square_num = [i**2 for i in range(0,10)]
    print('The solution looks like:', square_num, sep='\n')
    nested = [[c for c in range(0,5)] for r in range(0,5)]
    print('The nested data looks like:', nested, sep='\n')
    
def solution2_14(nlight):
    print('The if statement looks like: if room == \'bath\': print(\'Looking for the bathroom\')')
    print('The above is the correct wording, do not forget to indent!')
    print('The next if statement looks like: if lights == 0: print(\'it is dark\')')
    print('The elif and else statement is: if lights == 0: print(\'It is dark\') elif lights < 3: print(\'It is kind of dark\') else: print(\'It is bright\')')
    print('Remember proper indentation!')
    print('')
    room = 'bath'
    lights = nlight
    if room == 'bath':
        print('Looking for the bathroom')
    if lights == 0:
        print('It is dark')
    elif lights < 3:
        print('It is kind of dark')
    else:
        print('It is bright')

def solution2_15():
    print('We create the new list with: long_member = [member for member in members if len(member) >= 7]')
    print('We create empty strings with: empty_member = [member if len(member) >= 7 else \'\' for member in members]')
    print('')
    members = ['frank', 'samuel', 'merlin', 'alejando', 'lucas', 'brendan', 'george']
    long_member = [member for member in members if len(member) >= 7]
    empty_member = [member if len(member) >= 7 else '' for member in members]
    print(long_member)
    print(empty_member)    

def solution3_1():
    print('We import ex1 with: df = pd.read_csv(\'data/ex1.csv\')')
    print('We import ex2 with no headers with: df_noheader = pd.read_csv(\'data/ex2.csv\', header=None)')
    print('We import ex2 with our headers with: df_header = pd.read_csv(\'data/ex2.csv\', names=[\'a\', \'b\', \'c\', \'d\', \'message\'])')
    print('We import ex2 and assign message to the index by adding ,index_col = \'message\' to the end.')
    print('')
    df = pd.read_csv('data/ex1.csv')
    df_noheader = pd.read_csv('data/ex2.csv', header=None)
    df_header = pd.read_csv('data/ex2.csv', names=['a', 'b', 'c', 'd', 'message'])
    df_index = pd.read_csv('data/ex2.csv', names=['a', 'b', 'c', 'd', 'message'], index_col = 'message')
    print('df looks like:', df, sep='\n')
    print('df_noheader looks like:', df_noheader, sep='\n')
    print('df_header looks like:', df_header, sep='\n')
    print('df_index looks like:', df_index, sep='\n')
    
def solution3_2():
    print('We observe the data with: list(open(\'data/ex3.txt\'))')
    print('We use pandas to open the data with: result = pd.read_csv(\'data/ex3.txt\', sep=\'\s+\')')
    print('')
    print('The raw data looks like:', list(open('data/ex3.txt')), sep='\n')
    result = pd.read_csv('data/ex3.txt', sep='\s+')
    print('The clean data looks like:', result, sep='\n')    

def solution3_3():
    df = pd.DataFrame(np.random.randn(7,3))
    df.iloc[1:4, 1] = np.nan
    df.iloc[1:2, 2] = np.nan
    print('We fill values with a 0 with: df.fillna(0)')
    print('We fill values with a forward fill with: df.fillna(method=\'ffill\')')
    print('We fill values with a limited forward fill with: df.fillna(method=\'ffill\', limit=2)')
    print('We fill values with a back fill with: df.fillna(method=\'bfill\')')
    print('We fill values with the mean with: df.fillna(df.mean())')
    print('')
    print('The original data frame looks like:', df, sep='\n')
    print('The 0 fill looks like:', df.fillna(0), sep='\n')
    print('The forward fill looks like:', df.fillna(method='ffill'), sep='\n')
    print('The limited forward fill looks like:', df.fillna(method='ffill', limit=2), sep='\n')
    print('The back fill looks like:', df.fillna(method='bfill'), sep='\n')    

def solution3_4():
    print('We examine ex5 with: pd.read_csv(\'data/ex5.csv\')')
    print('We create our additional missing values with: add_missing = {\'message\': [\'foo\']}')
    print('We import the data with: pd.read_csv(\'data/ex5.csv\', na_values = add_missing)')
    print('')
    result=pd.read_csv('data/ex5.csv')
    print('The original results look like:', result, sep='\n')
    add_missing={'message': ['foo']}
    result_new=pd.read_csv('data/ex5.csv', na_values=add_missing)
    print('The new results look like:', result_new, sep='\n')
    
def solution3_5():
    states = pd.DataFrame({'state': ['Ohio', 'California', 'California', 'Ohio', 'Ohio','California'],
                       'year' : ['2005', '2005', '2006', '2006', '2007','2006'],
                       'pop': [2.2, 7.2, 3.2, 7.7, 2.1, 7.7]})
    tips = pd.read_csv('data/tips.txt')
    small_tip = tips[: 25]
    small_tip.iloc[16::, [2]] = 'Yes'
    small_tip.iloc[2:4, [1]] = np.nan
    small_tip.iloc[6:21, [1]] = np.nan
    small_tip.iloc[23::, [1]] = np.nan
    print('We get the state average with: states[\'pop\'].groupby(states[\'state\']).mean()')
    print('We get the state/year average with: states[\'pop\'].groupby([states[\'state\'], states[\'year\']]).mean()')
    print('We get the state standard deviation with: states[\'pop\'].groupby(states[\'state\']).std()')
    print('We backfill by smoker in the original data frame with: small_tip[\'tip\'] = small_tip[\'tip\'].groupby(small_tip[\'smoker\']).fillna(method=\'bfill\')')
    print('')
    print('The state average is:', states['pop'].groupby(states['state']).mean(), sep='\n')
    print('The state/year average is:', states['pop'].groupby([states['state'],states['year']]).mean(), sep='\n')
    print('The state standard deviation is:', states['pop'].groupby(states['state']).std())
    print('The original data frame looks like:', small_tip, sep='\n')
    small_tip['tip'] = small_tip['tip'].groupby(small_tip['smoker']).fillna(method='bfill')
    print('The backfilled by smoker data is:', small_tip, sep='\n')
    
def solution3_6():
    df = pd.DataFrame({'key': ['foo', 'bar', 'baz'],
                  'A': [1,2,3],
                  'B': [4,5,6],
                  'C': [7,8,9]})
    print('We can melt the dataframe with: df_melted = pd.melt(df, [\'key\'])')
    print('We can go back to the original with: df_original = df_melted.pivot(index=\'key\', columns=\'variable\', values=\'value\')')
    print('We can reset the index with: df_original = df_original.reset_index()')
    print('')
    df_melted = pd.melt(df, ['key'])
    df_original = df_melted.pivot(index='key',columns='variable',values='value')
    df_original = df_original.reset_index()
    print('The melted dataframe looks like:', df_melted, sep='\n')
    print('The final version of df_original looks like:', df_original, sep='\n')    

def solution3_7():
    df1 = pd.DataFrame({'lkey': ['b','b','a','c','a','a','b'],
                   'data1': range(7)})
    df2 = pd.DataFrame({'rkey': ['a','b','d'],
                   'data2': range(3)})
    print('We can merge these two with: pd.merge(df1, df2, left_on=\'lkey\', right_on=\'rkey\')')
    print('We can do an outer merge with: pd.merge(df1, df2, left_on=\'lkey\', right_on=\'rkey\', how=\'outer\')')
    print('')
    df_merged = pd.merge(df1, df2, left_on='lkey', right_on='rkey')
    df_outer = pd.merge(df1, df2, left_on='lkey', right_on='rkey', how='outer')
    print('The merged dataframe looks like:', df_merged, sep='\n')
    print('The outer merge looks like:', df_outer, sep='\n')    
    
    
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def solution4_1():
    print('The solution code is too lengthy to present here. See our class notes for graphing Austin vs. Seattle weather. One beginning piece of advice would be to create two seperate files, one for each station. The solution graphs are presented below.')
    seattle = pd.read_csv('data/seattle_weather.csv')
    station1 = seattle.loc[seattle['STATION'] == 'USC00456295']
    station2 = seattle.loc[seattle['STATION'] == 'USC00454486']
    fig, ax = plt.subplots(2,1, sharey=True) # sharey=True ensures all plots have the same y-axis scale.

    ax[0].plot(station1['DATE'], station1['MLY-PRCP-NORMAL'],'k',color='b',label='Station1')
    ax[0].plot(station1['DATE'], station1['MLY-PRCP-25PCTL'],'k--',color='b',label='Station1 25pct')
    ax[0].plot(station1['DATE'], station1['MLY-PRCP-75PCTL'],'k--',color='b',label='Station1 75pct')
    ax[1].plot(station2['DATE'], station2['MLY-PRCP-NORMAL'],'k',color='r',label='Station2')
    ax[1].plot(station2['DATE'], station2['MLY-PRCP-25PCTL'],'k--',color='r',label='Station2 25pct')
    ax[1].plot(station2['DATE'], station2['MLY-PRCP-75PCTL'],'k--',color='r',label='Station2 75pct')

    ax[0].set_ylabel('Precipitation (inches)')
    ax[1].set_ylabel('Precipitation (inches)')
    ax[1].set_xlabel('Time (month)')
    ax[0].set_xticks([1,2,3,4,5,6,7,8,9,10,11,12])
    ax[0].set_xticklabels(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
    ax[1].set_xticks([1,2,3,4,5,6,7,8,9,10,11,12])
    ax[1].set_xticklabels(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
    ax[0].set_title('USC00456295 (Station 1) Rainfall')
    ax[1].set_title('USC00454486 (Station 2) Rainfall')
    plt.subplots_adjust(hspace=.5)

    fig = plt.figure()
    ax = fig.add_subplot()
    plt.title('Station 1 v. Station 2 Precipitation')
    plt.xlabel('Time (months)')
    plt.ylabel('Precipitation (inches)')
    ax.plot(station1['DATE'], station1['MLY-PRCP-NORMAL'],'k',color='b',label='Station1')
    ax.plot(station1['DATE'], station1['MLY-PRCP-25PCTL'],'k--',color='b',label='Station1 25pct')
    ax.plot(station1['DATE'], station1['MLY-PRCP-75PCTL'],'k--',color='b',label='Station1 75pct')
    ax.plot(station2['DATE'], station2['MLY-PRCP-NORMAL'],'k',color='r',label='Stataion2')
    ax.plot(station2['DATE'], station2['MLY-PRCP-25PCTL'],'k--',color='r',label='Station2 25pct')
    ax.plot(station2['DATE'], station2['MLY-PRCP-75PCTL'],'k--',color='r',label='Station2 75pct')
    ax.legend(loc='best')

def solution4_2():
    print('We create the houston_colors array with: houston_colors = [\'orangered\' if day  ==  330 else \'lightgray\' for day in houston_pollution[\'day\'])]')
    print('We create our plot with: sns.regplot(x = \'NO2\', y = \'SO2\', data = houston_pollution, fit_reg = False, scatter_kws = {\'facecolors\': houston_colors, \'alpha\': 0.7})')
    pollution = pd.read_csv('data/pollution_wide.csv')
    houston_pollution = pollution[pollution.city  ==  'Houston']

    houston_colors = ['orangered' if (day  ==  330) else 'lightgray' 
                      for day in (houston_pollution['day'])]
    print('The final visualization looks like:', ) 
    sns.regplot(x = 'NO2',
                y = 'SO2',
                data = houston_pollution,
                fit_reg = False, 
                # Send scatterplot argument to color points
                scatter_kws = {'facecolors': houston_colors, 'alpha': 0.7})  

def solution4_3():
    print('We find the max value with: max_03 = houston_pollution[\'03\'].max()')
    print('We make a new column with: houston_pollution[\'point_type\'] = [\'Highest 03 Day\' if 03 == max_03 else \'Others\' for 03 in houston_pollution[\'03\']]')
    print('Print the visualization with: sns.scatterplot(x=\'N02\', y=\'S02\', hue=\'point_type\', data=houston_pollution')
    pollution = pd.read_csv('data/pollution_wide.csv')    
    houston_pollution = pollution[pollution.city  ==  'Houston'].copy()

    # Find the highest observed O3 value
    max_O3 = houston_pollution.O3.max()

    # Make a column that denotes which day had highest O3
    houston_pollution['point_type'] = ['Highest O3 Day' if O3  ==  max_O3 else 'Others' for O3 in houston_pollution.O3]

    
    # Encode the hue of the points with the O3 generated column
    print('The final visualization looks like:')
    
    sns.scatterplot(x = 'NO2',
                    y = 'SO2',
                    hue = 'point_type',
                    data = houston_pollution)    

def solution4_4():
    print('The code is again too lengthy to present here. Instead, I am providing a few snippets of code that will prove helpful.')
    print('Remember to examine the problems from the end of our notes.')
    print('Consider using a groupby with more than one level, ie. groupby([\'var1\', \'var2\']).')
    print('Utilize the for loop from our notes combined with np.where and a conditional test to examine values relative to the median.')
          
    house = pd.read_csv('data/train.csv')
    numeric_features = house.select_dtypes(include=[np.number])

    house['YrSold'] = np.where(house['YrSold'] > 2008, 1, 0)
    house.groupby(['YrSold','Neighborhood'])['SalePrice'].mean().plot.bar()
    plt.title('Sale Price by Year/Neighborhood')
    plt.show()

    house['1stFlrSF'] = np.where(house['1stFlrSF'] > house['1stFlrSF'].median(), 1, 0)
    house.groupby('1stFlrSF')['SalePrice'].mean().plot.bar()
    plt.title('Sale Price by 1st Floor Size')
    plt.show()

    for feature in numeric_features:
        dataset = numeric_features.copy()
        dataset[feature] = np.where(dataset[feature] > dataset[feature].median() ,1,0)
        dataset.groupby(feature)['SalePrice'].mean().plot.bar()
        plt.title(feature)
        plt.show()
        
def solution5_1():
    print('We see the average price with: display(stocks_df[\'SPY\'].mean())')
    print('We see the standard deviations sorted with: display(stocks_df.std().sort_values())')
    print('We see the maximum price of AMZN with: display(stocks_df[\'AMZN\'].max())')
    
def solution5_2():
    print('Using the show_plot and normalize functions created above, we can graph the normalized data with:')
    print('show_plot(normalize(stocks_df), \'RAW STOCK PRICES (WITH NORMALIZATION)\')')   
    
def solution5_3():
    print('Using the interactive_plot and normalize functions created above, we can graph the normalized data with:')
    print('interactive_plot(normalize(stocks_df), \'Normalized Prices\')')
    
def solution5_4():
    print('We can calculate the returns for AMZN with the below code. Do not forget to indent where appropriate.')
    print('df = stocks_df[\'AMZN\']')
    print('df_daily_return = df.copy()')
    print('for j in range(1, len(df)):')
    print('    df_daily_return[j] = ((df[j]- df[j-1])/df[j-1]) * 100')
    print('df_daily_return[0] = 0')
    print('df_daily_return')    
    
def solution5_5():
    print('We can show both sets of plots with the below code:')
    print('show_plot(stocks_daily_return, \'STOCKS DAILY RETURNS\'')
    print('interactive_plot(stocks_daily_return, \'STOCK DAILY RETURNS INTERACTIVE\'')
    print('We can utilize the zooming feature of the interactive plot to find the largest daily return.')
       
def solution5_6():
    print('There is no code for this problem, it is just an interpretation of the above correlation matrix.') 
    
def solution5_7():
    print('There is no code for this problem, it is just an interpretation of the above set of histrograms.')
    
def solution5_8():
    print('We can graph all of our stocks with the below function. Do not forget to indent where appropriate')
    print('def all_reg_plots(df):')
    print('    for i in df.columns[1:]:')
    print('        ax = sns.regplot(x=\'SPY\', y=i, data=df)')
    print('        plt.show()')
    print('all_reg_plots(stocks_daily_return)')
    
def solution5_9():
    print('We can calculate expected return for all stocks with the below function. Do not forget to indent where appropriate')
    print('def all_capm_er(df, rf=0):')
    print('    for i in df.columns:')
    print('        if i != \'Date\' and i != \'SPY\':')
    print('        b, a = np.polyfit(df[\'SPY\'], df[i], 1)')
    print('        beta[i] = b')
    print('        alpha[i] = a')
    print('        rm = df[\'SPY\'].mean() * 252')
    print('        ER_i = rf + (beta[i] * (rm - rf))')
    print('        print(i + \' has an expected return of\', ER_i,\'%\')')
    print('all_capm_er(stocks_daily_return)')

def solution5_10():
    print('We can update the set of weights for this problem.')
    print('Repeat the next step for AAPL, AMZN, and GOOG.')
    print('weight_dictionary[\'AAPL\'] = .5')
    print('We can calculate the portfolio return with:')
    print('ER_P2 = sum(ER[k]*weight_dictionary[k] for k in ER)')
    
#########################
####### SOLUTION ########
#########################    
#########################
####### SOLUTION ########
#########################

