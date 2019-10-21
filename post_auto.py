import time,sys
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from requests import request as rq
from selenium.webdriver import Chrome,ChromeOptions
import chromedriver_binary
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

options = ChromeOptions()
options.add_argument('-headless')

# このコメントをslackのプライベートチャンネルから取得するようにしないとね
# 同時に使う画像をslackのプライベートチャンネルからコンピュータの画像フォルダの一枚目に来るようにしないとね

comment = "セレニウム おテスト"


driver = wd.Chrome()
# urlをリスト化する
url = "https://twitter.com/"

driver.get(url)

# ログイン前処理
driver.find_element_by_xpath('//*[@id="doc"]/div/div[1]/div[1]/div[2]/div[2]/div/a[2]').click()

time.sleep(3)

tw_account = "cyber_humuhumu"
tw_password = "Masa94341564"

# 名前の入力
id = driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input')
id.send_keys(tw_account)

# パスワードの入力
password = driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input')
password.send_keys(tw_password)


#　ログイン処理

driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button').click()


# 投稿

try:
    # time.sleep(2)
    # driver.find_element(By.CLASS_NAME,'DraftEditor-root').click()
    # elem = driver.find_element(By.CLASS_NAME,'public-DraftEditorPlaceholder-root')
    # elem.send_keys(comment)
    # print("success")
    # time.sleep(2)
    # elem.send_keys(Keys.CONTROL, Keys.ENTER)
    autotw1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'DraftEditor-root')))
    autotw1.click()
    element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CLASS_NAME, 'public-DraftEditorPlaceholder-root')))
    ActionChains(driver).move_to_element(element).send_keys(comment).perform()
    # sendTw = 
    if(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.xpath("//span[@data-testid=)))):
        print("OK")
    sendTw.click()

except KeyboardInterrupt:
    print("\n program is ended")
    sys.exit()










