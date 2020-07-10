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


# def get_median(numbers):
#     nums = sorted(numbers)
#     if len(nums)%2 != 0:
#         result = nums[int(len(numbers)/2)]
#     else:
#         result = (nums[int(len(nums)/2-1)] + nums[int(len(nums)/2)])/2
#     return result
#
# print(get_median([3, 3, 4, 4]))

# user_db = [{'orders': 12}, {'orders': 30}, {'orders': 45}]
#
# # перепишите эту часть
# order_sum = sum([user['orders'] for user in user_db])
# orders_per_user = order_sum/len(user_db)
# print(orders_per_user)

# values = [1, 2, 3]
# vectors = [(10, 3), (4, 5), (6, 7)]
# a1 = list(map(lambda x: x+2, [1, 2, 3]))
# # a2 = map(values, lambda x: x**0.5)
# a3 = list(map(lambda vec: (vec[0]**2 + vec[1]**2)**0.5, vectors))
# # a4 = list(map(lambda x, y: x + y, values))
#
# print(a3)

# values = [4, 8, 15, 16, 23, 42]
# mean = 18
#
# result = map(lambda x: x - mean, values)
# print(list(result))

# def normalize(numbers, mean=0, std=1):
#     result = [int((x - mean)/std) for x in numbers]
#     return result
# print(normalize([10, 20], mean=15))

# def sum_args(*args):
#     result = sum(args)
#     return result
# print(sum_args(10, 15, -4))

# def count_letters(sentence, average=False):
#     my_list = sentence.split(' ')
#     if average == False:
#         count_list = [len(x) for x in my_list]
#         result = sum(count_list)
#     else:
#         count_list = [len(x)/len(my_list) for x in my_list]
#         result = sum(count_list)
#     return result
#
#
# print(count_letters("I will build my own theme park", average=True))

# words = ["sofa", "suitcase", "valise", "picture", "basket", "carton", "doggie"]
# x = list(map(lambda w: sorted(w)[2], words))[3]
# print(x)

# def always(n):
#     return (lambda :n)
# five = always(5)
# print(five())

import pandas as pd
from IPython.display import display
from pprint import pprint
pd.set_option('display.max_columns', 40)
pd.set_option('display.width', 2000)
#
# data = pd.Series(["Январь", "Февраль", "Март", "Апрель"],
#                  index = ['Первый', "Второй", "Третий", "Четвёртый"])
# display(data)
# print('this loc')
# pprint(data.loc[['Первый', "Четвёртый"]])
# print('this out loc')
# pprint(data[['Второй', "Третий"]])
# print('this iloc')
# pprint(data.iloc[[0, 2]])
# print('this out iloc')
# pprint(data[[1, 3]])

# data = pd.Series(list(range(10, 1001)))
# print(data.loc[10] + data.loc[23] - data.loc[245] + data.iloc[122])
# print(data.iloc[990])

# df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
# display(df)

# df = pd.DataFrame([ [1,2,3], [2,3,4] ],
#                   columns = ['foo', 'bar', 'baz'],
#                   index = ['foobar', 'foobaz'])
# display(df)

# football = pd.read_csv('data_sf.csv')

# display(football)
# display(football.head(10))
# display(football.tail(7))
# display(football.info())
# display(football.describe())
# display(football.describe(include = ['object']))
# print('----------------')
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#     display(football.describe())

# df = pd.DataFrame([[i,i+1.2,i+2, 'hi'] for i in range(10)],
#                   columns = ['foo', 'bar', 'baz', 'foobar'])
# display(df)
# print('------')
# display(df.mean())

# df = pd.DataFrame([[i,i+1.2,i+2, 'hi'] for i in range(10)],
#                   columns = ['foo', 'bar', 'baz', 'foobar'])
# display(df['foo'])
# display(df.bar)

# df = pd.DataFrame([[i,i+1.2,i+2, 'hi'] for i in range(10)],
#                   columns = ['foo', 'bar', 'baz', 'foobar'])
# display(df.bar)
# display(df.bar.mean())
# display(df.bar.std())

