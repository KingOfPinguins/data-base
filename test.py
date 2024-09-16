
import random
from time import sleep
import multiprocessing
import openpyxl
import xlsxwriter
from threading import Thread, Event
from time import sleep

# event = Event()

# def modify_variable(var):
#     while True:
#         for i in range(len(var)):
#             var[i] += 1
#         if event.is_set():
#             break
#         sleep(.5)
#     print('Stop printing')


# my_var = [1, 2, 3]
# t = Thread(target=modify_variable, args=(my_var, ))
# t.start()
# while True:
#     try:
#         print(my_var)
#         sleep(1)
#     except KeyboardInterrupt:
#         event.set()
#         break
# t.join()
# print(my_var)


#####################################################
# event = Event()
# def modify_variable(var):
#     while True:
#         #for i in range(len(var)):
#         #    var[i] += 1
#         var[0] = 'b'
#         if event.is_set():
#             break
#         sleep(1)
#     print('Stop printing')


# my_var = ['a']
# t = Thread(target=modify_variable, args=(my_var, ))
# t.start()
# while True:
#     try:
#         print(my_var)
#         sleep(.5)
#     except KeyboardInterrupt:
#         event.set()
#         break
# t.join()
# print(my_var)





# numb = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# odds = filter(lambda x: x % 2, numb)

# # for i in odds:
# #     print(i)

# print(type(odds))

# if any(odds):
#     print(any(odds))
#     for odd in odds:
#         print(odd)

# for i in odds:
#     print(i) 

# list_numb = [ numbers for numbers in range(101) ]

# counter = 0

# for i in list_numb:
#     if '9' in str(i):
#         for y in str(i):
#             if y == '9':
#                 counter += 1
#                 #print(i)
#     else:
#         pass

# print("--", counter)
# print("--", list_numb)


# print(2*2 + 3*3)





LIST_ELEM =  '/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]'
address =    '/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[7]/div[3]'
web_page =   '/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[7]/div[6]'
phone =      '/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[7]/div[5]'
            #'/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[7]/div[5]/button/div/div[2]'


new_line_phone = LIST_ELEM[0:-10] + '[2]/div[7]/div[3]'

print(LIST_ELEM, '\n', new_line_phone)