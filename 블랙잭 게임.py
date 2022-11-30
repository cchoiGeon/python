import random
a = random.randint(1,11)
b = random.randint(1,11)
c = random.randint(1,11)
d = random.randint(1,11)
e = random.randint(1,11)
f = random.randint(1,11)
g = random.randint(1,11)
h = random.randint(1,11)
i = random.randint(1,11)
j = random.randint(1,11)
k = random.randint(1,11)
l = random.randint(1,11)
m = random.randint(1,11)
n = random.randint(1,11)
o = random.randint(1,11)
p = random.randint(1,11)
q = random.randint(1,11)
r = random.randint(1,11)
s = random.randint(1,11)
t = random.randint(1,11)
u = random.randint(1,11)
v = random.randint(1,11)
w = random.randint(1,11)
x = random.randint(1,11)
y = random.randint(1,11)
z = random.randint(1,11)
print("당신의 첫번째 카드는{}입니다.".format(a))
print("당신의 두번째 카드는{}입니다.".format(b))
print("")
#첫번째 if문
if a+b == 22: # 패가 22가 넘었을 때 두개의 11중 하나의 11을 -10 연산을 통해 1로 만들고 12로 만들어 계속 진행하는 코드이다. else 문으로는 그냥 아래 코드랑 똑같이 박으면 됨. -> 구현 완료
     result_1 = a+b-10
     print("당신의 패는 {}입니다.".format(result_1))
     print("더 뽑으시겠습니까?")
     ready_1 = input("1. 네 2. 아니요 > ")
     int_ready_1 = int(ready_1)
  #두번째 if문 (첫번째에 주는 카드에서 더 받을 때)
     if int_ready_1 == 1:
         print("당신의 세번째 카트는 {}입니다.".format(c))
         result_2 = result_1 + c
         print("당신의 패는 {}입니다. ".format(result_2))
         if result_2 >21 :
              print("21을 넘어 졌습니다.")
         else:
              print("더 뽑으시겠습니까?")
              print("")
              ready_2 = input("1.네 2.아니요 > ")
              int_ready_2 = int(ready_2)  
              if int_ready_2 == 1:
                      print("당신의 네번째 카트는 {}입니다.".format(d))
                      print("")
                      result_3 = result_2 + d
                      print("당신의 패는 {}입니다.".format(result_3))
                      if result_3 > 21:
                          print("패배하셨습니다.")
                      else:
                        print("딜러의 패를 공개하겠습니다.")
                        print("딜러의 첫 번째 패 {}, 두 번째 패 {} 입니다.".format(e,f))
                        dealer_1 = e + f
                        if dealer_1 == 22:# 딜러의 첫판 패가 22가 넘었을 때 두개의 11중 하나의 11을 -10 연산을 통해 1로 만들고 12로 만들어 계속 진행하는 코드이다. elif를 통해 17보다 클 때는 바로 멈춰서 result_3과 비교를 통해 누가 이겼는지 알려주는 코드를 만들어야 된다. 17보다 작을 때에는 (구현완료)
                              dealer_result_1 = dealer_1 - 10
                              print("딜러의 패는 {}입니다.".format(dealer_result_1))
                              print("계속 진행 중입니다.")
                              dealer_result_2 = dealer_result_1 + g
                              print("딜러의 세 번째 패는 {}입니다.".format(dealer_result_2))
                          
                              if dealer_result_2 > 21: 
                                         print("이기셨습니다!") 
                              elif dealer_result_2 >= 17:# 딜러의 패가 17을 넘었다. 
                                        if dealer_result_2 > result_3: #딜러가 이겼을 때
                                            print("딜러가 이겼습니다!")
                                        elif dealer_result_2 < result_3:# 딜러가 졌을 때
                                            print("이기겼습니다!")
                                        else:
                                            print("비기셨습니다.") # 비겼을 때
                              else : #딜러의 패가 17이 안됐을 때 
                                        print("딜러의 네 번째 패는 {}입니다.".format(h))
                                        dealer_result_3 = dealer_result_2 + h
                                        print("딜러의 패는 {}입니다.".format(dealer_result_3))
                                        if dealer_result_3 > 21: # 딜러의 패가 21을넘었다.
                                            print("이기셨습니다!")
                                        elif dealer_result_3 > 17:# 딜러의 패가 17을 넘었다. 
                                            if dealer_result_3 > result_3: #딜러가 이겼을 때
                                                  print("딜러가 이겼습니다!")
                                            elif dealer_result_3 < result_3:# 딜러가 졌을 때
                                                  print("이기겼습니다!")
                                            else:
                                                  print("비기셨습니다.") # 비겼을 때
                                        else: # 딜러의 패가 17이 안됐다. 
                                            print("구현 안됨 ~ ")
                                
                        elif dealer_1 >= 17: # 첫판 패 딜러 패가 17을 넘었다.
                            if dealer_result_1 > result_3: #딜러가 이겼을 때
                                    print("딜러가 이겼습니다!")
                            elif dealer_result_1 < result_3:# 딜러가 졌을 때
                                    print("이기겼습니다!")
                            else:
                                    print("비기셨습니다.") # 비겼을 때
                        else: #계속 패를 받으며 if 절을 통해 17을 넘으면 스톱한다.
                            print("딜러의 세 번째 패는 {}입니다.".format(i))
                            dealer_result_4 = dealer_result_1 + i
                            print("딜러의 패는 {}입니다.".format(dealer_result_4))
                            if dealer_result_4 > 21: # 딜러의 패가 21을넘었다.
                                    print("이기셨습니다!")
                            elif dealer_result_4 >= 17:# 딜러의 패가 17을 넘었다. 
                                    if dealer_result_4 > result_3: #딜러가 이겼을 때
                                           print("딜러가 이겼습니다!")
                                    elif dealer_result_4 < result_3:# 딜러가 졌을 때
                                           print("이기겼습니다!")
                                    else:
                                           print("비기셨습니다.") # 비겼을 때
                            else: # 딜러의 패가 17이 안됐다. 
                                    print("구현 안됨 ~ ")
              else:
                      print("딜러의 패를 공개하겠습니다.")
                      print("딜러의 첫 번째 패 {}, 두 번째 패 {} 입니다.".format(v,w))
                      dealer_1 =  v+w
                      if dealer_1 == 22:# 딜러의 첫판 패가 22가 넘었을 때 두개의 11중 하나의 11을 -10 연산을 통해 1로 만들고 12로 만들어 계속 진행하는 코드이다. elif를 통해 17보다 클 때는 바로 멈춰서 result_3과 비교를 통해 누가 이겼는지 알려주는 코드를 만들어야 된다. 17보다 작을 때에는 (구현완료)
                              dealer_result_1 = dealer_1 - 10
                              print("딜러의 패는 {}입니다.".format(dealer_result_1))
                              print("계속 진행 중입니다.")
                              dealer_result_2 = dealer_result_1 + x
                              print("딜러의 세 번째 패는 {}입니다.".format(dealer_result_2))
                          
                              if dealer_result_2 > 21: 
                                         print("이기셨습니다!") 
                              elif dealer_result_2 >= 17:# 딜러의 패가 17을 넘었다. 
                                        if dealer_result_2 > result_3: #딜러가 이겼을 때
                                            print("딜러가 이겼습니다!")
                                        elif dealer_result_2 < result_3:# 딜러가 졌을 때
                                            print("이기겼습니다!")
                                        else:
                                            print("비기셨습니다.") # 비겼을 때
                              else : #딜러의 패가 17이 안됐을 때 
                                        print("딜러의 네 번째 패는 {}입니다.".forma(y))
                                        dealer_result_3 = dealer_result_2 + y
                                        print("딜러의 패는 {}입니다.".format(dealer_result_3))
                                        if dealer_result_3 > 21: # 딜러의 패가 21을넘었다.
                                            print("이기셨습니다!")
                                        elif dealer_result_3 > 17:# 딜러의 패가 17을 넘었다. 
                                            if dealer_result_3 > result_3: #딜러가 이겼을 때
                                                  print("딜러가 이겼습니다!")
                                            elif dealer_result_3 < result_3:# 딜러가 졌을 때
                                                  print("이기겼습니다!")
                                            else:
                                                  print("비기셨습니다.") # 비겼을 때
                                        else: # 딜러의 패가 17이 안됐다. 
                                            print("구현 안됨 ~ ")
                                
                      elif dealer_1 >= 17: # 첫판 패 딜러 패가 17을 넘었다.
                            if dealer_result_1 > result_3: #딜러가 이겼을 때
                                    print("딜러가 이겼습니다!")
                            elif dealer_result_1 < result_3:# 딜러가 졌을 때
                                    print("이기겼습니다!")
                            else:
                                    print("비기셨습니다.") # 비겼을 때
                      else: #계속 패를 받으며 if 절을 통해 17을 넘으면 스톱한다.
                            print("딜러의 세 번째 패는 {}입니다.".format(i))
                            print("")
                            dealer_result_4 = dealer_result_1 + i
                            print("딜러의 패는 {}입니다.".format(dealer_result_4))
                            print("")
                            if dealer_result_4 > 21: # 딜러의 패가 21을넘었다.
                                    print("이기셨습니다!")
                            elif dealer_result_4 >= 17:# 딜러의 패가 17을 넘었다. 
                                    if dealer_result_4 > result_3: #딜러가 이겼을 때
                                           print("딜러가 이겼습니다!")
                                    elif dealer_result_4 < result_3:# 딜러가 졌을 때
                                           print("이기겼습니다!")
                                    else:
                                           print("비기셨습니다.") # 비겼을 때
                            else: # 딜러의 패가 17이 안됐다. 
                                    print("구현 안됨 ~ ")






     else: # 첫번째 패에 만족하고 그만 뽑아 딜러의 패만 공개하면 됨 q부터 사용
            print("딜러의 패를 공개하겠습니다.")
            print("")
            print("딜러의 첫 번째 패 {}, 두 번째 패 {} 입니다.".format(q,r))
            print("")
            very_dealer_1 =  q+r
            if very_dealer_1 == 22:# 딜러의 첫판 패가 22가 넘었을 때 / 딜러패임 
                dealer_result_1 = very_dealer_1 - 10
                print("딜러의 패는 {}입니다.".format(dealer_result_1))
                print("")
                print("계속 진행 중입니다.")
                print("")
                dealer_result_2 = dealer_result_1 + s
                print("딜러의 세 번째 패는 {}입니다.".format(dealer_result_2))
                print("")
                if dealer_result_2 > 21:
                   print("이기셨습니다!")
                elif dealer_result_2 >=17:
                     if dealer_result_2 > result_1:
                         print("지셨습니다!")
                     elif dealer_result_2 < result_1:
                         print("이기셨습니다!")
                     else:
                         print("비기셨습니다!")    

                else :
                   dealer_result_3 = dealer_result_2 + t
                   print("딜러의 네 번째 패는 {}입니다.".format(t))
                   print("")
                   print("딜러의 패는 {}입니다.".format(dealer_result_3))
                   if dealer_result_3 > 21:
                        print("이기셨습니다!")
                   elif dealer_result_3 >=17:
                      if dealer_result_3 > result_1:
                            print("지셨습니다!")
                      elif dealer_result_3 < result_1:
                            print("이기셨습니다!")
                      else:
                            print("비기셨습니다!")  
                   else:
                      print("운이 안 좋네요 그냥 이겼다 쳐요")
            elif very_dealer_1 >= 17:#딜러 패가 17을 넘겼을 때 
                  if very_dealer_1> 21:
                      print("이기셨습니다!")
                  elif very_dealer_1 < result_1:
                      print("이기셨습니다!")
                  elif very_dealer_1 > result_1:
                      print("지셨습니다!")
                  else:
                      print("비기셨습니다")

      
            else: # 딜러의 패가 17을 못 넘어 패를 계속 받아야 할 때
                print("딜러의 패를 계속 진행시키겠습니다")
                dealer_result_4 = very_dealer_1 + u
                print("딜러의 세번째 패는 {}입니다.".format(u))
                print("딜러의 패는 {}입니다.".format(dealer_result_4))
                if dealer_result_4 > 21:
                    print("이기셨습니다!")
                elif dealer_result_4 >=17:
                    if dealer_result_4 > result_1:
                        print("지셨습니다")
                    elif dealer_result_4 < result_1:
                        print("이기셨습니다!")
                    else:
                        print("비기셨습니다")
                else:
                    print("")

      
