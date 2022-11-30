import random
import turtle as t
# 계속된 랜덤 값을 넣어줘야 하므로 처음부터 while 함수로 시작해야 된다.
while True:
# 사진 넣을 수 있으면 사진 넣기/ 기초 배경 
  t.bgcolor("black")
  t.up()
  t.ht()
  
# dealer 카드 설정.
  a = random.randint(1,10)
  if a == 1:
    dealer_gif = "game/dealer_gif."
    t.addshape(dealer_gif)
  elif a== 2:
    dealer_gif = "game/dealer_gif."
    t.addshape(dealer_gif)
  elif a== 3:
    dealer_gif = "game/dealer_gif."
    t.addshape(dealer_gif)
  elif a== 4:
    dealer_gif = "game/dealer_gif."
    t.addshape(dealer_gif)
  elif a== 5:
    dealer_gif = "game/dealer_gif."
    t.addshape(dealer_gif)
  elif a== 6:
    dealer_gif = "game/dealer_gif."
    t.addshape(dealer_gif)
  elif a== 7:
    dealer_gif = "game/dealer_gif."
    t.addshape(dealer_gif)
  elif a== 8:
    dealer_gif = "game/dealer_gif."
    t.addshape(dealer_gif)
  elif a== 9:
    dealer_gif = "game/dealer_gif."
    t.addshape(dealer_gif)
  elif a== 10:
    dealer_gif = "game/dealer_gif."
    t.addshape(dealer_gif)
  else:
    pass
    
  # player 카드 설정.
  b = random.randint(1,10)
  if b == 1:
    player_gif = "game/player_gif."
    t.addshape(player_gif)
  elif b== 2:
    playerr_gif = "game/player_gif."
    t.addshape(player_gif)
  elif b== 3:
    player_gif = "game/player_gif."
    t.addshape(player_gif)
  elif b== 4:
    player_gif = "game/player_gif."
    t.addshape(player_gif)
  elif b== 5:
    player_gif = "game/player_gif."
    t.addshape(player_gif)
  elif b== 6:
    player_gif = "game/player_gif."
    t.addshape(player_gif)
  elif b== 7:
    player_gif = "game/player_gif."
    t.addshape(player_gif)
  elif b== 8:
    player_gif = "game/player_gif."
    t.addshape(player_gif)
  elif b== 9:
    player_gif = "game/player_gif."
    t.addshape(player_gif)
  elif b== 10:
    player_gif = "game/player_gif."
    t.addshape(player_gif)
  else:
    pass

# 플레이어 뒤집어 있는 카드 설정
  player_start_gif = "이미지 파일 경로 / 뒤집혀 있는 카드 gif"
  t.addshape(player_start_gif)
# 코인 설정
  coin_gif =  "이미지 파일 경로 / 코인 gif"
  t.addshape(coin_gif)
# 사진 크기 정해주기~ 
  pass

# 제목 및 첫 화면 정해주기
  t.title("인디언 포커 게임")
  title_1 = t.numinput("","  인디언 포커 게임\n 아무 바탕이나 눌러주세요 ") # 예를 들면 모두의 마블 게임을 들어가면 아무곳이나 클릭해주세요 이런 느낌이다. 클릭하면 바탕에 있는 곳이 바뀌면서 게임을 바로 시작할 수 있는 곳으로 넘어가준다. 나는 이것을 next로 설정할 것이다.

  t.onscreenclick(next,1)# 마우스 왼쪽 클릭시 다음으로 넘어감
  
  def next(x,y):
  # 게임 시작 화면으로 들어간다. 설정해줘야 되는 것은 게임 같은 화면과 상대방 패를 먼저 까주는 것이다. 내 패는 뒤집혀져있는 상태로 출력된다. 코인도 몇개인지 알려주기 ~
    c = 10
    t.bgcolor("green") # 사진 넣어주기 !~ 
    t.write("상대방 패",False,"center",("",30))
    t.goto(-200,-100)
    t.shape(dealer_gif) # 출력해주기 
    t.write("내 패",False,"center",("",30))
    t.goto(200,-100)
    t.shape(player_start_gif)
    t.goto(200,100)
    t.shape(coin_gif)
    t.write("{}".format(c),False,"center",("",10))
    # 상대방 패를 보고 결정하는 단계.
    t.title_2 = t.numinput("", "죽으시겠습니까? 1. 네 2.아니요 ")
    if t.title_2 == 1:
      c = c -1
      if c<=0:
        t.write("소유하고 있는 코인을 다 소모하셨습니다 ! ",False,"center",("",50))
        exit()
      else:
        pass

    else:
      t.title_3 = t.numinput("", "몇 개의 코인을 거시겠습니까? ")
      coin = t.title_3
      if coin > c:
        t.title_4 = t.textinput("","다시 입력해주세요")
        return t.title_3 
      else:
        pass
      t.goto(200,-100)
      t.shape(player_gif)
      if a > b:
        t.write("패배",False,"center",("",30))
        c = c - coin
      elif a < b:
        t.write("승리",False,"center",("",30))
        c = c + coin    
      else:
        t.write("무승부",False,"center",("",30))
    if c == 0:
      t.write("소유하고 있는 코인을 다 소모하셨습니다 ! ",False,"center",("",50))
      exit()
    elif c >= 100:
      t.write("우승하셨습니다!",False,"center",("",50))


next()