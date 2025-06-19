import os
import requests
import numpy as np
from time import sleep
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


# 1. .envファイルの中身を読み込む
load_dotenv()
MAIL_ADDRESS = os.getenv("MAIL_ADDRESS")
PASSWORD = os.getenv("PASSWORD")



# 2. Chromeを自動で用意して起動する（ヘッドレス）
options = Options()
options.add_argument('--headless')  # ウィンドウなしで実行
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')  # Linux系での安定動作のため
options.add_argument('--disable-gpu')  # GPU使わない
options.add_argument('--window-size=1920x1080')  # 一部サイトで必要なことがある

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 3. ログインしたいページを開く（ここはpaizaのログインページURLに変えてね）
driver.get("https://paiza.jp/login")

# 4. ページが開くまでちょっと待つ（必要に応じて長くしてね）
sleep(2)

# 5. メールアドレス入力欄をクラス名で見つけてメールを入力
email_box = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
email_box.send_keys(MAIL_ADDRESS)

# 6. パスワード入力欄をクラス名で見つけてパスワードを入力
password_box = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
password_box.send_keys(PASSWORD)

# 7. ログインボタンを押す（ボタンのセレクターはサイトに合わせて変えてね）
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

# 8. ログイン後の処理までちょっと待つ
sleep(5)

driver.get("https://paiza.jp/challenges/ranks/c")

sleep(5)

# アクセスするURL # 例のURL。実際にそのリンクがあるページにすること！
url = "https://paiza.jp/challenges/ranks/c"


# Seleniumで今表示されているページのHTMLを取得
html = driver.page_source

# BeautifulSoupでHTMLを読み込む
soup = BeautifulSoup(html, "html.parser")

sleep(5)

# ターゲットのクラスのaタグをすべて取得
link_tags = soup.find_all("a", class_="problem-box__header__title js_tracking_algorithm")

# ベースURL（相対リンクに使う）
base_url = "https://paiza.jp"

sleep(5)

question =[]

# 結果を表示
for tag in link_tags:
    href = tag.get("href")
    text = tag.text.strip()

    # 完全なURLにする
    full_url = base_url + href
    title = "タイトル" + text

    question.append((full_url, text))

    # print("URL:", full_url)
    # print("タイトル:", text)
    # print("------")

# ここでリストを全て取り出す
# for i in range(len(question)):
#     print(question[i])

# randaomに問題を選ぶ
random_index = np.random.randint(0, len(question))

# 選ばれた問題のURLとタイトルを取得
selected_url, selected_title = question[random_index]


print(f"問題のタイトル: {selected_title}")
print(f"問題のURL: {selected_url}")


# ブラウザを閉じる
driver.quit()