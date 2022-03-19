# pythonStudy

## 파일 입출력

### 파일 열기모드
|파일 열기모드|의미|
|:------------:|:---:|
|'w'|파일에 내용을 새로 쓸 때 사용|
|'r'|파일 내용을 읽을때 사용|
|'a'|파일에 내용을 추가할 때 사용|





### round함수
```
round(반올림할 숫자, 표시할 소수점 자릿수)
round(반올림할 숫자)
```
- round(37.666666666666664, 1) = 37.7
- round((50 + 45 + 33 + 39 + 29 + 30) / 6, 1) = 37.7

- round(4/3) = 1

### 향상for문
```
for 변수 in 리스트(또는 튜플이나 문자열):       # '변수'에 대입할 원소를 '리스트'에서 하나씩 가져옵니다
  수행할 문장                                  # 변수에 원소를 하나씩 대입할 때마다 문장을 수행합니다
```

### range함수
```
range(숫자)
range(시작할 숫자, 끝날 숫자)
```
- range(10) = 0~9
- range(2, 20) = 2~19

### print 형식지정자
```
print('%d를 포함한 출력 내용' %%d에 넣을 숫자
print('%d, %d를 포함한 출력 내용' %(%d, %d에 넣을 숫자)
```
- print('%d' %5) == 5
- print('%d X %d = %d ' %(5, 4, 5*4) == 5 X 4 = 20


















# cmd

## 오토마우스를 활용한 웹페이지 자동화
```
pip install pyautogui # 마우스와 키보드를 자동으로 제어하는 라이브러리

pip install pyperclip # 클립보드에 값을 복사하거나 붙여넣기 용도
```
#### 오토마우스 라이브러리 기능
```
pyautogui.position() : 마우스의 좌표를 입력받습니다.

pyautogui.moveTo(x,y) : x,y의 좌표로 이동합니다. 절대 좌표입니다.

pyautogui.miveTo(x,y,시간) : x,y의 좌표로 지정된 시간동안 이동합니다.

pyautogui.moveRel(x,y) : 현재 마우스 위치로 부터 x,y픽셀만큼이동합니다

pyautogui.click() : 현재 마우스 커서위치에 마우스를 클릭합니다.

pyautogui.doubleClick() : 현재 마우스 커서 위치에 마우스를 더블클릭합니다.

pyautogui.click(50,50) : 50,50의 위치에 마우스를 클릭합니다.

pyautogui.click(x=50, y=50) : x=50, y=50의 위치에 마우스를 우클릭합니다.

pyautogui.rightClick() : 현재 마우스 커서 위치에 마우스를 우클릭합니다.

pyautogui.dragTo(x=50, y=50, duratio=2) : 현재 마우스 위치부터 50,50좌표까지 2초동안 드래그합니다

pyautogui.typewrite("ABC") : ABC를 입력합니다. 한글은 지원되지 않습니다. 한글은 pyperclip라이브러리를 이용하여 붙여넣기를 통해 입력합니다.

pyautogui.typewrite("ABC", interval=1) : 1초동안 ABC를 입력합니다.

pyautogui.hotkey("ctrl", "V") : hotkey를 이용하여 두개의 키를 동시에 누를수있습니다. [Ctrl + V]를 입력합니다.

pyautogui.screenshot('저장경로', region=(100,100,50,50)) : screenshot을 이용하여 부분캡쳐를 할 수 있습니다. region=(x좌표, y좌표, 가로사이즈, 세로사이즈)입니다.

```
