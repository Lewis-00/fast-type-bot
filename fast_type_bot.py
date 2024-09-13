from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import keyboard
import pyautogui

chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://monkeytype.com/")

def main():
    keyboard.wait("enter")
    fetch_and_write_text()

    while not keyboard.is_pressed("delete"):
        if keyboard.is_pressed("ctrl+alt+1"):
            fetch_and_write_text()
            
        time.sleep(0.01)  
   
def fetch_and_write_text():
    source = fetch_text()
    text_to_write = get_text_to_write(source)
    write_text(text_to_write)
    return source

def get_text_to_write(source):
    text = ''

    for div in source:
        text += f"{div.text} "
    print(text)
    return text


def write_text(text_to_write: str):
    if text_to_write:
        pyautogui.typewrite(text_to_write, interval=0.028)

def fetch_text():
    return driver.find_elements(By.CSS_SELECTOR, "div.word")

main()
