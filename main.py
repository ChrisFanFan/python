from mora_api import mora_type_generator
from mora_api import my_name

my_name()

print("豬八戒來猜拳阿")


user_input = input("來猜拳阿!!!豬會選什麼呢???\n  1:剪刀\n  2:石頭 \n  3:布\nChoose>>")

print("豬選了:", user_input)
 

print("豬選了:", user_choose)

robots_input = mora_type_generator()

print("電腦選了:", robots_input)

'''
for x in range(10):
  print(mora_type_generator())
'''

if robots_input == user_choose:
  print("平手")
elif (user_choose=="剪刀" and robots_input=="布") or (user_choose=="石頭" and robots_input=="剪刀") or  (user_choose=="布" and robots_input=="石頭"):
  print("豬贏囉")
else:
  print("豬輸囉")
