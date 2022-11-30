#초깃 값
room_701 = 0
room_702 = 0
room_703 = 0
room_704 = 0
room_705 = 0
room_706 = 0
room_707 = 0
room_708 = 0


# 함수 정의해주기
#입실
def in_room():
    global room_701
    global room_702
    global room_703
    global room_704
    global room_705
    global room_706
    global room_707
    global room_708
    global room_709
    print("사용할 강의실을 입력하세요 ")
    print("")
    in_room = input("")
    print("")
    if in_room in "701":
        if room_701 == 0:
            print("사용 가능한 강의실입니다! ")
            print("")
            room_701 = 1
            return
        else:
            print("사용 중인 강의실입니다.")
            print("")
    if in_room in "702":
        if room_702 == 0:
            print("사용 가능한 강의실입니다! ")
            print("")
            room_702 = 1
            return
        else:
            print("사용 중인 강의실입니다.")
            print("")
    if in_room in "703":
        if room_703 == 0:
            print("사용 가능한 강의실입니다! ")
            print("")
            room_703 = 1
            return
        else:
            print("사용 중인 강의실입니다.")
            print("")
    if in_room in "704":
        if room_704 == 0:
            print("사용 가능한 강의실입니다! ")
            print("")
            room_704 = 1
            return
    else:
        print("사용 중인 강의실입니다.")
        print("")
    if in_room in "705":
        if room_705 == 0:
            print("사용 가능한 강의실입니다! ")
            print("")
            room_705 = 1
            return
        else:
            print("사용 중인 강의실입니다.")
            print("")
    if in_room in "706":
        if room_706 == 0:
            print("사용 가능한 강의실입니다! ")
            print("")
            room_706 = 1
            return
        else:
            print("사용 중인 강의실입니다.")
            print("")
    if in_room in "707":
        if room_707 == 0:
            print("사용 가능한 강의실입니다! ")
            print("")
            room_707 = 1
        else:
            print("사용 중인 강의실입니다.")
            print("")
    if in_room in "708":
        if room_708 == 0:
            print("사용 가능한 강의실입니다! ")
            print("")
            room_708 = 1
        else:
            print("사용 중인 강의실입니다.")
            print("")


# 퇴실
def out_room():
    global room_701
    global room_702
    global room_703
    global room_704
    global room_705
    global room_706
    global room_707
    global room_708
    global room_709
    print("")
    print("퇴실할 강의실을 입력해주세요.")
    print("")
    out_room = input("")
    print("")
    if out_room in "701":
        if room_701 == 1:
            print("")
            print("퇴실이 완료 되셨습니다")
            print("")
            room_701 = 0
        else:
            print("빈 강의실입니다 ")
            print("")
    if out_room in "702":
        if room_702 == 1:
            print("퇴실이 완료 되셨습니다")
            print("")
            room_702 = 0
        else:
            print("빈 강의실입니다 ")
            print("")
    if out_room in "703":
        if room_703 == 1:
            print("퇴실이 완료 되셨습니다")
            print("")
            room_703 = 0
        else:
            print("빈 강의실입니다 ")
            print("")
    if out_room in "704":
        if room_704 == 1:
            print("퇴실이 완료 되셨습니다")
            print("")
            room_704 = 0
        else:
            print("빈 강의실입니다 ")
            print("")
    if out_room in "705":
        if room_705 == 1:
            print("퇴실이 완료 되셨습니다")
            print("")
            room_705 = 0
        else:
            print("빈 강의실입니다 ")
            print("")
    if out_room in "706":
        if room_706 == 1:
            print("퇴실이 완료 되셨습니다")
            print("")
            room_706 = 0
        else:
            print("빈 강의실입니다 ")
            print("")
    if out_room in "707":
        if room_707 == 1:
            print("퇴실이 완료 되셨습니다")
            print("")
            room_707 = 0
        else:
            print("빈 강의실입니다 ")
            print("")
    if out_room in "708":
        if room_708 == 1:
            print("퇴실이 완료 되셨습니다")
            print("")
            room_708 = 0
        else:
            print("빈 강의실입니다 ")
            print("")


#예약
def ready_room():
    global room_701
    global room_702
    global room_703
    global room_704
    global room_705
    global room_706
    global room_707
    global room_708
    global room_709
    print("")
    print("예약할 강의실을 입력해주세요.")
    print("")
    ready_room = input("")
    print("")
    if ready_room in "701":
        if room_701 == 0:
            print("")
            print("예약이 완료 되셨습니다")
            print("")
            room_701 = 1
        else:
            print("사용중인 강의실입니다. ")
            print("")
    if ready_room in "702":
        if room_702 == 0:
            print("예약이 완료 되셨습니다")
            print("")
            room_702 = 1
        else:
            print("사용중인 강의실입니다. ")
            print("")
    if ready_room in "703":
        if room_703 == 0:
            print("예약이 완료 되셨습니다")
            print("")
            room_703 = 1
        else:
            print("사용중인 강의실입니다. ")
            print("")
    if ready_room in "704":
        if room_704 == 0:
            print("예약이 완료 되셨습니다")
            print("")
            room_704 = 1
        else:
            print("사용중인 강의실입니다. ")
            print("")
    if ready_room in "705":
        if room_705 == 0:
            print("예약이 완료 되셨습니다")
            print("")
            room_705 = 1
        else:
            print("사용중인 강의실입니다. ")
            print("")
    if ready_room in "706":
        if room_706 == 0:
            print("예약이 완료 되셨습니다")
            print("")
            room_706 = 1
        else:
            print("사용중인 강의실입니다. ")
            print("")
    if ready_room in "707":
        if room_707 == 0:
            print("예약이 완료 되셨습니다")
            print("")
            room_707 = 1
        else:
            print("사용중인 강의실입니다. ")
            print("")
    if ready_room in "708":
        if room_708 == 0:
            print("예약이 완료 되셨습니다")
            print("")
            room_708 = 1
        else:
            print("사용중인 강의실입니다. ")
            print("")


print("빈 강의실을 찾아주는 어플입니다.")
print("")
while True:
    print("입실, 퇴실, 예약 중 무엇을 선택하시겠습니까?")
    print("")
    input_room = input("")
    print("")
    if input_room == "입실":
        in_room()
    if input_room == "퇴실":
        out_room()
    if input_room == "예약":
        ready_room()
