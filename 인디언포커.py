import random
c = 10
while True:
  a = random.randint(1,10)
  b = random.randint(1,10)
  print("코인 : {}".format(c))
  print("")
  print("상대방의 패는 {}입니다.".format(a))
  print("")
  ready_1 = input("죽으시겠습니까?  1. 네 2. 아니요 > ")
  print("")
  int_ready_1 = int(ready_1)
  if int_ready_1 == 1:
    c-=1
    if c<=0:
      print("코인을 다 소모하셨습니다")
      break

    else:
      pass

  else:
    ready_2 = input(" 몇 개의 코인을 거시겠습니까? > ")
    print("")
    coin = int(ready_2)
    if coin > c:
      print("다시 입력하세요.")
      break #원래는 ready_2 구문으로 다시 돌아가야 되는데 그런 함수를 알지 못해서 break으로                아예 초기화를 해버림
    else:
      pass
    
    if a > b:
      print("상대방이 이겼습니다 !")
      print("")
      c = c - coin
    elif a < b:
      print("이기셨습니다!")
      print("")
      c = c + coin    
    else:
      print("비기셨습니다!")
      print("")
  if c == 0:
      print("가지고 있는 코인을 전부 소모하셨습니다!")
      break  
  elif c >= 100:
      print("우승하셨습니다!")