# def safe_sum(x, y):
#     try:
#         return(x+y)
#     except TypeError:
#         print(f"Can't sum {x} and {y}")
#         print(0)
#
# safe_sum(1, 2)
# safe_sum(5, 'a')

# proverb = 'Программисты - это устройства, преобразующие кофеин в код.'
# new_proverb = ''
# k = 1 # для нечетных
# i = 0 # для четных
# while i < len(proverb) or k < len(proverb):
#     i += 1
#     k += 1
#     if i %2 != 0 and k %2 == 0:
#         new_proverb += (proverb[k-1] + proverb[i-1])
# print(new_proverb, end = '')

# from pprint import pprint
# import csv
#
# reading = []
#
# with open('StudentsPerformance.csv', 'r') as data:
#     for line in data:
#         info = line.split(',')
#         if info[0] == '"gender"':
#             continue
#         else:
#             mark = int(info[6][1:-1])
#             reading.append(mark)
#
# reading_avg = sum(reading)/len(reading)
# print(reading_avg)
#
# above_avg = 0
# for mark in reading:
#     if mark < reading_avg:
#         above_avg += 1
# print(above_avg)
#
# reading_girls =[]
# with open('StudentsPerformance.csv', 'r') as data:
#     for line in data:
#         info = line.split(',')
#         if info[0] == '"gender"':
#             continue
#         else:
#             if info[0] == '"female"':
#                 mark = int(info[6][1:-1])
#                 reading_girls.append(mark)
#
# reading_girls_avg = sum(reading_girls)/len(reading_girls)
# print(reading_girls_avg)
#
# writing_count = 0
# writing =[]
# with open('StudentsPerformance.csv', 'r') as data:
#     for line in data:
#         info = line.split(',')
#         if info[0] == '"gender"':
#             continue
#         else:
#             mark = int(info[7][1:-2])
#             writing.append(mark)
# for mark in writing:
#     if mark > 90:
#         writing_count += 1
# print(writing_count)
#
# writing_count_lunch = 0
# writing_lunch =[]
# with open('StudentsPerformance.csv', 'r') as data:
#     for line in data:
#         info = line.split(',')
#         if info[0] == '"gender"':
#             continue
#         else:
#             if info[3] == '"standard"':
#                 mark = int(info[7][1:-2])
#                 writing_lunch.append(mark)
# for mark in writing_lunch:
#     if mark > 90:
#         writing_count_lunch += 1
# print(writing_count_lunch/writing_count*100)


