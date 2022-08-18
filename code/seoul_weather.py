# 오토마우스를 활용한 웹페이지 자동화

import pyautogui
import time
import pyperclip


pyautogui.moveTo(1116, 110, 0.2)
pyautogui.click()
time.sleep(0.5)

pyperclip.copy("서울날씨")
pyautogui.hotkey("ctrl", "v")
time.sleep(0.5)

pyautogui.write(["enter"])
time.sleep(1)

start_x = 1002
start_y = 326
end_x = 1647
end_y = 632


pyautogui.screenshot("서울날씨.png", region=(start_x, start_y, end_x-start_x, end_y-start_y))
