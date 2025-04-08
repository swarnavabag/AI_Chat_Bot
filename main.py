import pyautogui
import pyperclip
import time
import ai_assistance

def is_last_message_not_from_swarnava(chat_text: str) -> bool:
    """
    Returns True if the last message is NOT from Swarnava Bag.
    """
    lines = [line.strip() for line in chat_text.strip().splitlines() if line.strip()]
    if not lines:
        return False

    last_message = lines[-1]
   
    try:
        name_part = last_message.split("]")[1].strip()
        sender_name = name_part.split(":")[0].strip()
        return sender_name.lower() != "swarnava bag".lower()
    except IndexError:
        return False
    
print("Starting...")
time.sleep(1.4)

pyautogui.moveTo(730, 1055, duration=0.5)

while True:
    pyautogui.click()
    time.sleep(1)

    pyautogui.moveTo(663,111)
    pyautogui.dragTo(1900, 960, duration=1,button='left')

    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)

    pyautogui.moveTo(1275,514, duration=0.5)

    pyautogui.click()
    time.sleep(0.3)

    copied_text = pyperclip.paste()

    print(copied_text)
    
    if is_last_message_not_from_swarnava(copied_text)==False:
        answer=ai_assistance.get_ai_reply(copied_text)
        print(answer)
        pyautogui.moveTo(755, 1000, duration=0.5)
        pyautogui.click()
        time.sleep(0.3)

        pyperclip.copy(answer)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.2)
        pyautogui.press('enter')
