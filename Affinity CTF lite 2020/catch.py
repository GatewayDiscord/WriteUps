from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import cv2
from PIL import Image, ImageEnhance
import pyperclip
import pytesseract
import numpy as np
import base64

driver=webdriver.Chrome(executable_path="/home/elliot/ctfs/chromedriver")

while True:
    driver.get("http://web4.affinityctf.com/")


    while True:
        image=driver.find_element_by_xpath("/html/body/div[6]/img")
        src=image.get_attribute('src')
        if src!="":
            break

    src_bytes=bytes(src[22:],'utf-8')

#print(src_bytes)

    with open('saved.png','wb') as fh:
        fh.write(base64.decodebytes(src_bytes))

    filename="/home/elliot/ctfs/saved.png"
    im=Image.open(filename)
    enhancer=ImageEnhance.Sharpness(im)
    factor=2
    im_1=enhancer.enhance(factor)
    im_1.save("saved_enhanced.png")
    im_1=cv2.imread('saved_enhanced.png')
    im_gray=cv2.cvtColor(im_1, cv2.COLOR_BGR2GRAY)
    th, im_gray_=cv2.threshold(im_gray, 128, 192, cv2.THRESH_OTSU)
    im=Image.open('saved_nowgood.png')
    e=ImageEnhance.Sharpness(im)
    im_1=enhancer.enhance(0.1)
    im_1.save('saved_nowgood.png')
    #binarisation

    #noise filter


    img1=np.array(Image.open("saved_nowgood.png"))
    text=pytesseract.image_to_string(img1)
    text=text.replace(" ",'').replace('¢','c').replace('O','0').replace('o','0').replace('l','1').replace('S','8').replace('@','9').replace('?','').replace('h','b').replace('A','4')
    print(text)
    box=driver.find_element_by_xpath('/html/body/div[7]/form/input[1]')
    box.click()
    box.send_keys(f"{text}\n")
    input()

