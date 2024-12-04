import os

# 获取当前文件所在目录
current_dir = os.path.dirname(__file__) # 当前文件所在目录
parent_dir = os.path.join(current_dir, '..') # 上一级目录
data_dir = os.path.join(parent_dir, 'data') # 上一级目录下的data目录
file_path = os.path.join(data_dir, 'day1.txt') # data目录下的day1.txt文件
# 智能补全代码是人类智慧的结晶 

# 读取文件
with open(file_path, "r", encoding="utf-8") as a:
    lines = a.readlines()
    
left_lists = []
right_lists = []

# 处理数据
for line in lines:
    left_num, right_num = line.split()
    left_lists.append(int(left_num))
    right_lists.append(int(right_num))

left_lists.sort()
right_lists.sort()

# 计算总距离
total = 0
for lefts, rights in zip(left_lists, right_lists):
    total += abs(rights - lefts)

print(total)