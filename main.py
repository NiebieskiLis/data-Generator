import numpy as np

print("Ola to geniusz")

x=3
y=4

print("x = " +str(x)+ " a  y = "+str(y))

print("x + y = "+ str(x+y))

#Dictionary
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

# Update capital of germany

europe['germany'] = 'berlin'
# Remove australia

del(europe['australia'])

# Print europe
print(europe)

#how to put csv
# bricks = pd.read_csv("path")

# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict

my_dict = {'country' : names , 'drives_right' : dr , 'cars_per_cap' : cpc}

# Build a DataFrame cars from my_dict: cars

cars = pd.DataFrame(my_dict)

# Print cars
print (cars)