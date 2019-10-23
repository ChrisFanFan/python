from mora_api import mora_type_generator

mora_type = ["剪刀", "石頭", "布"]

count = 1
while (count < 10):
  print("Game ", count)

  user_input = int(input("來猜拳阿!!!豬會選什麼呢???\n  1:剪刀\n  2:石頭 \n  3:布\nChoose>>"))

  if user_input < 1 or user_input > 3:
    print("Error Input")
    continue

  user_choose = mora_type[(user_input)-1]

  print("豬選了:", user_choose)

  robots_input = mora_type_generator(mora_type)

  print("電腦選了:", robots_input)

  if robots_input == user_choose:
    print("平手")
  elif (user_choose=="剪刀" and robots_input=="布") or (user_choose=="石頭" and robots_input=="剪刀") or  (user_choose=="布" and robots_input=="石頭"):
    print("豬贏囉")
  else:
    print("豬輸囉")

  count = count + 1

  print("======================================")
print("The game is over!")