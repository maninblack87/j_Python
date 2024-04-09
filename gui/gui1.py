from tkinter import *



# 함수 정의 #####################################

# 입력하면 출력하는 함수
# >> ipt는 엔트리
# >> opt는 레이블
def update_label(ipt, opt):
    opt.config(text=ipt.get())

########################## (종료) 함수 정의 ######



# 윈도우 창 정의 #################################
window = Tk()
window.title("GUI 테스트")
window.geometry("500x400")
########################### (종료) 윈도우 창 정의 #



# 구성 요소 정의 ##################################
ipt_myname = Entry(window)
show_myname = Label(window)
confirm_myname = Button(window, text="확인", command=lambda: update_label(ipt_myname, show_myname))
########################### (종료) 구성 요소 정의 #



# 구성 요소 배치 ###################################
ipt_myname.pack()
show_myname.pack()
confirm_myname.pack()
########################### (종료) 구성 요소 배치 ##



# 애플리케이션 이벤트 루프 시작 ######################
window.mainloop()
#################### (종료) 애플리케이션 이벤트 루프 #