from tkinter import *
import time
# 기초 설정
window = Tk()
canvas = Canvas(window, width = 1600,height= 1600,bg ="white")
canvas.pack()
# 이미지 설정
first = PhotoImage(file="0.png")
first_1 = PhotoImage(file="1.png")
first_2 = PhotoImage(file="2.png")
first_3 = PhotoImage(file="3.png")
first_4 = PhotoImage(file="4.png")
first_5 = PhotoImage(file="5.png")
first_6 = PhotoImage(file="6.png")
first_7 = PhotoImage(file="7.png")
# 강의실들 0으로 초기화 시켜주기.

#
ho201 = 0



# 첫 시작, 첫 화면을 띄운 뒤에 버튼을 놓거나, 딜레이를 건 뒤 fist_screen으로 가게끔한다.
canvas.create_image(300,300,image=fisrt)
canvas.create_text(300,500,text="잠시만 기다려 주세요.")
time.sleep(10)
button_1 = Button(window,text=("들어가기"),command = first_screen())

# 함수 정의하기
# 첫 번째 함수 = 학교 건물 위치를 알려주는 사진을 띄운다. 쉬운 방법으로 10초를 딜레이 시킨 뒤 어떤 건물을 사용할 것인지 물어본다. 다른 방법으론 버튼을 넣어서 누르면 어떤 건물을 사용할 것인지 물어보는 방법도 있다.
  
def fist_screen():
  canvas.create_image(300,300,image=학교_건물_지도)
  canvas.create_text(300,500,text = ("선택하실 건물을 고르세요."))
  #버튼 위치 정하는 거 알아야 됨.-> button.place(x=,y=)사용.
  qw = Button(window, text = "A동", command = A())
  qw.place(x =300, y=100)
  er = Button(window, text = "B동", command = B())
  er.place(x =300, y=200)
  ty = Button(window, text = "C동", command = C())
  ty.place(x =300, y=300)
  ui = Button(window, text = "D동", command = D())
  ui.place(x =300, y=400)
  op = Button(window, text = "E동", command = E())
  op.place(x =300, y=500)
  ass = Button(window, text = ("산학융합관"), command = F())
  ass.place(x =300, y=600)
def A():
  pass
def B():
  pass
def C():
  pass
def D():
  pass
def E():
  pass
def F():
  canvas.create_image(300,300,image = first_1)
  canvas.create_text(300,500,text = ("선택하실 층을 고르세요."),fill="white")
  df = Button(window, text = "산학융합관 2층", command = floor2())
  df.place(x =100, y=100)
  gh = Button(window, text = "산학융합관 3층", command = floor3())
  gh.place(x =100, y=200)
  jk = Button(window, text = "산학융합관 4층", command = floor4())
  jk.place(x =100, y=300)
  lz = Button(window, text = "산학융합관 5층", command = floor5())
  lz.place(x =100, y=400)
  xc = Button(window, text = "산학융합관 6층", command = floor6())
  xc.place(x =100, y=500)
  vb = Button(window, text = "산학융합관 7층", command = floor7())
  vb.place(x =100, y=600)
# 각 층의 지도
def floor2():
  canvas.create_image(300,300,image = first_1)
  ee = Button(window, text ="201호",command = floor_choice())
  ee.place(x = 100, y= 100)
# 각 층의 호수
def floor_choice():
  global ho201
  input = Entry(window, width =15)
  input.place(x = 100, y = 100)

  #입실
  if input == "입실":
    if ho201 == 0:
      kk = Label(window,text="입실이 완료 되셨습니다.")
      kk.palce(x =100,y =100)
      ho201 = 1
    elif ho201 == 1:
      qq = Label(window,text ="사용중인 강의실 입니다.")
      qq.palce(x =100, y= 100)
    else :
      ww = Label(window,text ="예약중인 강의실입니다.")
      ww.place(x=100,y=100)
  #퇴실
  elif input == "퇴실":
    if ho201 == 0:
      vv = Label(window,text="퇴실이 완료된 강의실입니다.")
      vv.palce(x =100,y =100)
    elif ho201 == 1:
      gg = Label(window,text ="퇴실이 완료 되셨습니다.")
      gg.palce(x =100, y= 100)
      ho201 = 0
    else :
      tt = Label(window,text ="예약이 취소 되셨습니다.")
      tt.place(x=100,y=100)
      ho201 = 0
  #예약
  elif input == "예약":
    if ho201 == 0:
      bb = Label(window,text="예약이 완료 되셨습니다.")
      bb.palce(x =100,y =100)
      ho201 = 2
    elif ho201 == 1:
      nn = Label(window,text ="사용중인 강의실입니다..")
      nn.palce(x =100, y= 100)
    
    else :
      mm = Label(window,text ="예약 중인 강의실입니다..")
      mm.place(x=100,y=100)

  
  
  
  else:
    pass

# def 산학융합관_3층_지도():
#   canvas.create_image(300,300,image = frist_3)
  
# def 산학융합관_4층_지도():
#   canvas.create_image(300,300,image = frist_4)
  
# def 산학융합관_5층_지도():
#   canvas.create_image(300,300,image = frist_5)
  
# def 산학융합관_6층_지도():
#   canvas.create_image(300,300,image = frist_6)
  
# def 산학융합관_7층_지도():
#   canvas.create_image(300,300,image = frist_7)
  

  
# 산학융합관 2층 지도를 보여주고 왼쪽에 2층부터 7층까지 버튼을 만든다. 버튼을 누르면 해당 층 함수로 이동하게끔 만든다. 그리고 각 강의실마다 버튼을 만들어 각 강의실을 클릭했을 때 입실, 퇴실, 예약중 어떤 것을 할 지 정하게 한다. 


window.mainloop()


