import csv
import math
import statistics as st

'''Calculate the mean of your data set.

Subtract the mean from each of the data values and list the differences.

Square each of the differences from the previous step and make a list of the squares.

Add the squares from the previous step together.

Subtract one from the number of data values you started with.

Divide the sum from step four by the number from step five.

Take the square root of the number from the previous step. This is the standard deviation.'''

def standard_deviation(file):

    with open(file) as f:
        reader=csv.reader(f)
        file_data=list(reader)

    new_data=[]
    
    for i in range(len(file_data)):
        n_num=file_data[i][0]
        new_data.append(float(n_num))

    #sd=st.stdev(new_data)
    #print(sd)

    sum=0
    for i in range(0,len(new_data)):
        sum=sum+new_data[i]

    mean=sum/len(new_data)
    #print(mean)

    diff_list=[]
    for i in range(len(new_data)):
        difference=(new_data[i])-mean
        diff_list.append(difference)

    #print(diff_list)

    square_list=[]
    for i in range(len(diff_list)):
        square=(diff_list[i])*(diff_list[i])
        square_list.append(square)

    #print(square_list)

    square_sum=0
    for i in range(len(square_list)):
        square_sum=square_sum+square_list[i]

    #print(square_sum)

    n_num=len(new_data)-1
    #print(n_num)

    division=square_sum/n_num
    #print(division)

    standard_deviation=math.sqrt(division)
    print(standard_deviation)


file=str(input("Enter the file name: "))

standard_deviation(file)
