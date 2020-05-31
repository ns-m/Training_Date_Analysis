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


students = {}

f = open('StudentsPerformance.csv')

for line in f:
    info = line.split(',')
    if info[0] == '"gender"':
        continue
    else:
        ethnicity = info[1][1:-1]
        if ethnicity in students:
            students[ethnicity] += 1
        else:
            students[ethnicity] = 1
print(students['group A'])

f2 = open('StudentsPerformance.csv')
rating_a_math = []
rating_a_reading = []
rating_a_writing = []
rating_b_math = []
rating_b_reading = []
rating_b_writing = []
rating_c_math = []
rating_c_reading = []
rating_c_writing = []
rating_d_math = []
rating_d_reading = []
rating_d_writing = []
rating_e_math = []
rating_e_reading = []
rating_e_writing = []
for line2 in f2:
    info2= line2.split(',')
    if info2[0] == '"gender"':
        continue
    if info2[1] == '"group A"':
        mark1 = int(info2[5][1:-1])
        mark2 = int(info2[6][1:-1])
        mark3 = int(info2[7][1:-2])
        rating_a_math.append(mark1)
        rating_a_reading.append(mark2)
        rating_a_writing.append(mark3)
    if info2[1] == '"group B"':
        mark1 = int(info2[5][1:-1])
        mark2 = int(info2[6][1:-1])
        mark3 = int(info2[7][1:-2])
        rating_b_math.append(mark1)
        rating_b_reading.append(mark2)
        rating_b_writing.append(mark3)
    if info2[1] == '"group C"':
        mark1 = int(info2[5][1:-1])
        mark2 = int(info2[6][1:-1])
        mark3 = int(info2[7][1:-2])
        rating_c_math.append(mark1)
        rating_c_reading.append(mark2)
        rating_c_writing.append(mark3)
    if info2[1] == '"group D"':
        mark1 = int(info2[5][1:-1])
        mark2 = int(info2[6][1:-1])
        mark3 = int(info2[7][1:-2])
        rating_d_math.append(mark1)
        rating_d_reading.append(mark2)
        rating_d_writing.append(mark3)
    if info2[1] == '"group E"':
        mark1 = int(info2[5][1:-1])
        mark2 = int(info2[6][1:-1])
        mark3 = int(info2[7][1:-2])
        rating_e_math.append(mark1)
        rating_e_reading.append(mark2)
        rating_e_writing.append(mark3)

math_avg_a = sum(rating_a_math)/len(rating_a_math)
reading_avg_a = sum(rating_a_reading)/len(rating_a_reading)
writing_avg_a = sum(rating_a_writing)/len(rating_a_writing)
total_a = (math_avg_a + reading_avg_a + writing_avg_a)/3

math_avg_b = sum(rating_b_math)/len(rating_b_math)
reading_avg_b = sum(rating_b_reading)/len(rating_b_reading)
writing_avg_b = sum(rating_b_writing)/len(rating_b_writing)
total_b = (math_avg_b + reading_avg_b + writing_avg_b)/3

math_avg_c = sum(rating_c_math)/len(rating_c_math)
reading_avg_c = sum(rating_c_reading)/len(rating_c_reading)
writing_avg_c = sum(rating_c_writing)/len(rating_c_writing)
total_c = (math_avg_c + reading_avg_c + writing_avg_c)/3

math_avg_d = sum(rating_d_math)/len(rating_d_math)
reading_avg_d = sum(rating_d_reading)/len(rating_d_reading)
writing_avg_d = sum(rating_d_writing)/len(rating_d_writing)
total_d = (math_avg_d + reading_avg_d + writing_avg_d)/3

math_avg_e = sum(rating_e_math)/len(rating_e_math)
reading_avg_e = sum(rating_e_reading)/len(rating_e_reading)
writing_avg_e = sum(rating_e_writing)/len(rating_e_writing)
total_e = (math_avg_e + reading_avg_e + writing_avg_e)/3

for group, number in students.items():
    if group == 'group A':
        print(f'{group}: Count - {number}, Math - {math_avg_a:.2f}, Reading - {reading_avg_a:.2f}, Writing - {writing_avg_a:.2f}, Total - {total_a:.2f}')
    if group == 'group B':
        print(f'{group}: Count - {number}, Math - {math_avg_b:.2f}, Reading - {reading_avg_b:.2f}, Writing - {writing_avg_b:.2f}, Total - {total_b:.2f}')
    if group == 'group C':
        print(f'{group}: Count - {number}, Math - {math_avg_c:.2f}, Reading - {reading_avg_c:.2f}, Writing - {writing_avg_c:.2f}, Total - {total_c:.2f}')
    if group == 'group D':
        print(f'{group}: Count - {number}, Math - {math_avg_d:.2f}, Reading - {reading_avg_d:.2f}, Writing - {writing_avg_d:.2f}, Total - {total_d:.2f}')
    if group == 'group E':
        print(f'{group}: Count - {number}, Math - {math_avg_e:.2f}, Reading - {reading_avg_e:.2f}, Writing - {writing_avg_e:.2f}, Total - {total_e:.2f}')