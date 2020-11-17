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
    driver.get("http://web4.affinityctf.com/") #open the site on my browser


    while True:
        image=driver.find_element_by_xpath("/html/body/div[6]/img") #look for the image
        src=image.get_attribute('src') #copy the source of the image
        if src!="": 
            break #if the image source isn't "" (that is nothing. only happened when the image hadn't come yet) it stops the looking again and again
        #else keep looking until the image loads

    src_bytes=bytes(src[22:],'utf-8') #convert the base64 image source into bytes so that i can later save it as an image and process it

#print(src_bytes) --> was for debugging.

    with open('saved.png','wb') as fh:
        fh.write(base64.decodebytes(src_bytes)) #save bytes as an image

    #from here to
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
    #here i just threw together a lot of unnecessary binarisation and sharpening which might have cancelled each other out lmao. it is hot garbage. don't get confused here.

    img1=np.array(Image.open("saved_nowgood.png"))


    text=pytesseract.image_to_string(img1) #finally read the text from the image i processed
    text=text.replace(" ",'').replace('¢','c').replace('O','0').replace('o','0').replace('l','1').replace('S','8').replace('@','9').replace('?','').replace('h','b').replace('A','4') #replace some common fuck up patterns i noticed. this was necessary because the image text always only had hexadecimal in it. I noticed the pattern and thus replaced these when they came as they gave frequent errors

    print(text) #print it once to debug later
    box=driver.find_element_by_xpath('/html/body/div[7]/form/input[1]')
    box.click()
    box.send_keys(f"{text}\n") #find the box, click on it and submit.
    input() #i reviewed the response manually on the browser and clicked enter to repeat the whole process again till i got it right. took me a long time