# df = pd.DataFrame(football)
# display(df.Age.mean())
# display(df.Composure.count())
# display(df.ShortPassing.std())
# display(df.Wage.sum())
# display(df.Value.min())

# display(football[football.Age < 20])
# display(football[football.Age > football.Age.mean()])
# display(football[(football.Age < football.Age.mean())|
#         (football.Club == 'FC Barcelona')])

# display(football[(football.Age < football.Age.mean())&
#         (football.Club == 'FC Barcelona')].Wage.mean())

# display(football[(football.Wage > football.Wage.mean())].SprintSpeed.mean())

# display(football[(football.Wage < football.Wage.mean())].SprintSpeed.mean())

# display(football[(football.Wage == football.Wage.max())].Position)

# display(football[(football.Nationality == 'Brazil')].Penalties.sum())

# display(football[(football.HeadingAccuracy > 50)].Age.mean())

# display(football[(football.Composure > (football.Composure.max() * 0.9)) &
#                  (football.Reactions > (football.Reactions.max() * 0.9))].Age.min())

# display(football[(football.Age == football.Age.max())].Reactions.mean() -
#         football[(football.Age == football.Age.min())].Reactions.mean())

# df = football[(football.Value > football.Value.mean())].Nationality #shit code style
# my_list = {}
# for i in df:
#     if i in my_list:
#         my_list[i]+=1
#     else:
#         my_list[i] = 1
# list_d = list(my_list.items())
# list_d.sort(key=lambda i: i[1])
# for i in list_d:
#     print(i[0], ':', i[1]) #shit code style

# display(football[(football.Value > football.Value.mean())].Nationality.value_counts().index[0])

# display(football[(football.GKReflexes == football.GKReflexes.max())].Wage.mean() /
#         football[(football.GKHandling == football.GKHandling.max())].Wage.mean())

# display(football[(football.Aggression == football.Aggression.max())].ShotPower.mean() /
#         football[(football.Aggression == football.Aggression.min())].ShotPower.mean())

# df = football[(football.Value > football.Value.mean())].Nationality.value_counts()
# print(len(df.index))
# print(df['Spain'])
# print(df.loc[df>1])

# df = football.Club.value_counts()
# print(len(df.index))
# display(df)

# display(football.Position.value_counts(normalize=True)) # в процентах

# display(football['Age'].value_counts())

# display(football['Wage'].value_counts())

# display(football['Wage'].value_counts(bins=4))
# football_sm = football[football.columns[1:8]]
# df = football_sm['Wage'].value_counts(bins=4)
# display(df)
# display(df.index)
# display(df.index[3])
# display(df.index[3].left)
# display(df.index[3].right)
# display(football_sm['Wage']>df.index[3].left)
# display(football_sm.loc[(football_sm['Wage'] > df.index[3].left) & (football_sm['Wage'] <= df.index[3].right)])

# display(football['FKAccuracy'].value_counts(bins=5))

# display(football['Nationality'].unique())
# display(football['Nationality'].nunique())

# display(football['Nationality'].value_counts().reset_index())
# df = football['Nationality'].value_counts().reset_index()
# df.columns = ['Nationality','Players Count']
# display(df)

# display(football[(football.Nationality == 'Spain')]['Wage'].value_counts(normalize=True, bins=4))

# display(football[(football.Club == 'Manchester United')]['Nationality'].nunique())

# display(football[((football.Nationality == 'Brazil') & (football.Club == 'Juventus'))])

# display(football[((football.Age > 35))]['Club'].value_counts())

# display(football[(football.Nationality == 'Argentina')]['Age'].value_counts(bins=4))

# display(football[(football.Nationality == 'Spain')]['Age'].value_counts(normalize=True)[21] * 100)

# display(football.groupby(['Club']).sum())

# display(football.groupby(['Club']).sum().loc['FC Barcelona'])

# display(football.groupby(['Club']).sum().loc['FC Barcelona']['Wage'])

# display(football.groupby(['Club'])['Wage'].sum())

