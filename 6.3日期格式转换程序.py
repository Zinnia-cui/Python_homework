# 1. 定义月份的英文名字符串列表
monthList = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
# 2. 输入日期，并将其转换为月份的英文名字符串
dateStr=(input("Enter a date (mm/dd/yyyy):"))
# 3. 利用斜杠分离日期信息
month, day, year = dateStr.split('/')
# 4. 将月份字符串转换为月份数字（注意将其转为整数以便索引）
month_num = int(month)
# 5. 查找对应的月份名称
month_name = monthList[month_num - 1]  # 列表索引从0开始，所以要减1
# 6. 创建新的日期字符串，格式为“月份，日期，年份”
new_date_str = f"{month_name} {int(day)},{year}"
print(f"The converted date is:{new_date_str}")