# students = {}
#
# f = open('StudentsPerformance.csv')
#
# for line in f:
#     info = line.split(',')
#     if info[0] == '"gender"':
#         continue
#     else:
#         ethnicity = info[1][1:-1]
#         if ethnicity in students:
#             students[ethnicity] += 1
#         else:
#             students[ethnicity] = 1
# print(students['group A'])
#
# f2 = open('StudentsPerformance.csv')
# rating_a_math = []
# rating_a_reading = []
# rating_a_writing = []
# rating_b_math = []
# rating_b_reading = []
# rating_b_writing = []
# rating_c_math = []
# rating_c_reading = []
# rating_c_writing = []
# rating_d_math = []
# rating_d_reading = []
# rating_d_writing = []
# rating_e_math = []
# rating_e_reading = []
# rating_e_writing = []
# for line2 in f2:
#     info2= line2.split(',')
#     if info2[0] == '"gender"':
#         continue
#     if info2[1] == '"group A"':
#         mark1 = int(info2[5][1:-1])
#         mark2 = int(info2[6][1:-1])
#         mark3 = int(info2[7][1:-2])
#         rating_a_math.append(mark1)
#         rating_a_reading.append(mark2)
#         rating_a_writing.append(mark3)
#     if info2[1] == '"group B"':
#         mark1 = int(info2[5][1:-1])
#         mark2 = int(info2[6][1:-1])
#         mark3 = int(info2[7][1:-2])
#         rating_b_math.append(mark1)
#         rating_b_reading.append(mark2)
#         rating_b_writing.append(mark3)
#     if info2[1] == '"group C"':
#         mark1 = int(info2[5][1:-1])
#         mark2 = int(info2[6][1:-1])
#         mark3 = int(info2[7][1:-2])
#         rating_c_math.append(mark1)
#         rating_c_reading.append(mark2)
#         rating_c_writing.append(mark3)
#     if info2[1] == '"group D"':
#         mark1 = int(info2[5][1:-1])
#         mark2 = int(info2[6][1:-1])
#         mark3 = int(info2[7][1:-2])
#         rating_d_math.append(mark1)
#         rating_d_reading.append(mark2)
#         rating_d_writing.append(mark3)
#     if info2[1] == '"group E"':
#         mark1 = int(info2[5][1:-1])
#         mark2 = int(info2[6][1:-1])
#         mark3 = int(info2[7][1:-2])
#         rating_e_math.append(mark1)
#         rating_e_reading.append(mark2)
#         rating_e_writing.append(mark3)
#
# math_avg_a = sum(rating_a_math)/len(rating_a_math)
# reading_avg_a = sum(rating_a_reading)/len(rating_a_reading)
# writing_avg_a = sum(rating_a_writing)/len(rating_a_writing)
# total_a = (math_avg_a + reading_avg_a + writing_avg_a)/3
#
# math_avg_b = sum(rating_b_math)/len(rating_b_math)
# reading_avg_b = sum(rating_b_reading)/len(rating_b_reading)
# writing_avg_b = sum(rating_b_writing)/len(rating_b_writing)
# total_b = (math_avg_b + reading_avg_b + writing_avg_b)/3
#
# math_avg_c = sum(rating_c_math)/len(rating_c_math)
# reading_avg_c = sum(rating_c_reading)/len(rating_c_reading)
# writing_avg_c = sum(rating_c_writing)/len(rating_c_writing)
# total_c = (math_avg_c + reading_avg_c + writing_avg_c)/3
#
# math_avg_d = sum(rating_d_math)/len(rating_d_math)
# reading_avg_d = sum(rating_d_reading)/len(rating_d_reading)
# writing_avg_d = sum(rating_d_writing)/len(rating_d_writing)
# total_d = (math_avg_d + reading_avg_d + writing_avg_d)/3
#
# math_avg_e = sum(rating_e_math)/len(rating_e_math)
# reading_avg_e = sum(rating_e_reading)/len(rating_e_reading)
# writing_avg_e = sum(rating_e_writing)/len(rating_e_writing)
# total_e = (math_avg_e + reading_avg_e + writing_avg_e)/3
#
# for group, number in students.items():
#     if group == 'group A':
#         print(f'{group}: Count - {number}, Math - {math_avg_a:.2f}, Reading - {reading_avg_a:.2f}, Writing - {writing_avg_a:.2f}, Total - {total_a:.2f}')
#     if group == 'group B':
#         print(f'{group}: Count - {number}, Math - {math_avg_b:.2f}, Reading - {reading_avg_b:.2f}, Writing - {writing_avg_b:.2f}, Total - {total_b:.2f}')
#     if group == 'group C':
#         print(f'{group}: Count - {number}, Math - {math_avg_c:.2f}, Reading - {reading_avg_c:.2f}, Writing - {writing_avg_c:.2f}, Total - {total_c:.2f}')
#     if group == 'group D':
#         print(f'{group}: Count - {number}, Math - {math_avg_d:.2f}, Reading - {reading_avg_d:.2f}, Writing - {writing_avg_d:.2f}, Total - {total_d:.2f}')
#     if group == 'group E':
#         print(f'{group}: Count - {number}, Math - {math_avg_e:.2f}, Reading - {reading_avg_e:.2f}, Writing - {writing_avg_e:.2f}, Total - {total_e:.2f}')

# f = open('StudentsPerformance.csv')
# boys = 0
# for line in f:
#     info = line.split(',')
#     if info[0] == '"gender"':
#         continue
#     if info[0] == '"male"':
#         if info[3] == '"standard"':
#             boys += 1
# print(boys)

# f = open('StudentsPerformance.csv')
# boys = 0
# for line in f:
#     info = line.split(',')
#     if info[0] == '"gender"':
#         continue
#     if info[0] == '"male"':
#         if info[4] == '"completed"':
#             boys += 1
# print(boys)

# with open('StudentsPerformance.csv') as f:
#     girls = 0
#     for line in f:
#         info = line.split(',')
#         if info[0] == '"gender"':
#             continue
#         if info[0] == '"female"':
#             if info[2] == '"master\'s degree"':
#                 girls += 1
#     print(girls)