# display(football.groupby(['Club'])['Wage'].sum().sort_values(ascending=False))

# display(football.groupby(['Position'])['Wage'].sum().sort_values(ascending=False))

# display(football.groupby(['Nationality'])[['Wage','Age','ShotPower']].mean().sort_values(['Wage'],ascending=False).head(10))
# display(football.loc[football['Nationality'] == 'Dominican Republic'][['Name','Club','Wage','Age','ShotPower']])

# display(football.groupby(['Position'])[['Wage','Value']].mean().sort_values(['Value'],ascending=False).head(10))

# df = football.groupby(['Club'])['Wage'].agg(['mean', 'median'])
# display(df[(df['mean'] == df['median'])].count())
# display(df[(df['mean'] == df['median'])].max())
# display(df[(df['mean'] == df['median'])].sort_values(['mean'],ascending=False))

# display(football.groupby(['Club'])['Wage'].sum().sort_values(ascending=False)['Chelsea'])

# display(football[(football.Nationality == 'Argentina')].groupby(['Age'])['Wage'].max()[20])
# display(football[(football.Nationality == 'Argentina')].groupby(['Age'])['Wage'].max()[30])

# display(football[(football.Nationality == 'Argentina')].groupby(['Age'])['Wage'].min()[30])

# display(football[(football.Nationality == 'Argentina') & (football.Club == 'FC Barcelona')][['Strength','Balance']].max())

# pivot = football.loc[football['Club'].isin(['FC Barcelona','Real Madrid','Juventus','Manchester United'])].pivot_table(values=['Wage'],
# index=['Nationality'],
# columns=['Club'],
# aggfunc='sum',
# margins=True,
# fill_value=0)
# display(pivot)

# display(football.pivot_table(index=['Club'], columns=['Position'], values = 'Name', aggfunc = 'count',fill_value=0)['GK'].mean())

# display(football.pivot_table(index=['Club'], columns=['Position'], values = 'Name', aggfunc = 'count',fill_value=0)['CM'].value_counts()[0])

# display(football.loc[football['Club'].isin(['AS Monaco'])].pivot_table(index=['Nationality'], columns=['Club'],values='Wage'))

# display(football.pivot_table(index=['Club'], columns=['Position'], values='SprintSpeed', aggfunc='mean', margins=True, fill_value=0).max().sort_values(ascending=False))

# display(football.pivot_table(index=['Club'], columns=['Position'], values='SprintSpeed', aggfunc='mean', margins=True, fill_value=0)['ST'].sort_values(ascending=False))


# movies = pd.read_csv('movies.csv')
# ratings = pd.read_csv('ratings.csv')

# display(ratings.count())
# display(movies.head(1))
# display(ratings['rating'].min())
# display(ratings['rating'].max())

# display(movies.count())

# display(ratings.merge(movies, on='movieId', how='left').head())

# sm_ratings = pd.read_csv('ratings_example.txt', sep = '\t')
# display(sm_ratings.head())

# sm_movies = pd.read_csv('movies_example.txt', sep = '\t')
# display(sm_movies.head())

# display(sm_ratings.merge(sm_movies, how = 'left', on = 'movieId'))

# display(sm_ratings.merge(sm_movies, how = 'outer', on = 'movieId'))

# sm_movies.drop_duplicates(subset = 'movieId', keep = 'first', inplace = True)
# display(sm_movies.head())

# display(sm_ratings.merge(sm_movies, how = 'left', on = 'movieId'))

# items_dict = {
#
#     'item_id': [417283, 849734, 132223, 573943, 19475, 3294095, 382043, 302948, 100132, 312394],
#
#     'vendor': ['Samsung', 'LG', 'Apple', 'Apple', 'LG', 'Apple', 'Samsung', 'Samsung', 'LG', 'ZTE'],
#
#     'stock_count': [54, 33, 122, 18, 102, 43, 77, 143, 60, 19]
#
# }
#
# purchase_log = {
#
#     'purchase_id': [101, 101, 101, 112, 121, 145, 145, 145, 145, 221],
#
#     'item_id': [417283, 849734, 132223, 573943, 19475, 3294095, 382043, 302948, 103845, 100132],
#
#     'price': [13900, 5330, 38200, 49990, 9890, 33000, 67500, 34500, 89900, 11400]
#
# }
#
# items_df = pd.DataFrame(items_dict)
# purchase_df = pd.DataFrame(purchase_log)

