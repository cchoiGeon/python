import turtle as t
import time
# 사진들 넣어주기.
첫_화면 = "빈 강의실 만들기 프로젝트/첫 화면.gif"
t.addshape(첫_화면)
학교_건물_지도 = "빈 강의실 만들기 프로젝트/학교 건물 지도.gif"
t.addshape(학교_건물_지도)
산학융합관_2층 = "빈 강의실 만들기 프로젝트/산학융합관 2층.gif"
t.addshape(산학융합관_2층)
산학융합관_3층 = "빈 강의실 만들기 프로젝트/산학융합관 3층.gif"
t.addshape(산학융합관_3층)
산학융합관_4층 = "빈 강의실 만들기 프로젝트/산학융합관 4층.gif"
t.addshape(산학융합관_4층)
산학융합관_5층 = "빈 강의실 만들기 프로젝트/산학융합관 5층.gif"
t.addshape(산학융합관_5층)
산학융합관_6층 = "빈 강의실 만들기 프로젝트/산학융합관 6층.gif"
t.addshape(산학융합관_6층)
산학융합관_7층 = "빈 강의실 만들기 프로젝트/산학융합관 7층.gif"
t.addshape(산학융합관_7층)
# 강의실들 0으로 먼저 초기화 시켜주기 함수 속에 글로벌 (global()함수 꼭 넣기 !!) 사용하기
산융_701호 = 0
산융_702호 = 0
산융_703호 = 0
산융_704호 = 0
산융_705호 = 0
산융_706호 = 0
산융_707호 = 0
산융_708호 = 0

# 함수 정의하기
# 첫 번째 함수 = 학교 건물 위치를 알려주는 사진을 띄운다. 쉬운 방법으로 10초를 딜레이 시킨 뒤 어떤 건물을 사용할 것인지 물어본다. 다른 방법으론 화면을 터치해서 어떤 건물을 사용할 것인지 물어보는 방법도 있다.
def first_screen(x,y):
  t.shape(학교_건물_지도)
  time.sleep(10)
  t.a =str(t.numinput("","어느 건물을 사용하시겠습니까?"))
  if t.a =="산학융합관":
    산학융합관()  
  elif t.a == "A동":
    A동()
  elif t.a == "B동":
    B동()
  elif t.a == "A동":
    C동()
  elif t.a == "A동":
    D동()
  elif t.a == "A동":
    E동()
def A동(x,y):
  pass
def B동(x,y):
  pass
def C동(x,y):
  pass
def D동(x,y):
  pass
def E동(x,y):
  pass
# 두 번째 함수 = A동~E동 + 산학융합관까지 어떤 건물을 쓸 것인지 입력 받은 건물의 강의실 전개도(지도)를 보여주면서 2층 ~ 7층까지 선택할 수 있게 한다.
def 산학융합관(x,y):
  t.shape(산학융합관_2층)
  time.sleep(10)
  t.b = t.strinput("","몇 층을 이용하시겠습니까?")
  if t.a == "7층":
    산학융합관_7floor()
  if t.a == "6층":
    산학융합관_6floor()
  if t.a == "5층":
    산학융합관_5floor()
  if t.a == "4층":
    산학융합관_4floor()
  if t.a == "3층":
    산학융합관_3floor()
  if t.a == "2층":
    산학융합관_2floor()
    
