from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

load_dotenv()


EMAIL=os.environ.get("EMAIL_ADD")


TWITTER_PASSWORD=EMAIL=os.environ.get("TWITTER_PASS")
TWITTER_NAME=os.environ.get("TWITTER_ID")
chrome_option=webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_option)
driver.get("https://www.thehindu.com/news/cities/puducherry/?page=1")

news={}
news_link=[]
scroll=1600
div=1

while True:
    driver.execute_script(f"window.scrollTo(0, {scroll})")
    time.sleep(3)
    head_lines=driver.find_element(By.XPATH,value=f"/html/body/section[3]/div/div[2]/div[2]/div[{div}]/div/h3")
    # head_line=[i.text for i in head_lines]
    news[head_lines.text]=str(head_lines.get_attribute('innerHTML')).split()[1].split('"')[1]
    print(news)
    if div==3:
        break
    div+=1
    scroll+=70

print(news)


driver.get('https://x.com/i/flow/login')
time.sleep(20)
user_input=driver.find_element(By.XPATH,value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
user_input.send_keys(EMAIL,Keys.ENTER)
time.sleep(7)

pass_input=driver.find_element(By.XPATH,value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
pass_input.send_keys(TWITTER_PASSWORD,Keys.ENTER)

time.sleep(30)

tweet=driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
tweet.send_keys('Todays Top 3 HeadLine of Puducherry',Keys.ENTER)

for i in news:
    time.sleep(1)
    tweet.send_keys(f'{i} : {news[i]}',Keys.ENTER)
    
time.sleep(2)
post_click=driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span')
post_click.click()
time.sleep(2)
driver.quit()




