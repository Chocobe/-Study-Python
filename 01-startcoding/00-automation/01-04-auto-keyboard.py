import pyautogui
import pyperclip

# pyautogui.write('Hello World', interval=0.25)

# pyautogui.hotkey('command', 'c', interval=1)
# pyautogui.press('right', interval=1)
# pyautogui.press('enter', interval=1)
# pyautogui.hotkey('command', 'v', interval=1)

# 한글 입력
pyperclip.copy('한글입력 잘 되나?')
pyautogui.hotkey('command', 'v', interval=1)