def 산학융합관_7floor(x,y):
  t.shape(산학융합관_7층)
  global 산융_701호
  global 산융_702호
  global 산융_703호
  global 산융_704호
  global 산융_705호
  global 산융_706호
  global 산융_707호
  global 산융_708호
  t.fisrt_input = t.strinput("","입실, 퇴실, 예약 중 무엇을 선택하시겠습니까?")
  if t.first_input == "입실":
    input = t.strinput("","사용하실 강의실을 입력해주세요")
    if input == "701호":
      if 산융_701호 == 0:
        t.write("입실이 완료 되셨습니다",False,"center",("",30))
        산융_701호 = 1
        return
      else:
        t.write("사용 중인 강의실입니다",False,"center",("",30))
        return
    if input == "702호":
      if 산융_702호 == 0:
        t.write("입실이 완료 되셨습니다",False,"center",("",30))
        산융_702호 = 1
        return
      else:
        t.write("사용 중인 강의실입니다",False,"center",("",30))
        return
    if input == "703호":
      if 산융_703호 == 0:
        t.write("입실이 완료 되셨습니다",False,"center",("",30))
        산융_703호 = 1
        return
      else:
        t.write("사용 중인 강의실입니다",False,"center",("",30))
        return
    if input == "704호":
      if 산융_704호 == 0:
        t.write("입실이 완료 되셨습니다",False,"center",("",30))
        산융_704호 = 1
        return
      else:
        t.write("사용 중인 강의실입니다",False,"center",("",30))
        return
    if input == "705호":
      if 산융_705호 == 0:
        t.write("입실이 완료 되셨습니다",False,"center",("",30))
        산융_705호 = 1
        return
      else:
        t.write("사용 중인 강의실입니다",False,"center",("",30))
        return
    if input == "706호":
      if 산융_706호 == 0:
        t.write("입실이 완료 되셨습니다",False,"center",("",30))
        산융_706호 = 1
        return
      else:
        t.write("사용 중인 강의실입니다",False,"center",("",30))
        return
    if input == "707호":
      if 산융_707호 == 0:
        t.write("입실이 완료 되셨습니다",False,"center",("",30))
        산융_707호 = 1
        return
      else:
        t.write("사용 중인 강의실입니다",False,"center",("",30))
        return
    if input == "708호":
      if 산융_708호 == 0:
        t.write("입실이 완료 되셨습니다",False,"center",("",30))
        산융_708호 = 1
        return
      else:
        t.write("사용 중인 강의실입니다",False,"center",("",30))
        return


        
  elif t.frist_input == "퇴실":
    input = t.strinput("","퇴실하실 강의실을 입력해주세요")
    if input == "701호":
      if 산융_701호 == 0:
        t.write("빈 강의실입니다. 다시 입력해주세요")
        return
      else:
        t.write("퇴실이 완료 되셨습니다",False,"center",("",30))
        산융_701호 = 0
        return
    if input == "702호":
      if 산융_702호 == 0:
        t.write("빈 강의실입니다. 다시 입력해주세요")
        return
      else:
        t.write("퇴실이 완료 되셨습니다",False,"center",("",30))
        산융_702호 = 0
        return
    if input == "703호":
      if 산융_703호 == 0:
        t.write("빈 강의실입니다. 다시 입력해주세요")
        return
      else:
        t.write("퇴실이 완료 되셨습니다",False,"center",("",30))
        산융_703호 = 0
        return
    if input == "704호":
      if 산융_704호 == 0:
        t.write("빈 강의실입니다. 다시 입력해주세요")
        return
      else:
        t.write("퇴실이 완료 되셨습니다",False,"center",("",30))
        산융_704호 = 0
        return
    if input == "705호":
      if 산융_705호 == 0:
        t.write("빈 강의실입니다. 다시 입력해주세요")
        return
      else:
        t.write("퇴실이 완료 되셨습니다",False,"center",("",30))
        산융_705호 = 0
        return
    if input == "706호":
      if 산융_706호 == 0:
        t.write("빈 강의실입니다. 다시 입력해주세요")
        return
      else:
        t.write("퇴실이 완료 되셨습니다",False,"center",("",30))
        산융_706호 = 0
        return
    if input == "707호":
      if 산융_707호 == 0:
        t.write("빈 강의실입니다. 다시 입력해주세요")
        return
      else:
        t.write("퇴실이 완료 되셨습니다",False,"center",("",30))
        산융_707호 = 0
        return
    if input == "708호":
      if 산융_708호 == 0:
        t.write("빈 강의실입니다. 다시 입력해주세요")
        return
      else:
        t.write("퇴실이 완료 되셨습니다",False,"center",("",30))
        산융_708호 = 0
        return
    

        
  elif t.frist_input == "예약":
    input = t.strinput("","예약하실 강의실을 입력해주세요")
    if input == "701호":
      if 산융_701호 == 0:
        t.write("예약이 완료 되셨습니다",False,"center",("",30))
        산융_701호= 1
        return
      else:
        t.write("사용 중인 강의실입니다",False,"center",("",30))
        return
    if input == "702호":
      if 산융_702호 == 0:
        t.write("예약이 완료 되셨습니다",False,"center",("",30))
        산융_702호= 1
        return
      else:
        t.write("사용 중인 강의실입니다",False,"center",("",30))
        return
    if input == "703호":
      if 산융_703호 == 0:
        t.write("예약이 완료 되셨습니다",False,"center",("",30))
        산융_703호= 1
        return
      else:
        t.write("사용 중인 강의실입니다",False,"center",("",30))
        return
    if input == "704호":
      if 산융_704호 == 0:
        t.write("예약이 완료 되셨습니다",False,"center",("",30))
        산융_704호= 1
        return
      else:
        t.write("사용 중인 강의실입니다",False,"center",("",30))
        return
    if input == "705호":
      if 산융_705호 == 0:
        t.write("예약이 완료 되셨습니다",False,"center",("",30))
        산융_705호= 1
        return
      else:
        t.write("사용 중인 강의실입니다",False,"center",("",30))
        return
    if input == "706호":
      if 산융_706호 == 0:
        t.write("예약이 완료 되셨습니다",False,"center",("",30))
        산융_706호= 1
        return
      else:
        t.write("사용 중인 강의실입니다",False,"center",("",30))
        return
    if input == "707호":
      if 산융_707호 == 0:
        t.write("예약이 완료 되셨습니다",False,"center",("",30))
        산융_707호= 1
        return
      else:
        t.write("사용 중인 강의실입니다",False,"center",("",30))
        return
    if input == "708호":
      if 산융_708호 == 0:
        t.write("예약이 완료 되셨습니다",False,"center",("",30))
        산융_708호= 1
        return
      else:
        t.write("사용 중인 강의실입니다",False,"center",("",30))
        return

def 산학융합관_6floor(x,y):
  t.shape(산학융합관_6층)
def 산학융합관_5floor(x,y):
  t.shape(산학융합관_5층)
def 산학융합관_4floor(x,y):
  t.shape(산학융합관_4층)
def 산학융합관_3floor(x,y):
  t.shape(산학융합관_3층)
def 산학융합관_2floor(x,y):
  t.shape(산학융합관_2층)



# 실제 실행 코드들
# 첫 화면// 가운데 학교 로고와 바로 밑에 한국 공학 대학교라는 문구를 출력시켜 주고 작은 글씨로 아무 곳이나 클릭해주세요를 출력시킨다.
t.ht()
t.up()
t.shape(첫_화면)
t.write("아무 곳이나 클릭해주세요",False,"center",("",10))
t.onscreenclick(first_screen,1)