# display(items_df.merge(purchase_df, how = 'outer', on = 'item_id'))
# display(purchase_df.merge(items_df, how = 'outer', on = 'item_id'))

# merged = items_df.merge(purchase_df, how = 'inner', on = 'item_id')
# display(merged)
# print(f'Count of models - {len(merged)}')

# merged = items_df.merge(purchase_df, how = 'outer', on = 'item_id')
# merged['sum_sell'] = merged['stock_count'] * merged['price']
# display(merged[(merged['sum_sell'] == merged['sum_sell'].max())]['item_id'])
# merged.loc['ALL_sum'] = merged['sum_sell'].sum()
# display(merged)

import glob, os

# files = os.listdir('data')
# pprint(files)

# files = ['setup.py', 'ratings.txt', 'stock_stats.txt', 'movies.txt', 'run.sh', 'game_of_thrones.mov']
# data = []
# for file in files:
#     if file.endswith(".txt"):
#         data.append(file)
# pprint(data)

# for root, dirs, files in os.walk('data'):
#     print(root, dirs, files)

# files_in_data = []
# for files in os.listdir('data'):
#     if files.endswith(".txt"):
#         files_in_data.append(files)
#
# data = pd.DataFrame(columns = ['userId', 'movieId', 'rating', 'timestamp'])
# temp = pd.DataFrame(columns = ['userId', 'movieId', 'rating', 'timestamp'])
# for fl in files_in_data:
#     temp = pd.read_csv(os.path.join('data', fl), names=['userId', 'movieId', 'rating', 'timestamp'])
#     data = pd.concat([data, temp])
# display(data)

# display(ratings[(ratings['rating'] == ratings['rating'].min())].count())

# display(ratings.merge(movies, how='outer', on='movieId'))

# merged = ratings.merge(movies, how='outer', on='movieId')
# display(merged[(merged['movieId']==3456)])

import matplotlib
from matplotlib import pyplot as plt
plt.interactive(True)

macduck = pd.read_csv('tips.csv')
# display(macduck.count())

# display(macduck['total_bill'].max())

# plt.show(macduck.plot())
# #
# plt.show(macduck['total_bill'].plot(kind = 'hist'))
# #
# plt.show(macduck['total_bill'].plot(kind = 'hist', grid = True, title = 'Общая сумма счёта'))
# #
# plt.show(macduck['day'].value_counts().plot(kind = 'bar', grid = True, colormap = 'coolwarm', title = 'Количество посетителей по дням'))

# plt.show(macduck.groupby(by = ['sex', 'smoker'])['tip'].mean().plot(kind = 'bar', grid= True))

# def maskify(cc):
#     if len(cc) <= 4:
#         return cc
#     else:
#         cc2 = list(map(lambda c : c.replace(c, '#'), cc[:-4]))
#         cc2 += cc[-4:]
#         return (''.join(cc2))

# def maskify(cc):
#     return len(cc[:-4])*"#" + cc[-4:]
#
# print(maskify("1"))

# def descending_order(num):
#     return int(''.join(sorted(str(num), reverse = True)))
#
# print(descending_order(0))

# def DNA_strand(dna):
#     dna2 = []
#     for x in dna:
#         if x == 'A':
#             dna2 += 'T'
#         elif x == 'T':
#             dna2 += 'A'
#         elif x == 'G':
#             dna2 += 'C'
#         elif x == 'C':
#             dna2 += 'G'
#     dna = ''.join(dna2)
#     return dna


# def DNA_strand(dna):
#     return ''.join([{'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}[letter] for letter in dna])
#
# print(DNA_strand("GTAT"))