# with open('StudentsPerformance.csv') as f:
#     group_c = 0
#     for line in f:
#         info = line.split(',')
#         if info[0] == '"gender"':
#             continue
#         if info[1] == '"group C"':
#             if info[4] == '"completed"':
#                 group_c += 1
#     print(group_c)

# with open('StudentsPerformance.csv') as f:
#     girls = 0
#     for line in f:
#         info = line.split(',')
#         if info[0] == '"gender"':
#             continue
#         if info[0] == '"female"':
#             if info[2] == '"master\'s degree"' and int(info[5][1:-1]) > 90:
#                 girls += 1
#     print(girls)

# with open('StudentsPerformance.csv') as f:
#     boys = []
#     for line in f:
#         info = line.split(',')
#         if info[0] == '"gender"':
#             continue
#         if info[0] == '"male"':
#             boys.append(int(info[6][1:-1]))
#     print(sum(boys)/len(boys))

# with open('StudentsPerformance.csv') as f:
#     read = []
#     for line in f:
#         info = line.split(',')
#         if info[0] == '"gender"':
#             continue
#         if info[5][1:-1] == '100':
#             read.append(int(info[6][1:-1]))
#     print(sum(read)/len(read))

# with open('StudentsPerformance.csv') as f:
#     writing = []
#     for line in f:
#         info = line.split(',')
#         if info[0] == '"gender"':
#             continue
#         if info[3] == '"free/reduced"':
#             writing.append(int(info[7][1:-2]))
#     print(sum(writing)/len(writing))

# import datetime
#
# now = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
# print(now)

# import time
# time_tuple = (2018, 12, 31, 0, 0, 0, 0, 0, 0)
# timestamp = time.mktime(time_tuple)
# print(timestamp)

# import time
# time_tuple = (2019, 1, 1, 0, 0, 0, 0, 0, 0)
# timestamp = time.mktime(time_tuple)
# print(timestamp)

# import time
# time_tuple = (2019, 1, 1, 0, 0, 0, 0, 0, 0)
# time_tuple2 = (2019, 1, 31, 0, 0, 0, 0, 0, 0)
# timestamp = time.mktime(time_tuple2) - time.mktime(time_tuple)
# print(timestamp)

# from datetime import datetime
# date_string = '2019-07-07T18:59:33'
# df = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S')
# # date_format = f"{df.day}.{df.month}.{df.year}"
# date_format = df.strftime("%d.%m.%Y")
# print(date_format)

# from datetime import datetime
# datetime_list = []
# dt_list = ['2019-07-07T18:59:06', '2019-07-07T19:00:02', '2019-07-07T19:01:04']
# for dt in dt_list:
#     elem = datetime.strptime(dt, '%Y-%m-%dT%H:%M:%S')
#     datetime_list.append(elem)
# print(datetime_list)

# from datetime import datetime
#
# report_seconds = []
# datetime_list = [
#     datetime(2019, 7, 7, 18, 59, 6),
#     datetime(2019, 7, 7, 19, 0, 2),
#     datetime(2019, 7, 7, 19, 1, 4)
# ]
# for dts in datetime_list:
#     report_seconds.append(dts.second)
#
# print(report_seconds)

# from datetime import datetime
# report_seconds = [6, 2, 4]
#
# total_time = sum(report_seconds)
# print(total_time)

# numbers = [1, 3, 5, 7]
# def get_median(numbers):
#     nums = sorted(numbers)
#     if len(nums)%2 != 0:
#         result = nums[int(len(numbers)/2)]
#     else:
#         result = (nums[int(len(nums)/2-1)] + nums[int(len(nums)/2)])/2
#     return result
# print(get_median(numbers))

# user_db = [{'orders': 12}, {'orders': 30}, {'orders': 45}]
#
# # перепишите эту часть
# def avg_orders(user_db):
#     order_sum = sum([user['orders'] for user in user_db])
#     orders_per_user = order_sum/len(user_db)
#     print(orders_per_user)
# avg_orders(user_db)

from random import randint
# добавьте функцию get_euro_rate
def get_euro_rate():
    result = randint(65, 85)
    return result

# используйте get_euro_rate в следующей функции
def to_euro(price):
    exchange_rate = get_euro_rate()
    rounded = round(price/exchange_rate, 2)
    return '€' + str(rounded)
print(to_euro(100))