from selenium import webdriver
from selenium.webdriver.edge.options import Options
import os
os.chdir("C:/Users/%USERNAME%/Desktop/images")
Options = Options()
Options.add_argument("headless")
driver = webdriver.Edge(executable_path=r"EDIT HERE WITH EDGE WEBDRIVER", options=Options)

global url
global counter
global page
global num
counter = 1
page = 1
num = page
url = 'URL FOR RULE34.XXX'
driver.get(url)
driver.find_element("xpath",'/html/body/div[6]/div/div[2]/div[2]/div/form/input[1]').send_keys(str(page))
driver.find_element("xpath",'/html/body/div[6]/div/div[2]/div[2]/div/form/input[2]').click()
url = driver.current_url

def set(counter,test):
    for i in range(1,43):
        print("element:"+str(i)+" " +"TOTAL IMAGES UNTIL NOW: "+str(counter) +" "+"page: ", test)
        driver.get(url)
        xpath= '/html/body/div[6]/div/div[2]/div[1]/span['+str(i)+']/a/img'
        print(xpath)
        xpathimg = '//*[@id="image"]'
        xpathvid = '//*[@id="gelcomVideoPlayer"]'
        driver.find_element("xpath",xpath).click()
        try:
            driver.find_element("xpath",xpathimg).get_attribute('src')
            img = driver.find_element("xpath",xpathimg).get_attribute('src')
            driver.get(img)
            driver.save_screenshot('images'+str(counter)+"page"+str(page)+'.png')
            counter = counter + 1
        except:
            print("video skipped")
            driver.get(url)
while True:
    set(counter,page)
    page = page + 1
    driver.get(url)
    driver.find_element("xpath",'/html/body/div[6]/div/div[2]/div[2]/div/form/input[1]').send_keys(str(page))
    driver.find_element("xpath",'/html/body/div[6]/div/div[2]/div[2]/div/form/input[2]').click()
    url = driver.current_url
    