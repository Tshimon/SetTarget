from selenium import webdriver
import time

from selenium.webdriver.common.by import By

# ChromeDriverを立ち上げる
driver = webdriver.Chrome()

# SBI証券のページを表示
url = "https://www.sbisec.co.jp/ETGate"
driver.get(url)
time.sleep(3)

# ログイン
username_value = "Z64-0673471" # 任意の値を設定してください
password_value = "Jyakkujr12" # 任意の値を設定してください

username = driver.find_element(By.NAME, "user_id")
username.send_keys(username_value)
time.sleep(0.2)

password = driver.find_element(By.NAME, "user_password")
password.send_keys(password_value)
time.sleep(0.2)

driver.find_element(By.NAME,"ACT_login").click()
time.sleep(1)

# 取引を開く
driver.find_element(By.CSS_SELECTOR, "img[title=取引]").click()
time.sleep(1)



# 取引タイプ
trade_type_dict = {
    "現物買": "genK",
    "現物売": "genU",
    "信用新規買": "shinK",
    "信用新規売": "shinU",
}

#　取引： 現物買 現物売
trade_type = "現物買"
driver.find_element(By.ID,trade_type_dict.get(trade_type)).click()
time.sleep(1)

#　証券コード 銘柄コード：
stockcode_value = "7203"
stockcode = driver.find_element(By.NAME, "stock_sec_code")
stockcode.send_keys(stockcode_value)
time.sleep(0.2)

#　株数 ：
quantity_value = "0"
quantity = driver.find_element(By.NAME, "input_quantity")
quantity.send_keys(quantity_value)
time.sleep(0.2)

# period 期間 ：
period_type_dict = {
    "当日中": 0,
    "今週中": 1,
    "期間指定": 2
}

period_type = "期間指定"
driver.find_elements(By.NAME,"selected_limit_in")[period_type_dict.get(period_type)].click()
time.sleep(1)

# 価格の指定　価格 ：
price_type_dict = {
    "指値": 0,
    "成行": 1,
    "逆指値": 2
}

price_type = "成行"
driver.find_elements(By.NAME,"in_sasinari_kbn")[price_type_dict.get(price_type)].click()
time.sleep(1)

# 預り区分 ：
deposit_type_dict = {
    "一般預り": 0,
    "NISA預り": 1,
    "旧NISA預り": 2
}

deposit_type = "NISA預り"
driver.find_elements(By.NAME,"hitokutei_trade_kbn")[deposit_type_dict.get(deposit_type)].click()
time.sleep(1)

# 取引パスワード
trade_password_value = "Jyakkujr12" # 任意の値を設定してください

trade_password = driver.find_element(By.ID, "pwd3")
trade_password.send_keys(trade_password_value)
time.sleep(1)

# 注文画面を省略
driver.find_element(By.ID,"shouryaku").click()
time.sleep(1)

# 注文発注をクリック
driver.find_element(By.CSS_SELECTOR,"img[title=注文発注]").click()
time.sleep(10)



