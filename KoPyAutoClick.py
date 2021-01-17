from pyautogui import size, confirm, prompt, rightClick, click
from keyboard import is_pressed
screenWidth, screenHeight = size()

print(screenWidth, screenHeight)
lr = 'l'
while True:
    check = confirm(
        text=f'컴퓨터의 모니터 사이즈 : {screenWidth} X {screenHeight}\nf7을 눌러 종료할 수 있습니다.\n설정을 누르면 좌클릭/우클릭을 변경할 수 있습니다.\n시작하시겠습니까?',
        title='시작하기', buttons=['아니요', "예", "설정"])
    if check == "아니요":
        quit()
    elif check == "설정":
        lrc = prompt(
            text='밑에 입력창에 \'좌클릭/우클릭\' 이라고 입력해주세요.\n좌클릭 우클릭 외의 것이 들어오면 좌클릭으로 설정됩니다.')
        lr = 'r' if lrc == '우클릭' else 'l'
    else:
        break

while True:
    if lr == 'r':
        rightClick()
    else:
        click()
    if is_pressed('f7'):
        ask = confirm(text="정말 종료하시겠습니까?",
                      title="종료", buttons=['아니요', '예'])
        if ask == "예":
            quit()
