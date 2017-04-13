import csv
import sys
import math
import random
from random import shuffle
import numpy as np
random.seed(0)

if(len(sys.argv)!=2):
    print "greedy msvv balance" 
    sys.exit(0) 
algo = sys.argv[1]

def greedy(queries,budget,bidder_data):

    revenue = 0.0

    for advertisement in queries:
        greedy_list = []
        temp_list = []
        for line in bidder_data:
            if(line[1]==advertisement and budget[line[0]]>=float(line[2])):
                temp_list.append(line)

        max_list = []

        max_value = -1.0
        for single_row in temp_list:
            if(max_value<float(single_row[2])):
                max_value = float(single_row[2])
                max_list = single_row

        if len(max_list)>0:
            revenue += float(max_list[2])
            budget[max_list[0]] -= float(max_list[2])

    return revenue

def MSVV(queries,budget,bidder_data):

    revenue = 0.0

    for advertisement in queries:
        temp_list = []
        for line in bidder_data:
            if(line[1]==advertisement and budget[line[0]]>=float(line[2])):
                temp_list.append(line)

        max_list = []

        max_value = -1.0
        for single_row in temp_list:
            temp = 1 - math.exp((copyBudget[single_row[0]]-budget[single_row[0]])/copyBudget[single_row[0]]-1)
            if (float(single_row[2])*temp>max_value):
                max_value = float(single_row[2])*temp
                max_list = single_row
        #print revenue
        if len(max_list)>0:
            max_value = float(max_list[2])
            revenue += max_value
            budget[max_list[0]] -= max_value

    return revenue

    
def Balance(queries,budget,bidder_data):

    revenue = 0.0

    for advertisement in queries:
        greedy_list = []
        temp_list = []
        for line in bidder_data:
            if(line[1]==advertisement and budget[line[0]]>=float(line[2])):
                temp_list.append(line)

        max_list = []

        max_value = -1.0
        for single_row in temp_list:
            if(max_value<float(budget[single_row[0]])):
                max_value = float(budget[single_row[0]])
                max_list = single_row
        #print revenue
        if len(max_list)>0:
            revenue += float(max_list[2])
            budget[max_list[0]] -= float(max_list[2])

    return revenue



budget = {}
queries = []
bidder_data = []
temp = []

revenue_list = []

f = open("bidder_dataset.csv", 'rb')
read = csv.reader(f)
next(read, None)

for row in read:
    if(row[3]!=""):
        budget[(row[0])] = float(row[3])
    for word in row:
        temp.append(word)
    bidder_data.append(temp)
    temp = []

copyBudget = budget.copy()


f = open("queries.txt","r")
for line in f:
    queries.append(line.strip('\n'))

total_revenue = sum(budget.values())

# print budget
# sys.exit(0)
#greedy(queries,budget,bidder_data)

if algo == "greedy":
    print "revenue:",greedy(queries,budget,bidder_data)
elif algo == "msvv":
    print "revenue:",MSVV(queries,budget,bidder_data)
elif algo == "balance":
    print "revenue:",Balance(queries,budget,bidder_data)

#count = 0;
for i in range(100):
    #print count
    budget = copyBudget.copy()
    shuffle(queries)
    if algo == "greedy":
        revenue_list.append(greedy(queries,budget,bidder_data))
    elif algo == "msvv":
        revenue_list.append(MSVV(queries,budget,bidder_data))
    elif algo == "balance":
        revenue_list.append(Balance(queries,budget,bidder_data))
    #count +=1
print "competitive ratio:",np.mean(revenue_list)/total_revenue
"""
count = 0;
for i in range(100):
    print count
    budget = copyBudget.copy()
    shuffle(queries)
    revenue_list.append(MSVV(queries,budget,bidder_data))
    count +=1
print "competitive ratio",np.mean(revenue_list)/total_revenue

count = 0;
for i in range(100):
    print count
    budget = copyBudget.copy()
    shuffle(queries)
    revenue_list.append(Balance(queries,budget,bidder_data))
    count +=1
print "competitive ratio",np.mean(revenue_list)/total_revenue
"""



  
#greedy(queries,budget,bidder_data) 
#MSVV(queries,budget,bidder_data)
#Balance(queries,budget,bidder_data)  


