import pyautogui
import time

# print('--- 마우스 자동화 ---')

# 1. 화면 크기 출력
# print(pyautogui.size())

# 2. 마우스 위치 출력
# time.sleep(2) # (js) window.setTimeout(() => 2_000) 같음
# print(pyautogui.position())

# 3. 마우스 이동
# pyautogui.moveTo(33, 333, 2)

# 4. 마우스 클릭
# pyautogui.click()
# pyautogui.click(button='right')
# pyautogui.click(clicks=3, interval=1)

# 5. 마우스 정보
print(pyautogui.position())
pyautogui.moveTo(2156, 52, 2)
pyautogui.mouseDown(button='left')
pyautogui.moveTo(1910, 52, 2)
pyautogui.mouseUp(button='left')
