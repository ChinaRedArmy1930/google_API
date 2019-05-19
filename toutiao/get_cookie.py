import requests
import time 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import  slide_verify 
from io import BytesIO

import  threading



chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')

tmp = "/home/yangxiaoyu/tmp";

browser = webdriver.Chrome(chrome_options=chrome_options);

browser.get("https://sso.toutiao.com/login/?service=https://mp.toutiao.com/sso_confirm/?redirect_url=/")

try:

    ## 点击登陆按钮
    #login = browser.find_element_by_css_selector('body > div > div.carousel > div.page.page-1 > div > img.i3')
    #login.click()
    #time.sleep(3)
    # 填写手机号
    with open(tmp+"/source.txt", 'wb') as f:
        f.write(bytes(browser.page_source,encoding='utf8')) 
    phone = browser.find_element_by_id('user-mobile')
    phone.send_keys('13530918563')
    # 获取验证码
    browser.find_element_by_class_name('get-code').click()
    #此时会弹窗滑动窗口

    time.sleep(3)
    #print(browser.page_source)
    browser.find_element_by_id('validate-big')

    with open(tmp+"/source.txt", 'wb') as f:
        f.write(bytes(browser.page_source,encoding='utf8')) 

    
    #将图片下载到本地
    window_slide =  browser.find_element_by_id('validate-big')
    small_slide  =  browser.find_element_by_class_name('validate-block')
    
    img = requests.get(window_slide.get_attribute("src"))
    with open(tmp+"/img.jpg", 'wb') as f:
        f.write(img.content) 
    
    img_small = requests.get(small_slide.get_attribute("src"))
    with open(tmp+"/img_small.jpg", 'wb') as f2:
        f2.write(img_small.content) 

    
    img_big = slide_verify.get_image(browser, window_slide);


    img_small = slide_verify.get_image(browser, small_slide);




    location = slide_verify.get_distance(img_big, 268,150,img_small);
    print(location)
    '''
    #track_list = get_track(0)



    #print(window_slide.get_attribute("src"))

    #browser.get_screenshot_as_file("D:/test2/滑动验证/img.jpg")#对整个页面截图

    verfiy_code_input = input("请输入验证码:")
    # 验证码输入框
    mobile_code = browser.find_element_by_id('mobile-code')
    mobile_code.send_keys(verfiy_code_input)

    # 登陆
    browser.find_element_by_id('bytedance-SubmitStatic').click()
    time.sleep(5)
    cookies = browser.get_cookies()
    with open('cookies.json', 'w') as f:
        self.cookies = json.loads(f.write(json.dumps(cookies)))
    '''
    #e = threading.Event();
    #e.wait();
finally:
    
    browser.quit();
