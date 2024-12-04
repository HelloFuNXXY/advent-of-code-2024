import os
from collections import Counter

current_dir = os.path.dirname(__file__) 
parent_dir = os.path.join(current_dir, '..') 
data_dir = os.path.join(parent_dir, 'data') 
file_path = os.path.join(data_dir, 'day1.txt') 

with open(file_path, "r", encoding="utf-8") as a:
    lines = a.readlines()
    
left_lists = []
right_lists = []

for line in lines:
    left_num, right_num = line.split()
    left_lists.append(int(left_num))
    right_lists.append(int(right_num))

count = dict(Counter(right_lists))
total = 0

for lefts in left_lists:
    if lefts in count:
        total += lefts * count[lefts]

print(total)
