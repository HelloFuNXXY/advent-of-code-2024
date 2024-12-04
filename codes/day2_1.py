import os

current_dir = os.path.dirname(__file__) 
parent_dir = os.path.join(current_dir, '..') 
data_dir = os.path.join(parent_dir, 'data') 
file_path = os.path.join(data_dir, 'day2.txt') 

def is_safe(report):
    # 将报告字符串转换为整数列表
    levels = list(map(int, report.split()))
    
    # 检查所有级别是否都是递增或递减
    increasing = all(x < y for x, y in zip(levels, levels[1:]))
    decreasing = all(x > y for x, y in zip(levels, levels[1:]))
    
    # 如果既不是递增也不是递减，则返回False
    if not (increasing or decreasing):
        return False
    
    # 检查任何两个相邻级别之间的差异是否在1到3之间
    for i in range(len(levels) - 1):
        if not (1 <= abs(levels[i] - levels[i + 1]) <= 3):
            return False
    
    return True

def count_safe_reports(filename):
    safe_count = 0
    # 打开文件并逐行读取
    with open(filename, 'r') as file:
        for report in file:
            if is_safe(report.strip()):
                safe_count += 1
    return safe_count

# 示例文件名
filename = file_path

# 计算并打印安全报告的数量
print("Number of safe reports:", count_safe_reports(filename))
