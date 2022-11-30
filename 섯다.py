import random
import turtle as t
e = 10

while True:
  t.bgcolor("black")
  t.up()
  t.ht()
  a = random.randint(1,10)
  b = random.randint(1,10)
  c = random.randint(1,10)
  d = random.randint(1,10)
  
  player = a + b
  dealer = c + d
  if player >= 10:
    player = player - 10
  else:
    pass
  if dealer >= 10:
    dealer = dealer - 10
  else:
    pass
  print("코인 : {}".format(e))
  print("")
  print("당신의 패는 {}입니다.".format(a))
  print("")
  print("상대방 패는 {}입니다.".format(c))
  print("")
  ready = input("계속 받으시겠습니까? 죽으시겠습니까? 1. 계속 2. 죽는다 > ")
  print("")
  int_ready = int(ready)
  if int_ready == 1:
    coin_str = input("몇 개의 코인을 거시겠습니까? > ")
    print("")
    coin = int(coin_str)
    if coin > e:
      print("다시 입력하세요")
      break
    else:
      pass
    print("두번째 패는 {}입니다.".format(b))
    print("")
    print("당신의 패는 {},{}입니다.".format(a,b))
    print("")
    print("상대방 패를 오픈하겠습니다.")
    print("")
    print("상대방 패는 {}, {} 입니다.".format(c,d))
    print("")
    if a == b:
      print("당신의 패는 {}땡 입니다!".format(a))
      print("")
      if c == d:
        print("상대방의 패는 {}땡 입니다 !".format(c))
        print("")
        if a > c:
          print("이기셨습니다!")
          e = e + coin
        elif a < c:
          print("지셨습니다!")
          e = e - coin
          if e <= 0:
            print("코인을 전부 소모하셨습니다.")
            break
          else:
            pass
        else:
          print("비기셨습니다!")
      else:
        print("이기셨습니다!")
        print("")
        
    elif c == d: 
       print("상대방의 패는 {}땡 입니다 !".format(c))
       print("")
       print("지셨습니다 !")
       print("")
       e = e - coin
       if e <= 0:
          print("코인을 전부 소모하셨습니다.")
          break
       else:
          pass
    elif player > dealer:
      print("당신의 패는 {}끗   상대방 패는 {} 끗 입니다.".format(player,dealer))
      print("")
      print("이기셨습니다!")
      print("")
      e = e + coin
    elif player < dealer: 
      print("당신의 패는 {}끗   상대방 패는 {} 끗 입니다.".format(player,dealer))
      print("")
      print("지셨습니다!")
      print("")
      e = e - coin
      if e <= 0:
        print("코인을 전부 소모하셨습니다.")
        break
      else:
        pass
    else:
      print("비기셨습니다!")
    