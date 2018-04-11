
#from __future__ import division
import matplotlib.pyplot as plt
import numpy as np


def outlierDetection(Q1,Q3,list_of_numbers):
    #this function takes a list of numbers and prints out those numbers that are considered outliers
    IQR= float(Q3-Q1)
    print ("IQR= ",IQR)
    lowerthreshold=Q1-(IQR*1.5)
    print ("Lowerthreshold= ",lowerthreshold)
    upperthreshold=Q3+(IQR*1.5)
    print ("Upperthreshold= ",upperthreshold)
    for i in list_of_numbers:
        lowflag=0
        highflag=0
        if (i <lowerthreshold):
            lowflag=1
        if (i>upperthreshold):
            highflag=1
        if (lowflag):
            print (i , "is an outlier because it is lower than than the lowerthreshold")
        if (highflag):
            print (i , "is an outlier because it is higher than than the upperthreshold")

# different lists
list_of_numbers=[53,79,80,82,87,91,93,98]
#list_of_numbers=[53,79,80,82,87,91,93,98,57,79,99,66]
#list_of_numbers=[1,1,4,4,9,11]

#the numbers need to be sorted first
list_of_numbers.sort()
print ("The observations after sorting: ", list_of_numbers,'\n')


# printing the number of observations
print  ("Number of observations =  ",len(list_of_numbers),'\n')



# getting the minimum number of the list
Min=list_of_numbers[0]

#getting the maximum number of the list
Max=list_of_numbers[-1]


# getting the Q2 of the list
median = np.median(list_of_numbers)
# getting the Q3 of the list
upper_quartile = np.percentile(list_of_numbers, 75)
# getting the Q1 of the list
lower_quartile = np.percentile(list_of_numbers, 25)

# printing the five number summary
print ("Five Number Summary ",Min, lower_quartile, median, upper_quartile, Max,'\n')

# getting the outliers
outlierDetection(lower_quartile, upper_quartile,list_of_numbers)

# plotting the BOXPLOT verticaly with outliers as  diamond shape
plt.figure()
#plt.boxplot(list_of_numbers, 0, 'gD',0.50)
# plotting the BOXPLOT horizontal
plt.boxplot(list_of_numbers, 0, 'rs',0)
'''
# plotting the BOXPLOT with an outliers as a +
plt.boxplot(list_of_numbers)
# don't show outlier points
plt.figure()
plt.boxplot(list_of_numbers, 0, '')

# horizontal boxes
plt.figure()
plt.boxplot(list_of_numbers, 0, 'rs', 0)
'''


plt.show()
