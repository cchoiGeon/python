import random
a = random.randint(1,1000)
i = 0
while True:
  str_result = input("임의의 수를 맞추시오 ! > ")
  print("")
  int_result = int(str_result)
  i += 1
  if int_result == a:
    print("맞추셨습니다 !")
    print("")
    print("{}회 만에 성공하셨습니다 !".format(i))
    break
  elif int_result > a:
    print("Down!")
  else:
    print("Up!")