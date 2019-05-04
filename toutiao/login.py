import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')

browser = webdriver.Chrome(chrome_options=chrome_options);

browser.get("https://mp.toutiao.com/profile_v3/index")
with open('cookies.json') as f:
    cookies = json.loads(f.read())
for cookie in cookies:
    browser.add_cookie(cookie)


header={"Cookie":"UM_distinctid=16a8125304f122-0d83716317e184-3e385e0c-1fa400-16a812530502dd;"+
"tt_webid=6687027185675044365;"+
"ccid=1548253c4be628ed0a0bc058a0ac4a00;"+
"toutiao_sso_user=328bc5b1e78d1fff8b0a1b857c00000f;"+
"__tea_sdk__ssid=undefined;s_v_web_id=32ed5fc50faad6ac24bcf4e84c2d8b20;"+
"sso_uid_tt=a7c3fefb62c82433a48b6a5c15c85986;"+
"_ga=GA1.2.1217183117.1556955272;"+
"_gid=GA1.2.944236970.1556955272;"+
"install_id=0;sid_tt=2d8d1b62e4fa54edd276a770de2ab973;"+
"sid_guard=2d8d1b62e4fa54edd276a770de2ab973;"+
"sessionid=2d8d1b62e4fa54edd276a770de2ab973;"+
"uid_tt=f6bdd04c0a24df6f2d1ea5f3ece12fb1"};
html=requests.get(url,headers=header)
print(html.text)
