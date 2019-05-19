# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import PIL.Image as image
from PIL import Image,ImageEnhance
import time,re, random
import requests
from io import BytesIO
tmp = "/home/yangxiaoyu/tmp";
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

#对比两张图片 找到缺口
def get_distance(image1,image1width,image1height,image2):
    '''
      拿到滑动验证码需要移动的距离
      :param image1:没有缺口的图片对象
      :param image2:带缺口的图片对象
      :return:需要移动的距离
      '''

    threshold = 50
    for i in range(0,image1width):  
        for j in range(0,image1height):  
            pixel1 = image1.getpixel((i,j))
            pixel2 = image2.getpixel((i,j))
            res_R = abs(pixel1[0]-pixel2[0]) # 计算RGB差
            res_G = abs(pixel1[1] - pixel2[1])  # 计算RGB差
            res_B = abs(pixel1[2] - pixel2[2])  # 计算RGB差
            if res_R > threshold and res_G > threshold and res_B > threshold:
                return i  # 需要移动的距离





def merge_image(image_file,location_list):
    """
     拼接图片
    :param image_file:
    :param location_list:
    :return:
    """
    im = Image.open(image_file)
    new_im = Image.new('RGB',(260,116))
    # 把无序的图片 切成52张小图片
    im_list_upper = []
    im_list_down = []
    # print(location_list)
    for location in location_list:
        # print(location['y'])
        if location['y'] == -58: # 上半边
            im_list_upper.append(im.crop((abs(location['x']),58,abs(location['x'])+10,116)))
        if location['y'] == 0:  # 下半边
            im_list_down.append(im.crop((abs(location['x']),0,abs(location['x'])+10,58)))

    x_offset = 0
    for im in im_list_upper:
        new_im.paste(im,(x_offset,0))  # 把小图片放到 新的空白图片上
        x_offset += im.size[0]

    x_offset = 0
    for im in im_list_down:
        new_im.paste(im,(x_offset,58))
        x_offset += im.size[0]
    #new_im.show()
    return new_im

def get_image(driver, img):
    '''
    下载无序的图片  然后进行拼接 获得完整的图片
    :param driver:
    :param img:
    :return:
    '''
    time.sleep(2)

    image_result = requests.get(img.get_attribute("src")).content

    image_file = BytesIO(image_result) # 是一张无序的图片

    with open(tmp+"/btyeio.jpg","wb") as f:
            f.write(image_file.read())

    return image_result
   