else: # 처음 패 a+b에서 21를 넘지 않을 때 대부분 이 코드로 실행된다. 여기서는 result가 아닌 good으로 정함 숫자는 j부터 시작함 구현 완료
  good = a+b
  print("당신의 패는 {}입니다.".format(good))
  print("")
  print("더 뽑으시겠습니까?")
  print("")
  good_ready_1 = input("1. 네 2. 아니요 > ")
  int_good_ready_1 = int(good_ready_1)
  if int_good_ready_1 == 1: # 더뽑을 때 코드들 / 세번 째 카드까지 볼 때
         print("당신의 세번째 카트는 {}입니다.".format(j))
         print("")
         good_2 = good + j
         print("당신의 패는 {}입니다. ".format(good_2))
         print("")
         if good_2 >21 :
              print("21을 넘어 졌습니다.")
         else:
              print("더 뽑으시겠습니까?")
              good_ready_2 = input("1.네 2.아니요 > ")
              int_good_ready_2 = int(good_ready_2)
              if int_good_ready_2 == 1: # 네번째 카드까지 볼 때
                      print("당신의 네번째 카트는 {}입니다.".format(k))
                      good_3 = good_2 + k
                      print("당신의 패는 {}입니다.".format(good_3))
                      if good_3 > 21:
                        print("지셨습니다.")
                      else:
                        print("딜러의 패를 공개하겠습니다.")
                        print("")
                        print("딜러의 첫 번째 패 {}, 두 번째 패 {} 입니다.".format(l,m))
                        print("")
                        good_dealer_1 = l + m       
                        if good_dealer_1 == 22:# 딜러의 첫판 패가 22가 넘었을 때 두개의 11중 하나의 11을 -10 연산을 통해 1로 만들고 12로 만들어 계속 진행하는 코드이다. elif를 통해 17보다 클 때는 바로 멈춰서 result_3과 비교를 통해 누가 이겼는지 알려주는 코드를 만들어야 된다. 
                              good_dealer_result_1 = good_dealer_1 - 10
                              print("딜러의 패는 {}입니다.".format(good_dealer_result_1))
                              print("")
                              print("계속 진행 중입니다.")
                              print("")
                              good_dealer_result_2 = good_dealer_result_1 + n
                              print("딜러의 세 번째 패는 {}입니다.".format(good_dealer_result_2))
                              print("")
                              if good_dealer_result_2 > 21: 
                                    print("이기셨습니다!") 
                              elif good_dealer_result_2 > 17:# 딜러의 패가 17을 넘었다. 
                                    if good_dealer_result_2 > good_3: #딜러가 이겼을 때
                                            print("딜러가 이겼습니다!")
                                    elif dealer_result_2 < good_3:# 딜러가 졌을 때
                                            print("이기겼습니다!")
                                    else:
                                            print("비기셨습니다.") # 비겼을 때
                              else : #딜러의 패가 17이 안됐을 때 
                                    print("딜러의 네 번째 패는 {}입니다.".format(o))
                                    print("")
                                    good_dealer_result_3 = good_dealer_result_2 + o
                                    print("딜러의 패는 {}입니다.".format(good_dealer_result_3))
                                    if good_dealer_result_3 > 21: # 딜러의 패가 21을넘었다.
                                          print("이기셨습니다!")
                                    elif good_dealer_result_3 > 17:# 딜러의 패가 17을 넘었다. 
                                          if good_dealer_result_3 > good_3: #딜러가 이겼을 때
                                                  print("딜러가 이겼습니다!")
                                          elif good_dealer_result_3 < good_3:# 딜러가 졌을 때
                                                  print("이기겼습니다!")
                                          else:
                                                  print("비기셨습니다.") # 비겼을 때
                                    else: # 딜러의 패가 17이 안됐다. 
                                          print("구현 안됨 ~ ")
                        elif good_dealer_1 > 17: # 첫판 패 딜러 패가 17을 넘었다.
                              if good_dealer_1 > good_3: #딜러가 이겼을 때
                                    print("딜러가 이겼습니다!")
                              elif good_dealer_1 < good_3:# 딜러가 졌을 때
                                    print("이기겼습니다!")
                              else:
                                    print("비기셨습니다.") # 비겼을 때
                        else: #계속 패를 받으며 if 절을 통해 17을 넘으면 스톱한다.
                              print("딜러의 세 번째 패는 {}입니다.".format(p))
                              print("")
                              good_dealer_result_4 = good_dealer_1 + p
                              print("딜러의 패는 {}입니다.".format(good_dealer_result_4))
                              print("")
                              if good_dealer_result_4 > 21: # 딜러의 패가 21을넘었다.
                                    print("이기셨습니다!")
                              elif good_dealer_result_4 > 17:# 딜러의 패가 17을 넘었다. 
                                    if good_dealer_result_4 > good_3: #딜러가 이겼을 때
                                           print("딜러가 이겼습니다!")
                                    elif good_dealer_result_4 < good_3:# 딜러가 졌을 때
                                           print("이기겼습니다!")
                                    else:
                                           print("비기셨습니다.") # 비겼을 때
                              else: # 딜러의 패가 17이 안됐다. 
                                    print("구현 안됨 ~ ")      
    
                
                  

  else: # 두번째 패까지만 받고 받지 않음
                      print("딜러의 패를 공개하겠습니다.")
                      print("")
                      print("딜러의 첫 번째 패 {}, 두 번째 패 {} 입니다.".format(l,m))
                      good_dealer_1 = l + m
                      if good_dealer_1 == 22:# 딜러의 첫판 패가 22가 넘었을 때 두개의 11중 하나의 11을 -10 연산을 통해 1로 만들고 12로 만들어 계속 진행하는 코드이다. elif를 통해 17보다 클 때는 바로 멈춰서 result_3과 비교를 통해 누가 이겼는지 알려주는 코드를 만들어야 된다. 
                              good_dealer_result_1 = good_dealer_1 - 10
                              print("딜러의 패는 {}입니다.".format(good_dealer_result_1))
                              print("")
                              print("계속 진행 중입니다.")
                              print("")
                              good_dealer_result_2 = good_dealer_result_1 + n
                              print("딜러의 세 번째 패는 {}입니다.".format(good_dealer_result_2))
                              if good_dealer_result_2 > 21: 
                                    print("이기셨습니다!") 
                              elif good_dealer_result_2 > 17:# 딜러의 패가 17을 넘었다. 
                                    if good_dealer_result_2 > good_3: #딜러가 이겼을 때
                                            print("딜러가 이겼습니다!")
                                    elif dealer_result_2 < good_3:# 딜러가 졌을 때
                                            print("이기겼습니다!")
                                    else:
                                            print("비기셨습니다.") # 비겼을 때
                              else : #딜러의 패가 17이 안됐을 때 
                                    print("딜러의 네 번째 패는 {}입니다.".format(o))
                                    print("")
                                    good_dealer_result_3 = good_dealer_result_2 + o
                                    print("딜러의 패는 {}입니다.".format(good_dealer_result_3))
                                    print("")
                                    if good_dealer_result_3 > 21: # 딜러의 패가 21을넘었다.
                                          print("이기셨습니다!")
                                    elif good_dealer_result_3 > 17:# 딜러의 패가 17을 넘었다. 
                                          if good_dealer_result_3 > good_3: #딜러가 이겼을 때
                                                  print("딜러가 이겼습니다!")
                                          elif good_dealer_result_3 < good_3:# 딜러가 졌을 때
                                                  print("이기겼습니다!")
                                          else:
                                                  print("비기셨습니다.") # 비겼을 때
                                    else: # 딜러의 패가 17이 안됐다. 
                                          print("적당히 해 십알 구현 안됨 ~ ")
                      elif good_dealer_1 > 17: # 첫판 패 딜러 패가 17을 넘었다.
                              if good_dealer_1 > good_3: #딜러가 이겼을 때
                                    print("딜러가 이겼습니다!")
                              elif good_dealer_1 < good_3:# 딜러가 졌을 때
                                    print("이기겼습니다!")
                              else:
                                    print("비기셨습니다.") # 비겼을 때
                      else: #계속 패를 받으며 if 절을 통해 17을 넘으면 스톱한다.
                              print("딜러의 패는 {}입니다.".format(good_dealer_1))
                              print("")
                              print("딜러의 세 번째 패는 {}입니다.".format(p))
                              print("")
                              good_dealer_result_4 = good_dealer_1 + p
                              print("딜러의 패는 {}입니다.".format(good_dealer_result_4))
                              if good_dealer_result_4 > 21: # 딜러의 패가 21을넘었다.
                                    print("이기셨습니다!")
                              elif good_dealer_result_4 > 17:# 딜러의 패가 17을 넘었다. 
                                    if good_dealer_result_4 > good: #딜러가 이겼을 때
                                           print("딜러가 이겼습니다!")
                                    elif good_dealer_result_4 < good:# 딜러가 졌을 때
                                           print("이기겼습니다!")
                                    else:
                                           print("비기셨습니다.") # 비겼을 때
                              else: # 딜러의 패가 17이 안됐다. 
                                    print("구현 안됨 ~ ")
              
