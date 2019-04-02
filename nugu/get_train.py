from selenium import webdriver
import pandas as pd
import numpy as np
import time,datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException


# 역마다 배차가 다르기때문에 그 배차가 제일 긴 숫자를 받아서 긴 숫자를 반환한다
def max_size(test):
    max_num = 0
    for i in range(len(test)):
        if max_num > len(test[i]):
            pass
        elif max_num == len(test[i]):
            pass
        else:
            max_num = len(test[i])

    return max_num


# ktx srt 무궁화 itx-산천 등의 유형을 받는다
def type_train():
    try:
        type_boxes = []
        elem = driver.find_element_by_id('wrap')
        elem = driver.find_element_by_class_name('container-e')
        elem = driver.find_element_by_class_name('sub_wrap')
        elem = driver.find_element_by_class_name('etk-seat')
        elem = driver.find_element_by_id('result-form')

        try:
            elem = driver.find_element_by_class_name('th_thead')
            elem = driver.find_element_by_class_name('etk-seat')
            elem = driver.find_elements_by_class_name('trnGp')
            length = len(elem)
        #             print(length)
        except TypeError:
            length = 0
        #             print(0)
        for i in range(0, len(elem), 1):
            type_box = elem[i].text
            type_boxes.append(type_box)

    except NameError:
        return 0, 0
    except NoSuchElementException:
        return 0, 0
    return type_boxes, length

# 시간을 가져오는 코드
def find_text():
    boxes=[]
    try:
        elem = driver.find_element_by_id('wrap')
        elem = driver.find_element_by_class_name('container-e')
        elem = driver.find_element_by_class_name('sub_wrap')
        elem = driver.find_element_by_class_name('etk-seat')
        elem = driver.find_element_by_id('result-form')
        try:
            elem = driver.find_element_by_class_name('th_thead')
            elem = driver.find_element_by_class_name('etk-seat')
            elem = driver.find_elements_by_class_name('time')
            for i in range(0,len(elem),2):
                box = elem[i].text
                boxes.append(box)
            # 로딩이 빠르면 오류가 발생하기에 코드가 실행하는 cup를 2초 멈추게 만든다
            time.sleep(2)
        except:
            return 0
    except NameError:
            return 0
    except NoSuchElementException:
            return 0
    return boxes


name_box = ["Suseo", "Dongchan", "Jiji", "Cheonan(Asan)", "Osong", "Daejeon", "Gimcheon(Gumi)", "Dongdaegu",
            "ShinKyungju", "Ulsan(Tongdosa)", "Busan", "Gongju", "Iksan", "Jeong-eup", "Gwangju(Songje)", "Naju",
            "Mokpo"]
name_boxs = ["Suseo_h", "Dongchan_h", "Jiji_h", "Cheonan(Asan)_h", "Osong_h", "Daejeon_h", "Gimcheon(Gumi)_h",
             "Dongdaegu_h", "ShinKyungju_h", "Ulsan(Tongdosa)_h", "Busan_h", "Gongju_h", "Iksan_h", "Jeong-eup_h",
             "Gwangju(Songje)_h", "Naju_h", "Mokpo_h",
             "Suseo_m", "Dongchan_m", "Jiji_m", "Cheonan(Asan)_m", "Osong_m", "Daejeon_m", "Gimcheon(Gumi)_m",
             "Dongdaegu_m", "ShinKyungju_m", "Ulsan(Tongdosa)_m", "Busan_m", "Gongju_m", "Iksan_m", "Jeong-eup_m",
             "Gwangju(Songje)_m", "Naju_m", "Mokpo_m"
             ]

while True:
    start = datetime.datetime.now()
    start = start.hour
    # 무조건 자정이 되엇을때 실행해다라
    if start == 0 or start <= 1:
        dic, dicts, dic_type = {}, {}, {}
        dic_1, dicts_1, dic_type_1 = {}, {}, {}
        dic_2, dicts_2, dic_type_2 = {}, {}, {}
        # 오늘 데이터 담을 공간
        box_2_20, box_2_21, box_2_22, box_2_23, box_2_24, box_2_25, box_2_26, box_2_27, box_2_28, box_2_29, box_2_30, box_2_31, box_2_32, box_2_33, box_2_34, box_2_35, box_2_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_3_20, box_3_21, box_3_22, box_3_23, box_3_24, box_3_25, box_3_26, box_3_27, box_3_28, box_3_29, box_3_30, box_3_31, box_3_32, box_3_33, box_3_34, box_3_35, box_3_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_4_20, box_4_21, box_4_22, box_4_23, box_4_24, box_4_25, box_4_26, box_4_27, box_4_28, box_4_29, box_4_30, box_4_31, box_4_32, box_4_33, box_4_34, box_4_35, box_4_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_5_20, box_5_21, box_5_22, box_5_23, box_5_24, box_5_25, box_5_26, box_5_27, box_5_28, box_5_29, box_5_30, box_5_31, box_5_32, box_5_33, box_5_34, box_5_35, box_5_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_6_20, box_6_21, box_6_22, box_6_23, box_6_24, box_6_25, box_6_26, box_6_27, box_6_28, box_6_29, box_6_30, box_6_31, box_6_32, box_6_33, box_6_34, box_6_35, box_6_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_7_20, box_7_21, box_7_22, box_7_23, box_7_24, box_7_25, box_7_26, box_7_27, box_7_28, box_7_29, box_7_30, box_7_31, box_7_32, box_7_33, box_7_34, box_7_35, box_7_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_8_20, box_8_21, box_8_22, box_8_23, box_8_24, box_8_25, box_8_26, box_8_27, box_8_28, box_8_29, box_8_30, box_8_31, box_8_32, box_8_33, box_8_34, box_8_35, box_8_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_9_20, box_9_21, box_9_22, box_9_23, box_9_24, box_9_25, box_9_26, box_9_27, box_9_28, box_9_29, box_9_30, box_9_31, box_9_32, box_9_33, box_9_34, box_9_35, box_9_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_10_20, box_10_21, box_10_22, box_10_23, box_10_24, box_10_25, box_10_26, box_10_27, box_10_28, box_10_29, box_10_30, box_10_31, box_10_32, box_10_33, box_10_34, box_10_35, box_10_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_11_20, box_11_21, box_11_22, box_11_23, box_11_24, box_11_25, box_11_26, box_11_27, box_11_28, box_11_29, box_11_30, box_11_31, box_11_32, box_11_33, box_11_34, box_11_35, box_11_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_12_20, box_12_21, box_12_22, box_12_23, box_12_24, box_12_25, box_12_26, box_12_27, box_12_28, box_12_29, box_12_30, box_12_31, box_12_32, box_12_33, box_12_34, box_12_35, box_12_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_13_20, box_13_21, box_13_22, box_13_23, box_13_24, box_13_25, box_13_26, box_13_27, box_13_28, box_13_29, box_13_30, box_13_31, box_13_32, box_13_33, box_13_34, box_13_35, box_13_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_14_20, box_14_21, box_14_22, box_14_23, box_14_24, box_14_25, box_14_26, box_14_27, box_14_28, box_14_29, box_14_30, box_14_31, box_14_32, box_14_33, box_14_34, box_14_35, box_14_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_15_20, box_15_21, box_15_22, box_15_23, box_15_24, box_15_25, box_15_26, box_15_27, box_15_28, box_15_29, box_15_30, box_15_31, box_15_32, box_15_33, box_15_34, box_15_35, box_15_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_16_20, box_16_21, box_16_22, box_16_23, box_16_24, box_16_25, box_16_26, box_16_27, box_16_28, box_16_29, box_16_30, box_16_31, box_16_32, box_16_33, box_16_34, box_16_35, box_16_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_17_20, box_17_21, box_17_22, box_17_23, box_17_24, box_17_25, box_17_26, box_17_27, box_17_28, box_17_29, box_17_30, box_17_31, box_17_32, box_17_33, box_17_34, box_17_35, box_17_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_18_20, box_18_21, box_18_22, box_18_23, box_18_24, box_18_25, box_18_26, box_18_27, box_18_28, box_18_29, box_18_30, box_18_31, box_18_32, box_18_33, box_18_34, box_18_35, box_18_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []

        big_box = [[box_2_20, box_2_21, box_2_22, box_2_23, box_2_24, box_2_25, box_2_26, box_2_27, box_2_28, box_2_29,
                    box_2_30, box_2_31, box_2_32, box_2_33, box_2_34, box_2_35, box_2_36],
                   [box_3_20, box_3_21, box_3_22, box_3_23, box_3_24, box_3_25, box_3_26, box_3_27, box_3_28, box_3_29,
                    box_3_30, box_3_31, box_3_32, box_3_33, box_3_34, box_3_35, box_3_36],
                   [box_4_20, box_4_21, box_4_22, box_4_23, box_4_24, box_4_25, box_4_26, box_4_27, box_4_28, box_4_29,
                    box_4_30, box_4_31, box_4_32, box_4_33, box_4_34, box_4_35, box_4_36],
                   [box_5_20, box_5_21, box_5_22, box_5_23, box_5_24, box_5_25, box_5_26, box_5_27, box_5_28, box_5_29,
                    box_5_30, box_5_31, box_5_32, box_5_33, box_5_34, box_5_35, box_5_36],
                   [box_6_20, box_6_21, box_6_22, box_6_23, box_6_24, box_6_25, box_6_26, box_6_27, box_6_28, box_6_29,
                    box_6_30, box_6_31, box_6_32, box_6_33, box_6_34, box_6_35, box_6_36],
                   [box_7_20, box_7_21, box_7_22, box_7_23, box_7_24, box_7_25, box_7_26, box_7_27, box_7_28, box_7_29,
                    box_7_30, box_7_31, box_7_32, box_7_33, box_7_34, box_7_35, box_7_36],
                   [box_8_20, box_8_21, box_8_22, box_8_23, box_8_24, box_8_25, box_8_26, box_8_27, box_8_28, box_8_29,
                    box_8_30, box_8_31, box_8_32, box_8_33, box_8_34, box_8_35, box_8_36],
                   [box_9_20, box_9_21, box_9_22, box_9_23, box_9_24, box_9_25, box_9_26, box_9_27, box_9_28, box_9_29,
                    box_9_30, box_9_31, box_9_32, box_9_33, box_9_34, box_9_35, box_9_36],
                   [box_10_20, box_10_21, box_10_22, box_10_23, box_10_24, box_10_25, box_10_26, box_10_27, box_10_28,
                    box_10_29, box_10_30, box_10_31, box_10_32, box_10_33, box_10_34, box_10_35, box_10_36],
                   [box_11_20, box_11_21, box_11_22, box_11_23, box_11_24, box_11_25, box_11_26, box_11_27, box_11_28,
                    box_11_29, box_11_30, box_11_31, box_11_32, box_11_33, box_11_34, box_11_35, box_11_36],
                   [box_12_20, box_12_21, box_12_22, box_12_23, box_12_24, box_12_25, box_12_26, box_12_27, box_12_28,
                    box_12_29, box_12_30, box_12_31, box_12_32, box_12_33, box_12_34, box_12_35, box_12_36],
                   [box_13_20, box_13_21, box_13_22, box_13_23, box_13_24, box_13_25, box_13_26, box_13_27, box_13_28,
                    box_13_29, box_13_30, box_13_31, box_13_32, box_13_33, box_13_34, box_13_35, box_13_36],
                   [box_14_20, box_14_21, box_14_22, box_14_23, box_14_24, box_14_25, box_14_26, box_14_27, box_14_28,
                    box_14_29, box_14_30, box_14_31, box_14_32, box_14_33, box_14_34, box_14_35, box_14_36],
                   [box_15_20, box_15_21, box_15_22, box_15_23, box_15_24, box_15_25, box_15_26, box_15_27, box_15_28,
                    box_15_29, box_15_30, box_15_31, box_15_32, box_15_33, box_15_34, box_15_35, box_15_36],
                   [box_16_20, box_16_21, box_16_22, box_16_23, box_16_24, box_16_25, box_16_26, box_16_27, box_16_28,
                    box_16_29, box_16_30, box_16_31, box_16_32, box_16_33, box_16_34, box_16_35, box_16_36],
                   [box_17_20, box_17_21, box_17_22, box_17_23, box_17_24, box_17_25, box_17_26, box_17_27, box_17_28,
                    box_17_29, box_17_30, box_17_31, box_17_32, box_17_33, box_17_34, box_17_35, box_17_36],
                   [box_18_20, box_18_21, box_18_22, box_18_23, box_18_24, box_18_25, box_18_26, box_18_27, box_18_28,
                    box_18_29, box_18_30, box_18_31, box_18_32, box_18_33, box_18_34, box_18_35, box_18_36]
                   ]

        box_type_2_20, box_type_2_21, box_type_2_22, box_type_2_23, box_type_2_24, box_type_2_25, box_type_2_26, box_type_2_27, box_type_2_28, box_type_2_29, box_type_2_30, box_type_2_31, box_type_2_32, box_type_2_33, box_type_2_34, box_type_2_35, box_type_2_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_type_3_20, box_type_3_21, box_type_3_22, box_type_3_23, box_type_3_24, box_type_3_25, box_type_3_26, box_type_3_27, box_type_3_28, box_type_3_29, box_type_3_30, box_type_3_31, box_type_3_32, box_type_3_33, box_type_3_34, box_type_3_35, box_type_3_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_type_4_20, box_type_4_21, box_type_4_22, box_type_4_23, box_type_4_24, box_type_4_25, box_type_4_26, box_type_4_27, box_type_4_28, box_type_4_29, box_type_4_30, box_type_4_31, box_type_4_32, box_type_4_33, box_type_4_34, box_type_4_35, box_type_4_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_type_5_20, box_type_5_21, box_type_5_22, box_type_5_23, box_type_5_24, box_type_5_25, box_type_5_26, box_type_5_27, box_type_5_28, box_type_5_29, box_type_5_30, box_type_5_31, box_type_5_32, box_type_5_33, box_type_5_34, box_type_5_35, box_type_5_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_type_6_20, box_type_6_21, box_type_6_22, box_type_6_23, box_type_6_24, box_type_6_25, box_type_6_26, box_type_6_27, box_type_6_28, box_type_6_29, box_type_6_30, box_type_6_31, box_type_6_32, box_type_6_33, box_type_6_34, box_type_6_35, box_type_6_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_type_7_20, box_type_7_21, box_type_7_22, box_type_7_23, box_type_7_24, box_type_7_25, box_type_7_26, box_type_7_27, box_type_7_28, box_type_7_29, box_type_7_30, box_type_7_31, box_type_7_32, box_type_7_33, box_type_7_34, box_type_7_35, box_type_7_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_type_8_20, box_type_8_21, box_type_8_22, box_type_8_23, box_type_8_24, box_type_8_25, box_type_8_26, box_type_8_27, box_type_8_28, box_type_8_29, box_type_8_30, box_type_8_31, box_type_8_32, box_type_8_33, box_type_8_34, box_type_8_35, box_type_8_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_type_9_20, box_type_9_21, box_type_9_22, box_type_9_23, box_type_9_24, box_type_9_25, box_type_9_26, box_type_9_27, box_type_9_28, box_type_9_29, box_type_9_30, box_type_9_31, box_type_9_32, box_type_9_33, box_type_9_34, box_type_9_35, box_type_9_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_type_10_20, box_type_10_21, box_type_10_22, box_type_10_23, box_type_10_24, box_type_10_25, box_type_10_26, box_type_10_27, box_type_10_28, box_type_10_29, box_type_10_30, box_type_10_31, box_type_10_32, box_type_10_33, box_type_10_34, box_type_10_35, box_type_10_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_type_11_20, box_type_11_21, box_type_11_22, box_type_11_23, box_type_11_24, box_type_11_25, box_type_11_26, box_type_11_27, box_type_11_28, box_type_11_29, box_type_11_30, box_type_11_31, box_type_11_32, box_type_11_33, box_type_11_34, box_type_11_35, box_type_11_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_type_12_20, box_type_12_21, box_type_12_22, box_type_12_23, box_type_12_24, box_type_12_25, box_type_12_26, box_type_12_27, box_type_12_28, box_type_12_29, box_type_12_30, box_type_12_31, box_type_12_32, box_type_12_33, box_type_12_34, box_type_12_35, box_type_12_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_type_13_20, box_type_13_21, box_type_13_22, box_type_13_23, box_type_13_24, box_type_13_25, box_type_13_26, box_type_13_27, box_type_13_28, box_type_13_29, box_type_13_30, box_type_13_31, box_type_13_32, box_type_13_33, box_type_13_34, box_type_13_35, box_type_13_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_type_14_20, box_type_14_21, box_type_14_22, box_type_14_23, box_type_14_24, box_type_14_25, box_type_14_26, box_type_14_27, box_type_14_28, box_type_14_29, box_type_14_30, box_type_14_31, box_type_14_32, box_type_14_33, box_type_14_34, box_type_14_35, box_type_14_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_type_15_20, box_type_15_21, box_type_15_22, box_type_15_23, box_type_15_24, box_type_15_25, box_type_15_26, box_type_15_27, box_type_15_28, box_type_15_29, box_type_15_30, box_type_15_31, box_type_15_32, box_type_15_33, box_type_15_34, box_type_15_35, box_type_15_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_type_16_20, box_type_16_21, box_type_16_22, box_type_16_23, box_type_16_24, box_type_16_25, box_type_16_26, box_type_16_27, box_type_16_28, box_type_16_29, box_type_16_30, box_type_16_31, box_type_16_32, box_type_16_33, box_type_16_34, box_type_16_35, box_type_16_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_type_17_20, box_type_17_21, box_type_17_22, box_type_17_23, box_type_17_24, box_type_17_25, box_type_17_26, box_type_17_27, box_type_17_28, box_type_17_29, box_type_17_30, box_type_17_31, box_type_17_32, box_type_17_33, box_type_17_34, box_type_17_35, box_type_17_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_type_18_20, box_type_18_21, box_type_18_22, box_type_18_23, box_type_18_24, box_type_18_25, box_type_18_26, box_type_18_27, box_type_18_28, box_type_18_29, box_type_18_30, box_type_18_31, box_type_18_32, box_type_18_33, box_type_18_34, box_type_18_35, box_type_18_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []

        big_type_box = [
            [box_type_2_20, box_type_2_21, box_type_2_22, box_type_2_23, box_type_2_24, box_type_2_25, box_type_2_26,
             box_type_2_27, box_type_2_28, box_type_2_29, box_type_2_30, box_type_2_31, box_type_2_32, box_type_2_33,
             box_type_2_34, box_type_2_35, box_type_2_36],
            [box_type_3_20, box_type_3_21, box_type_3_22, box_type_3_23, box_type_3_24, box_type_3_25, box_type_3_26,
             box_type_3_27, box_type_3_28, box_type_3_29, box_type_3_30, box_type_3_31, box_type_3_32, box_type_3_33,
             box_type_3_34, box_type_3_35, box_type_3_36],
            [box_type_4_20, box_type_4_21, box_type_4_22, box_type_4_23, box_type_4_24, box_type_4_25, box_type_4_26,
             box_type_4_27, box_type_4_28, box_type_4_29, box_type_4_30, box_type_4_31, box_type_4_32, box_type_4_33,
             box_type_4_34, box_type_4_35, box_type_4_36],
            [box_type_5_20, box_type_5_21, box_type_5_22, box_type_5_23, box_type_5_24, box_type_5_25, box_type_5_26,
             box_type_5_27, box_type_5_28, box_type_5_29, box_type_5_30, box_type_5_31, box_type_5_32, box_type_5_33,
             box_type_5_34, box_type_5_35, box_type_5_36],
            [box_type_6_20, box_type_6_21, box_type_6_22, box_type_6_23, box_type_6_24, box_type_6_25, box_type_6_26,
             box_type_6_27, box_type_6_28, box_type_6_29, box_type_6_30, box_type_6_31, box_type_6_32, box_type_6_33,
             box_type_6_34, box_type_6_35, box_type_6_36],
            [box_type_7_20, box_type_7_21, box_type_7_22, box_type_7_23, box_type_7_24, box_type_7_25, box_type_7_26,
             box_type_7_27, box_type_7_28, box_type_7_29, box_type_7_30, box_type_7_31, box_type_7_32, box_type_7_33,
             box_type_7_34, box_type_7_35, box_type_7_36],
            [box_type_8_20, box_type_8_21, box_type_8_22, box_type_8_23, box_type_8_24, box_type_8_25, box_type_8_26,
             box_type_8_27, box_type_8_28, box_type_8_29, box_type_8_30, box_type_8_31, box_type_8_32, box_type_8_33,
             box_type_8_34, box_type_8_35, box_type_8_36],
            [box_type_9_20, box_type_9_21, box_type_9_22, box_type_9_23, box_type_9_24, box_type_9_25, box_type_9_26,
             box_type_9_27, box_type_9_28, box_type_9_29, box_type_9_30, box_type_9_31, box_type_9_32, box_type_9_33,
             box_type_9_34, box_type_9_35, box_type_9_36],
            [box_type_10_20, box_type_10_21, box_type_10_22, box_type_10_23, box_type_10_24, box_type_10_25,
             box_type_10_26, box_type_10_27, box_type_10_28, box_type_10_29, box_type_10_30, box_type_10_31,
             box_type_10_32, box_type_10_33, box_type_10_34, box_type_10_35, box_type_10_36],
            [box_type_11_20, box_type_11_21, box_type_11_22, box_type_11_23, box_type_11_24, box_type_11_25,
             box_type_11_26, box_type_11_27, box_type_11_28, box_type_11_29, box_type_11_30, box_type_11_31,
             box_type_11_32, box_type_11_33, box_type_11_34, box_type_11_35, box_type_11_36],
            [box_type_12_20, box_type_12_21, box_type_12_22, box_type_12_23, box_type_12_24, box_type_12_25,
             box_type_12_26, box_type_12_27, box_type_12_28, box_type_12_29, box_type_12_30, box_type_12_31,
             box_type_12_32, box_type_12_33, box_type_12_34, box_type_12_35, box_type_12_36],
            [box_type_13_20, box_type_13_21, box_type_13_22, box_type_13_23, box_type_13_24, box_type_13_25,
             box_type_13_26, box_type_13_27, box_type_13_28, box_type_13_29, box_type_13_30, box_type_13_31,
             box_type_13_32, box_type_13_33, box_type_13_34, box_type_13_35, box_type_13_36],
            [box_type_14_20, box_type_14_21, box_type_14_22, box_type_14_23, box_type_14_24, box_type_14_25,
             box_type_14_26, box_type_14_27, box_type_14_28, box_type_14_29, box_type_14_30, box_type_14_31,
             box_type_14_32, box_type_14_33, box_type_14_34, box_type_14_35, box_type_14_36],
            [box_type_15_20, box_type_15_21, box_type_15_22, box_type_15_23, box_type_15_24, box_type_15_25,
             box_type_15_26, box_type_15_27, box_type_15_28, box_type_15_29, box_type_15_30, box_type_15_31,
             box_type_15_32, box_type_15_33, box_type_15_34, box_type_15_35, box_type_15_36],
            [box_type_16_20, box_type_16_21, box_type_16_22, box_type_16_23, box_type_16_24, box_type_16_25,
             box_type_16_26, box_type_16_27, box_type_16_28, box_type_16_29, box_type_16_30, box_type_16_31,
             box_type_16_32, box_type_16_33, box_type_16_34, box_type_16_35, box_type_16_36],
            [box_type_17_20, box_type_17_21, box_type_17_22, box_type_17_23, box_type_17_24, box_type_17_25,
             box_type_17_26, box_type_17_27, box_type_17_28, box_type_17_29, box_type_17_30, box_type_17_31,
             box_type_17_32, box_type_17_33, box_type_17_34, box_type_17_35, box_type_17_36],
            [box_type_18_20, box_type_18_21, box_type_18_22, box_type_18_23, box_type_18_24, box_type_18_25,
             box_type_18_26, box_type_18_27, box_type_18_28, box_type_18_29, box_type_18_30, box_type_18_31,
             box_type_18_32, box_type_18_33, box_type_18_34, box_type_18_35, box_type_18_36]
            ]
        # 내일 데이터 담을 공간
        box_1_2_20, box_1_2_21, box_1_2_22, box_1_2_23, box_1_2_24, box_1_2_25, box_1_2_26, box_1_2_27, box_1_2_28, box_1_2_29, box_1_2_30, box_1_2_31, box_1_2_32, box_1_2_33, box_1_2_34, box_1_2_35, box_1_2_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_1_3_20, box_1_3_21, box_1_3_22, box_1_3_23, box_1_3_24, box_1_3_25, box_1_3_26, box_1_3_27, box_1_3_28, box_1_3_29, box_1_3_30, box_1_3_31, box_1_3_32, box_1_3_33, box_1_3_34, box_1_3_35, box_1_3_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_1_4_20, box_1_4_21, box_1_4_22, box_1_4_23, box_1_4_24, box_1_4_25, box_1_4_26, box_1_4_27, box_1_4_28, box_1_4_29, box_1_4_30, box_1_4_31, box_1_4_32, box_1_4_33, box_1_4_34, box_1_4_35, box_1_4_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_1_5_20, box_1_5_21, box_1_5_22, box_1_5_23, box_1_5_24, box_1_5_25, box_1_5_26, box_1_5_27, box_1_5_28, box_1_5_29, box_1_5_30, box_1_5_31, box_1_5_32, box_1_5_33, box_1_5_34, box_1_5_35, box_1_5_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_1_6_20, box_1_6_21, box_1_6_22, box_1_6_23, box_1_6_24, box_1_6_25, box_1_6_26, box_1_6_27, box_1_6_28, box_1_6_29, box_1_6_30, box_1_6_31, box_1_6_32, box_1_6_33, box_1_6_34, box_1_6_35, box_1_6_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_1_7_20, box_1_7_21, box_1_7_22, box_1_7_23, box_1_7_24, box_1_7_25, box_1_7_26, box_1_7_27, box_1_7_28, box_1_7_29, box_1_7_30, box_1_7_31, box_1_7_32, box_1_7_33, box_1_7_34, box_1_7_35, box_1_7_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_1_8_20, box_1_8_21, box_1_8_22, box_1_8_23, box_1_8_24, box_1_8_25, box_1_8_26, box_1_8_27, box_1_8_28, box_1_8_29, box_1_8_30, box_1_8_31, box_1_8_32, box_1_8_33, box_1_8_34, box_1_8_35, box_1_8_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_1_9_20, box_1_9_21, box_1_9_22, box_1_9_23, box_1_9_24, box_1_9_25, box_1_9_26, box_1_9_27, box_1_9_28, box_1_9_29, box_1_9_30, box_1_9_31, box_1_9_32, box_1_9_33, box_1_9_34, box_1_9_35, box_1_9_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_1_10_20, box_1_10_21, box_1_10_22, box_1_10_23, box_1_10_24, box_1_10_25, box_1_10_26, box_1_10_27, box_1_10_28, box_1_10_29, box_1_10_30, box_1_10_31, box_1_10_32, box_1_10_33, box_1_10_34, box_1_10_35, box_1_10_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_1_11_20, box_1_11_21, box_1_11_22, box_1_11_23, box_1_11_24, box_1_11_25, box_1_11_26, box_1_11_27, box_1_11_28, box_1_11_29, box_1_11_30, box_1_11_31, box_1_11_32, box_1_11_33, box_1_11_34, box_1_11_35, box_1_11_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_1_12_20, box_1_12_21, box_1_12_22, box_1_12_23, box_1_12_24, box_1_12_25, box_1_12_26, box_1_12_27, box_1_12_28, box_1_12_29, box_1_12_30, box_1_12_31, box_1_12_32, box_1_12_33, box_1_12_34, box_1_12_35, box_1_12_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_1_13_20, box_1_13_21, box_1_13_22, box_1_13_23, box_1_13_24, box_1_13_25, box_1_13_26, box_1_13_27, box_1_13_28, box_1_13_29, box_1_13_30, box_1_13_31, box_1_13_32, box_1_13_33, box_1_13_34, box_1_13_35, box_1_13_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_1_14_20, box_1_14_21, box_1_14_22, box_1_14_23, box_1_14_24, box_1_14_25, box_1_14_26, box_1_14_27, box_1_14_28, box_1_14_29, box_1_14_30, box_1_14_31, box_1_14_32, box_1_14_33, box_1_14_34, box_1_14_35, box_1_14_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_1_15_20, box_1_15_21, box_1_15_22, box_1_15_23, box_1_15_24, box_1_15_25, box_1_15_26, box_1_15_27, box_1_15_28, box_1_15_29, box_1_15_30, box_1_15_31, box_1_15_32, box_1_15_33, box_1_15_34, box_1_15_35, box_1_15_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_1_16_20, box_1_16_21, box_1_16_22, box_1_16_23, box_1_16_24, box_1_16_25, box_1_16_26, box_1_16_27, box_1_16_28, box_1_16_29, box_1_16_30, box_1_16_31, box_1_16_32, box_1_16_33, box_1_16_34, box_1_16_35, box_1_16_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_1_17_20, box_1_17_21, box_1_17_22, box_1_17_23, box_1_17_24, box_1_17_25, box_1_17_26, box_1_17_27, box_1_17_28, box_1_17_29, box_1_17_30, box_1_17_31, box_1_17_32, box_1_17_33, box_1_17_34, box_1_17_35, box_1_17_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_1_18_20, box_1_18_21, box_1_18_22, box_1_18_23, box_1_18_24, box_1_18_25, box_1_18_26, box_1_18_27, box_1_18_28, box_1_18_29, box_1_18_30, box_1_18_31, box_1_18_32, box_1_18_33, box_1_18_34, box_1_18_35, box_1_18_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []

        big_box_1 = [
            [box_1_2_20, box_1_2_21, box_1_2_22, box_1_2_23, box_1_2_24, box_1_2_25, box_1_2_26, box_1_2_27, box_1_2_28,
             box_1_2_29, box_1_2_30, box_1_2_31, box_1_2_32, box_1_2_33, box_1_2_34, box_1_2_35, box_1_2_36],
            [box_1_3_20, box_1_3_21, box_1_3_22, box_1_3_23, box_1_3_24, box_1_3_25, box_1_3_26, box_1_3_27, box_1_3_28,
             box_1_3_29, box_1_3_30, box_1_3_31, box_1_3_32, box_1_3_33, box_1_3_34, box_1_3_35, box_1_3_36],
            [box_1_4_20, box_1_4_21, box_1_4_22, box_1_4_23, box_1_4_24, box_1_4_25, box_1_4_26, box_1_4_27, box_1_4_28,
             box_1_4_29, box_1_4_30, box_1_4_31, box_1_4_32, box_1_4_33, box_1_4_34, box_1_4_35, box_1_4_36],
            [box_1_5_20, box_1_5_21, box_1_5_22, box_1_5_23, box_1_5_24, box_1_5_25, box_1_5_26, box_1_5_27, box_1_5_28,
             box_1_5_29, box_1_5_30, box_1_5_31, box_1_5_32, box_1_5_33, box_1_5_34, box_1_5_35, box_1_5_36],
            [box_1_6_20, box_1_6_21, box_1_6_22, box_1_6_23, box_1_6_24, box_1_6_25, box_1_6_26, box_1_6_27, box_1_6_28,
             box_1_6_29, box_1_6_30, box_1_6_31, box_1_6_32, box_1_6_33, box_1_6_34, box_1_6_35, box_1_6_36],
            [box_1_7_20, box_1_7_21, box_1_7_22, box_1_7_23, box_1_7_24, box_1_7_25, box_1_7_26, box_1_7_27, box_1_7_28,
             box_1_7_29, box_1_7_30, box_1_7_31, box_1_7_32, box_1_7_33, box_1_7_34, box_1_7_35, box_1_7_36],
            [box_1_8_20, box_1_8_21, box_1_8_22, box_1_8_23, box_1_8_24, box_1_8_25, box_1_8_26, box_1_8_27, box_1_8_28,
             box_1_8_29, box_1_8_30, box_1_8_31, box_1_8_32, box_1_8_33, box_1_8_34, box_1_8_35, box_1_8_36],
            [box_1_9_20, box_1_9_21, box_1_9_22, box_1_9_23, box_1_9_24, box_1_9_25, box_1_9_26, box_1_9_27, box_1_9_28,
             box_1_9_29, box_1_9_30, box_1_9_31, box_1_9_32, box_1_9_33, box_1_9_34, box_1_9_35, box_1_9_36],
            [box_1_10_20, box_1_10_21, box_1_10_22, box_1_10_23, box_1_10_24, box_1_10_25, box_1_10_26, box_1_10_27,
             box_1_10_28, box_1_10_29, box_1_10_30, box_1_10_31, box_1_10_32, box_1_10_33, box_1_10_34, box_1_10_35,
             box_1_10_36],
            [box_1_11_20, box_1_11_21, box_1_11_22, box_1_11_23, box_1_11_24, box_1_11_25, box_1_11_26, box_1_11_27,
             box_1_11_28, box_1_11_29, box_1_11_30, box_1_11_31, box_1_11_32, box_1_11_33, box_1_11_34, box_1_11_35,
             box_1_11_36],
            [box_1_12_20, box_1_12_21, box_1_12_22, box_1_12_23, box_1_12_24, box_1_12_25, box_1_12_26, box_1_12_27,
             box_1_12_28, box_1_12_29, box_1_12_30, box_1_12_31, box_1_12_32, box_1_12_33, box_1_12_34, box_1_12_35,
             box_1_12_36],
            [box_1_13_20, box_1_13_21, box_1_13_22, box_1_13_23, box_1_13_24, box_1_13_25, box_1_13_26, box_1_13_27,
             box_1_13_28, box_1_13_29, box_1_13_30, box_1_13_31, box_1_13_32, box_1_13_33, box_1_13_34, box_1_13_35,
             box_1_13_36],
            [box_1_14_20, box_1_14_21, box_1_14_22, box_1_14_23, box_1_14_24, box_1_14_25, box_1_14_26, box_1_14_27,
             box_1_14_28, box_1_14_29, box_1_14_30, box_1_14_31, box_1_14_32, box_1_14_33, box_1_14_34, box_1_14_35,
             box_1_14_36],
            [box_1_15_20, box_1_15_21, box_1_15_22, box_1_15_23, box_1_15_24, box_1_15_25, box_1_15_26, box_1_15_27,
             box_1_15_28, box_1_15_29, box_1_15_30, box_1_15_31, box_1_15_32, box_1_15_33, box_1_15_34, box_1_15_35,
             box_1_15_36],
            [box_1_16_20, box_1_16_21, box_1_16_22, box_1_16_23, box_1_16_24, box_1_16_25, box_1_16_26, box_1_16_27,
             box_1_16_28, box_1_16_29, box_1_16_30, box_1_16_31, box_1_16_32, box_1_16_33, box_1_16_34, box_1_16_35,
             box_1_16_36],
            [box_1_17_20, box_1_17_21, box_1_17_22, box_1_17_23, box_1_17_24, box_1_17_25, box_1_17_26, box_1_17_27,
             box_1_17_28, box_1_17_29, box_1_17_30, box_1_17_31, box_1_17_32, box_1_17_33, box_1_17_34, box_1_17_35,
             box_1_17_36],
            [box_1_18_20, box_1_18_21, box_1_18_22, box_1_18_23, box_1_18_24, box_1_18_25, box_1_18_26, box_1_18_27,
             box_1_18_28, box_1_18_29, box_1_18_30, box_1_18_31, box_1_18_32, box_1_18_33, box_1_18_34, box_1_18_35,
             box_1_18_36]
            ]

        box_1_type_2_20, box_1_type_2_21, box_1_type_2_22, box_1_type_2_23, box_1_type_2_24, box_1_type_2_25, box_1_type_2_26, box_1_type_2_27, box_1_type_2_28, box_1_type_2_29, box_1_type_2_30, box_1_type_2_31, box_1_type_2_32, box_1_type_2_33, box_1_type_2_34, box_1_type_2_35, box_1_type_2_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_1_type_3_20, box_1_type_3_21, box_1_type_3_22, box_1_type_3_23, box_1_type_3_24, box_1_type_3_25, box_1_type_3_26, box_1_type_3_27, box_1_type_3_28, box_1_type_3_29, box_1_type_3_30, box_1_type_3_31, box_1_type_3_32, box_1_type_3_33, box_1_type_3_34, box_1_type_3_35, box_1_type_3_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_1_type_4_20, box_1_type_4_21, box_1_type_4_22, box_1_type_4_23, box_1_type_4_24, box_1_type_4_25, box_1_type_4_26, box_1_type_4_27, box_1_type_4_28, box_1_type_4_29, box_1_type_4_30, box_1_type_4_31, box_1_type_4_32, box_1_type_4_33, box_1_type_4_34, box_1_type_4_35, box_1_type_4_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_1_type_5_20, box_1_type_5_21, box_1_type_5_22, box_1_type_5_23, box_1_type_5_24, box_1_type_5_25, box_1_type_5_26, box_1_type_5_27, box_1_type_5_28, box_1_type_5_29, box_1_type_5_30, box_1_type_5_31, box_1_type_5_32, box_1_type_5_33, box_1_type_5_34, box_1_type_5_35, box_1_type_5_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_1_type_6_20, box_1_type_6_21, box_1_type_6_22, box_1_type_6_23, box_1_type_6_24, box_1_type_6_25, box_1_type_6_26, box_1_type_6_27, box_1_type_6_28, box_1_type_6_29, box_1_type_6_30, box_1_type_6_31, box_1_type_6_32, box_1_type_6_33, box_1_type_6_34, box_1_type_6_35, box_1_type_6_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_1_type_7_20, box_1_type_7_21, box_1_type_7_22, box_1_type_7_23, box_1_type_7_24, box_1_type_7_25, box_1_type_7_26, box_1_type_7_27, box_1_type_7_28, box_1_type_7_29, box_1_type_7_30, box_1_type_7_31, box_1_type_7_32, box_1_type_7_33, box_1_type_7_34, box_1_type_7_35, box_1_type_7_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_1_type_8_20, box_1_type_8_21, box_1_type_8_22, box_1_type_8_23, box_1_type_8_24, box_1_type_8_25, box_1_type_8_26, box_1_type_8_27, box_1_type_8_28, box_1_type_8_29, box_1_type_8_30, box_1_type_8_31, box_1_type_8_32, box_1_type_8_33, box_1_type_8_34, box_1_type_8_35, box_1_type_8_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_1_type_9_20, box_1_type_9_21, box_1_type_9_22, box_1_type_9_23, box_1_type_9_24, box_1_type_9_25, box_1_type_9_26, box_1_type_9_27, box_1_type_9_28, box_1_type_9_29, box_1_type_9_30, box_1_type_9_31, box_1_type_9_32, box_1_type_9_33, box_1_type_9_34, box_1_type_9_35, box_1_type_9_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_1_type_10_20, box_1_type_10_21, box_1_type_10_22, box_1_type_10_23, box_1_type_10_24, box_1_type_10_25, box_1_type_10_26, box_1_type_10_27, box_1_type_10_28, box_1_type_10_29, box_1_type_10_30, box_1_type_10_31, box_1_type_10_32, box_1_type_10_33, box_1_type_10_34, box_1_type_10_35, box_1_type_10_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_1_type_11_20, box_1_type_11_21, box_1_type_11_22, box_1_type_11_23, box_1_type_11_24, box_1_type_11_25, box_1_type_11_26, box_1_type_11_27, box_1_type_11_28, box_1_type_11_29, box_1_type_11_30, box_1_type_11_31, box_1_type_11_32, box_1_type_11_33, box_1_type_11_34, box_1_type_11_35, box_1_type_11_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_1_type_12_20, box_1_type_12_21, box_1_type_12_22, box_1_type_12_23, box_1_type_12_24, box_1_type_12_25, box_1_type_12_26, box_1_type_12_27, box_1_type_12_28, box_1_type_12_29, box_1_type_12_30, box_1_type_12_31, box_1_type_12_32, box_1_type_12_33, box_1_type_12_34, box_1_type_12_35, box_1_type_12_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_1_type_13_20, box_1_type_13_21, box_1_type_13_22, box_1_type_13_23, box_1_type_13_24, box_1_type_13_25, box_1_type_13_26, box_1_type_13_27, box_1_type_13_28, box_1_type_13_29, box_1_type_13_30, box_1_type_13_31, box_1_type_13_32, box_1_type_13_33, box_1_type_13_34, box_1_type_13_35, box_1_type_13_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_1_type_14_20, box_1_type_14_21, box_1_type_14_22, box_1_type_14_23, box_1_type_14_24, box_1_type_14_25, box_1_type_14_26, box_1_type_14_27, box_1_type_14_28, box_1_type_14_29, box_1_type_14_30, box_1_type_14_31, box_1_type_14_32, box_1_type_14_33, box_1_type_14_34, box_1_type_14_35, box_1_type_14_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_1_type_15_20, box_1_type_15_21, box_1_type_15_22, box_1_type_15_23, box_1_type_15_24, box_1_type_15_25, box_1_type_15_26, box_1_type_15_27, box_1_type_15_28, box_1_type_15_29, box_1_type_15_30, box_1_type_15_31, box_1_type_15_32, box_1_type_15_33, box_1_type_15_34, box_1_type_15_35, box_1_type_15_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_1_type_16_20, box_1_type_16_21, box_1_type_16_22, box_1_type_16_23, box_1_type_16_24, box_1_type_16_25, box_1_type_16_26, box_1_type_16_27, box_1_type_16_28, box_1_type_16_29, box_1_type_16_30, box_1_type_16_31, box_1_type_16_32, box_1_type_16_33, box_1_type_16_34, box_1_type_16_35, box_1_type_16_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_1_type_17_20, box_1_type_17_21, box_1_type_17_22, box_1_type_17_23, box_1_type_17_24, box_1_type_17_25, box_1_type_17_26, box_1_type_17_27, box_1_type_17_28, box_1_type_17_29, box_1_type_17_30, box_1_type_17_31, box_1_type_17_32, box_1_type_17_33, box_1_type_17_34, box_1_type_17_35, box_1_type_17_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_1_type_18_20, box_1_type_18_21, box_1_type_18_22, box_1_type_18_23, box_1_type_18_24, box_1_type_18_25, box_1_type_18_26, box_1_type_18_27, box_1_type_18_28, box_1_type_18_29, box_1_type_18_30, box_1_type_18_31, box_1_type_18_32, box_1_type_18_33, box_1_type_18_34, box_1_type_18_35, box_1_type_18_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []

        big_type_box_1 = [
            [box_1_type_2_20, box_1_type_2_21, box_1_type_2_22, box_1_type_2_23, box_1_type_2_24, box_1_type_2_25,
             box_1_type_2_26, box_1_type_2_27, box_1_type_2_28, box_1_type_2_29, box_1_type_2_30, box_1_type_2_31,
             box_1_type_2_32, box_1_type_2_33, box_1_type_2_34, box_1_type_2_35, box_1_type_2_36],
            [box_1_type_3_20, box_1_type_3_21, box_1_type_3_22, box_1_type_3_23, box_1_type_3_24, box_1_type_3_25,
             box_1_type_3_26, box_1_type_3_27, box_1_type_3_28, box_1_type_3_29, box_1_type_3_30, box_1_type_3_31,
             box_1_type_3_32, box_1_type_3_33, box_1_type_3_34, box_1_type_3_35, box_1_type_3_36],
            [box_1_type_4_20, box_1_type_4_21, box_1_type_4_22, box_1_type_4_23, box_1_type_4_24, box_1_type_4_25,
             box_1_type_4_26, box_1_type_4_27, box_1_type_4_28, box_1_type_4_29, box_1_type_4_30, box_1_type_4_31,
             box_1_type_4_32, box_1_type_4_33, box_1_type_4_34, box_1_type_4_35, box_1_type_4_36],
            [box_1_type_5_20, box_1_type_5_21, box_1_type_5_22, box_1_type_5_23, box_1_type_5_24, box_1_type_5_25,
             box_1_type_5_26, box_1_type_5_27, box_1_type_5_28, box_1_type_5_29, box_1_type_5_30, box_1_type_5_31,
             box_1_type_5_32, box_1_type_5_33, box_1_type_5_34, box_1_type_5_35, box_1_type_5_36],
            [box_1_type_6_20, box_1_type_6_21, box_1_type_6_22, box_1_type_6_23, box_1_type_6_24, box_1_type_6_25,
             box_1_type_6_26, box_1_type_6_27, box_1_type_6_28, box_1_type_6_29, box_1_type_6_30, box_1_type_6_31,
             box_1_type_6_32, box_1_type_6_33, box_1_type_6_34, box_1_type_6_35, box_1_type_6_36],
            [box_1_type_7_20, box_1_type_7_21, box_1_type_7_22, box_1_type_7_23, box_1_type_7_24, box_1_type_7_25,
             box_1_type_7_26, box_1_type_7_27, box_1_type_7_28, box_1_type_7_29, box_1_type_7_30, box_1_type_7_31,
             box_1_type_7_32, box_1_type_7_33, box_1_type_7_34, box_1_type_7_35, box_1_type_7_36],
            [box_1_type_8_20, box_1_type_8_21, box_1_type_8_22, box_1_type_8_23, box_1_type_8_24, box_1_type_8_25,
             box_1_type_8_26, box_1_type_8_27, box_1_type_8_28, box_1_type_8_29, box_1_type_8_30, box_1_type_8_31,
             box_1_type_8_32, box_1_type_8_33, box_1_type_8_34, box_1_type_8_35, box_1_type_8_36],
            [box_1_type_9_20, box_1_type_9_21, box_1_type_9_22, box_1_type_9_23, box_1_type_9_24, box_1_type_9_25,
             box_1_type_9_26, box_1_type_9_27, box_1_type_9_28, box_1_type_9_29, box_1_type_9_30, box_1_type_9_31,
             box_1_type_9_32, box_1_type_9_33, box_1_type_9_34, box_1_type_9_35, box_1_type_9_36],
            [box_1_type_10_20, box_1_type_10_21, box_1_type_10_22, box_1_type_10_23, box_1_type_10_24, box_1_type_10_25,
             box_1_type_10_26, box_1_type_10_27, box_1_type_10_28, box_1_type_10_29, box_1_type_10_30, box_1_type_10_31,
             box_1_type_10_32, box_1_type_10_33, box_1_type_10_34, box_1_type_10_35, box_1_type_10_36],
            [box_1_type_11_20, box_1_type_11_21, box_1_type_11_22, box_1_type_11_23, box_1_type_11_24, box_1_type_11_25,
             box_1_type_11_26, box_1_type_11_27, box_1_type_11_28, box_1_type_11_29, box_1_type_11_30, box_1_type_11_31,
             box_1_type_11_32, box_1_type_11_33, box_1_type_11_34, box_1_type_11_35, box_1_type_11_36],
            [box_1_type_12_20, box_1_type_12_21, box_1_type_12_22, box_1_type_12_23, box_1_type_12_24, box_1_type_12_25,
             box_1_type_12_26, box_1_type_12_27, box_1_type_12_28, box_1_type_12_29, box_1_type_12_30, box_1_type_12_31,
             box_1_type_12_32, box_1_type_12_33, box_1_type_12_34, box_1_type_12_35, box_1_type_12_36],
            [box_1_type_13_20, box_1_type_13_21, box_1_type_13_22, box_1_type_13_23, box_1_type_13_24, box_1_type_13_25,
             box_1_type_13_26, box_1_type_13_27, box_1_type_13_28, box_1_type_13_29, box_1_type_13_30, box_1_type_13_31,
             box_1_type_13_32, box_1_type_13_33, box_1_type_13_34, box_1_type_13_35, box_1_type_13_36],
            [box_1_type_14_20, box_1_type_14_21, box_1_type_14_22, box_1_type_14_23, box_1_type_14_24, box_1_type_14_25,
             box_1_type_14_26, box_1_type_14_27, box_1_type_14_28, box_1_type_14_29, box_1_type_14_30, box_1_type_14_31,
             box_1_type_14_32, box_1_type_14_33, box_1_type_14_34, box_1_type_14_35, box_1_type_14_36],
            [box_1_type_15_20, box_1_type_15_21, box_1_type_15_22, box_1_type_15_23, box_1_type_15_24, box_1_type_15_25,
             box_1_type_15_26, box_1_type_15_27, box_1_type_15_28, box_1_type_15_29, box_1_type_15_30, box_1_type_15_31,
             box_1_type_15_32, box_1_type_15_33, box_1_type_15_34, box_1_type_15_35, box_1_type_15_36],
            [box_1_type_16_20, box_1_type_16_21, box_1_type_16_22, box_1_type_16_23, box_1_type_16_24, box_1_type_16_25,
             box_1_type_16_26, box_1_type_16_27, box_1_type_16_28, box_1_type_16_29, box_1_type_16_30, box_1_type_16_31,
             box_1_type_16_32, box_1_type_16_33, box_1_type_16_34, box_1_type_16_35, box_1_type_16_36],
            [box_1_type_17_20, box_1_type_17_21, box_1_type_17_22, box_1_type_17_23, box_1_type_17_24, box_1_type_17_25,
             box_1_type_17_26, box_1_type_17_27, box_1_type_17_28, box_1_type_17_29, box_1_type_17_30, box_1_type_17_31,
             box_1_type_17_32, box_1_type_17_33, box_1_type_17_34, box_1_type_17_35, box_1_type_17_36],
            [box_1_type_18_20, box_1_type_18_21, box_1_type_18_22, box_1_type_18_23, box_1_type_18_24, box_1_type_18_25,
             box_1_type_18_26, box_1_type_18_27, box_1_type_18_28, box_1_type_18_29, box_1_type_18_30, box_1_type_18_31,
             box_1_type_18_32, box_1_type_18_33, box_1_type_18_34, box_1_type_18_35, box_1_type_18_36]
            ]

        # 모레에 대한 변수 선언
        box_2_2_20, box_2_2_21, box_2_2_22, box_2_2_23, box_2_2_24, box_2_2_25, box_2_2_26, box_2_2_27, box_2_2_28, box_2_2_29, box_2_2_30, box_2_2_31, box_2_2_32, box_2_2_33, box_2_2_34, box_2_2_35, box_2_2_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_2_3_20, box_2_3_21, box_2_3_22, box_2_3_23, box_2_3_24, box_2_3_25, box_2_3_26, box_2_3_27, box_2_3_28, box_2_3_29, box_2_3_30, box_2_3_31, box_2_3_32, box_2_3_33, box_2_3_34, box_2_3_35, box_2_3_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_2_4_20, box_2_4_21, box_2_4_22, box_2_4_23, box_2_4_24, box_2_4_25, box_2_4_26, box_2_4_27, box_2_4_28, box_2_4_29, box_2_4_30, box_2_4_31, box_2_4_32, box_2_4_33, box_2_4_34, box_2_4_35, box_2_4_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_2_5_20, box_2_5_21, box_2_5_22, box_2_5_23, box_2_5_24, box_2_5_25, box_2_5_26, box_2_5_27, box_2_5_28, box_2_5_29, box_2_5_30, box_2_5_31, box_2_5_32, box_2_5_33, box_2_5_34, box_2_5_35, box_2_5_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_2_6_20, box_2_6_21, box_2_6_22, box_2_6_23, box_2_6_24, box_2_6_25, box_2_6_26, box_2_6_27, box_2_6_28, box_2_6_29, box_2_6_30, box_2_6_31, box_2_6_32, box_2_6_33, box_2_6_34, box_2_6_35, box_2_6_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_2_7_20, box_2_7_21, box_2_7_22, box_2_7_23, box_2_7_24, box_2_7_25, box_2_7_26, box_2_7_27, box_2_7_28, box_2_7_29, box_2_7_30, box_2_7_31, box_2_7_32, box_2_7_33, box_2_7_34, box_2_7_35, box_2_7_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_2_8_20, box_2_8_21, box_2_8_22, box_2_8_23, box_2_8_24, box_2_8_25, box_2_8_26, box_2_8_27, box_2_8_28, box_2_8_29, box_2_8_30, box_2_8_31, box_2_8_32, box_2_8_33, box_2_8_34, box_2_8_35, box_2_8_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_2_9_20, box_2_9_21, box_2_9_22, box_2_9_23, box_2_9_24, box_2_9_25, box_2_9_26, box_2_9_27, box_2_9_28, box_2_9_29, box_2_9_30, box_2_9_31, box_2_9_32, box_2_9_33, box_2_9_34, box_2_9_35, box_2_9_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_2_10_20, box_2_10_21, box_2_10_22, box_2_10_23, box_2_10_24, box_2_10_25, box_2_10_26, box_2_10_27, box_2_10_28, box_2_10_29, box_2_10_30, box_2_10_31, box_2_10_32, box_2_10_33, box_2_10_34, box_2_10_35, box_2_10_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_2_11_20, box_2_11_21, box_2_11_22, box_2_11_23, box_2_11_24, box_2_11_25, box_2_11_26, box_2_11_27, box_2_11_28, box_2_11_29, box_2_11_30, box_2_11_31, box_2_11_32, box_2_11_33, box_2_11_34, box_2_11_35, box_2_11_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_2_12_20, box_2_12_21, box_2_12_22, box_2_12_23, box_2_12_24, box_2_12_25, box_2_12_26, box_2_12_27, box_2_12_28, box_2_12_29, box_2_12_30, box_2_12_31, box_2_12_32, box_2_12_33, box_2_12_34, box_2_12_35, box_2_12_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_2_13_20, box_2_13_21, box_2_13_22, box_2_13_23, box_2_13_24, box_2_13_25, box_2_13_26, box_2_13_27, box_2_13_28, box_2_13_29, box_2_13_30, box_2_13_31, box_2_13_32, box_2_13_33, box_2_13_34, box_2_13_35, box_2_13_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_2_14_20, box_2_14_21, box_2_14_22, box_2_14_23, box_2_14_24, box_2_14_25, box_2_14_26, box_2_14_27, box_2_14_28, box_2_14_29, box_2_14_30, box_2_14_31, box_2_14_32, box_2_14_33, box_2_14_34, box_2_14_35, box_2_14_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_2_15_20, box_2_15_21, box_2_15_22, box_2_15_23, box_2_15_24, box_2_15_25, box_2_15_26, box_2_15_27, box_2_15_28, box_2_15_29, box_2_15_30, box_2_15_31, box_2_15_32, box_2_15_33, box_2_15_34, box_2_15_35, box_2_15_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_2_16_20, box_2_16_21, box_2_16_22, box_2_16_23, box_2_16_24, box_2_16_25, box_2_16_26, box_2_16_27, box_2_16_28, box_2_16_29, box_2_16_30, box_2_16_31, box_2_16_32, box_2_16_33, box_2_16_34, box_2_16_35, box_2_16_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_2_17_20, box_2_17_21, box_2_17_22, box_2_17_23, box_2_17_24, box_2_17_25, box_2_17_26, box_2_17_27, box_2_17_28, box_2_17_29, box_2_17_30, box_2_17_31, box_2_17_32, box_2_17_33, box_2_17_34, box_2_17_35, box_2_17_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_2_18_20, box_2_18_21, box_2_18_22, box_2_18_23, box_2_18_24, box_2_18_25, box_2_18_26, box_2_18_27, box_2_18_28, box_2_18_29, box_2_18_30, box_2_18_31, box_2_18_32, box_2_18_33, box_2_18_34, box_2_18_35, box_2_18_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []

        big_box_2 = [
            [box_2_2_20, box_2_2_21, box_2_2_22, box_2_2_23, box_2_2_24, box_2_2_25, box_2_2_26, box_2_2_27, box_2_2_28,
             box_2_2_29, box_2_2_30, box_2_2_31, box_2_2_32, box_2_2_33, box_2_2_34, box_2_2_35, box_2_2_36],
            [box_2_3_20, box_2_3_21, box_2_3_22, box_2_3_23, box_2_3_24, box_2_3_25, box_2_3_26, box_2_3_27, box_2_3_28,
             box_2_3_29, box_2_3_30, box_2_3_31, box_2_3_32, box_2_3_33, box_2_3_34, box_2_3_35, box_2_3_36],
            [box_2_4_20, box_2_4_21, box_2_4_22, box_2_4_23, box_2_4_24, box_2_4_25, box_2_4_26, box_2_4_27, box_2_4_28,
             box_2_4_29, box_2_4_30, box_2_4_31, box_2_4_32, box_2_4_33, box_2_4_34, box_2_4_35, box_2_4_36],
            [box_2_5_20, box_2_5_21, box_2_5_22, box_2_5_23, box_2_5_24, box_2_5_25, box_2_5_26, box_2_5_27, box_2_5_28,
             box_2_5_29, box_2_5_30, box_2_5_31, box_2_5_32, box_2_5_33, box_2_5_34, box_2_5_35, box_2_5_36],
            [box_2_6_20, box_2_6_21, box_2_6_22, box_2_6_23, box_2_6_24, box_2_6_25, box_2_6_26, box_2_6_27, box_2_6_28,
             box_2_6_29, box_2_6_30, box_2_6_31, box_2_6_32, box_2_6_33, box_2_6_34, box_2_6_35, box_2_6_36],
            [box_2_7_20, box_2_7_21, box_2_7_22, box_2_7_23, box_2_7_24, box_2_7_25, box_2_7_26, box_2_7_27, box_2_7_28,
             box_2_7_29, box_2_7_30, box_2_7_31, box_2_7_32, box_2_7_33, box_2_7_34, box_2_7_35, box_2_7_36],
            [box_2_8_20, box_2_8_21, box_2_8_22, box_2_8_23, box_2_8_24, box_2_8_25, box_2_8_26, box_2_8_27, box_2_8_28,
             box_2_8_29, box_2_8_30, box_2_8_31, box_2_8_32, box_2_8_33, box_2_8_34, box_2_8_35, box_2_8_36],
            [box_2_9_20, box_2_9_21, box_2_9_22, box_2_9_23, box_2_9_24, box_2_9_25, box_2_9_26, box_2_9_27, box_2_9_28,
             box_2_9_29, box_2_9_30, box_2_9_31, box_2_9_32, box_2_9_33, box_2_9_34, box_2_9_35, box_2_9_36],
            [box_2_10_20, box_2_10_21, box_2_10_22, box_2_10_23, box_2_10_24, box_2_10_25, box_2_10_26, box_2_10_27,
             box_2_10_28, box_2_10_29, box_2_10_30, box_2_10_31, box_2_10_32, box_2_10_33, box_2_10_34, box_2_10_35,
             box_2_10_36],
            [box_2_11_20, box_2_11_21, box_2_11_22, box_2_11_23, box_2_11_24, box_2_11_25, box_2_11_26, box_2_11_27,
             box_2_11_28, box_2_11_29, box_2_11_30, box_2_11_31, box_2_11_32, box_2_11_33, box_2_11_34, box_2_11_35,
             box_2_11_36],
            [box_2_12_20, box_2_12_21, box_2_12_22, box_2_12_23, box_2_12_24, box_2_12_25, box_2_12_26, box_2_12_27,
             box_2_12_28, box_2_12_29, box_2_12_30, box_2_12_31, box_2_12_32, box_2_12_33, box_2_12_34, box_2_12_35,
             box_2_12_36],
            [box_2_13_20, box_2_13_21, box_2_13_22, box_2_13_23, box_2_13_24, box_2_13_25, box_2_13_26, box_2_13_27,
             box_2_13_28, box_2_13_29, box_2_13_30, box_2_13_31, box_2_13_32, box_2_13_33, box_2_13_34, box_2_13_35,
             box_2_13_36],
            [box_2_14_20, box_2_14_21, box_2_14_22, box_2_14_23, box_2_14_24, box_2_14_25, box_2_14_26, box_2_14_27,
             box_2_14_28, box_2_14_29, box_2_14_30, box_2_14_31, box_2_14_32, box_2_14_33, box_2_14_34, box_2_14_35,
             box_2_14_36],
            [box_2_15_20, box_2_15_21, box_2_15_22, box_2_15_23, box_2_15_24, box_2_15_25, box_2_15_26, box_2_15_27,
             box_2_15_28, box_2_15_29, box_2_15_30, box_2_15_31, box_2_15_32, box_2_15_33, box_2_15_34, box_2_15_35,
             box_2_15_36],
            [box_2_16_20, box_2_16_21, box_2_16_22, box_2_16_23, box_2_16_24, box_2_16_25, box_2_16_26, box_2_16_27,
             box_2_16_28, box_2_16_29, box_2_16_30, box_2_16_31, box_2_16_32, box_2_16_33, box_2_16_34, box_2_16_35,
             box_2_16_36],
            [box_2_17_20, box_2_17_21, box_2_17_22, box_2_17_23, box_2_17_24, box_2_17_25, box_2_17_26, box_2_17_27,
             box_2_17_28, box_2_17_29, box_2_17_30, box_2_17_31, box_2_17_32, box_2_17_33, box_2_17_34, box_2_17_35,
             box_2_17_36],
            [box_2_18_20, box_2_18_21, box_2_18_22, box_2_18_23, box_2_18_24, box_2_18_25, box_2_18_26, box_2_18_27,
             box_2_18_28, box_2_18_29, box_2_18_30, box_2_18_31, box_2_18_32, box_2_18_33, box_2_18_34, box_2_18_35,
             box_2_18_36]
            ]

        box_2_type_2_20, box_2_type_2_21, box_2_type_2_22, box_2_type_2_23, box_2_type_2_24, box_2_type_2_25, box_2_type_2_26, box_2_type_2_27, box_2_type_2_28, box_2_type_2_29, box_2_type_2_30, box_2_type_2_31, box_2_type_2_32, box_2_type_2_33, box_2_type_2_34, box_2_type_2_35, box_2_type_2_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_2_type_3_20, box_2_type_3_21, box_2_type_3_22, box_2_type_3_23, box_2_type_3_24, box_2_type_3_25, box_2_type_3_26, box_2_type_3_27, box_2_type_3_28, box_2_type_3_29, box_2_type_3_30, box_2_type_3_31, box_2_type_3_32, box_2_type_3_33, box_2_type_3_34, box_2_type_3_35, box_2_type_3_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_2_type_4_20, box_2_type_4_21, box_2_type_4_22, box_2_type_4_23, box_2_type_4_24, box_2_type_4_25, box_2_type_4_26, box_2_type_4_27, box_2_type_4_28, box_2_type_4_29, box_2_type_4_30, box_2_type_4_31, box_2_type_4_32, box_2_type_4_33, box_2_type_4_34, box_2_type_4_35, box_2_type_4_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_2_type_5_20, box_2_type_5_21, box_2_type_5_22, box_2_type_5_23, box_2_type_5_24, box_2_type_5_25, box_2_type_5_26, box_2_type_5_27, box_2_type_5_28, box_2_type_5_29, box_2_type_5_30, box_2_type_5_31, box_2_type_5_32, box_2_type_5_33, box_2_type_5_34, box_2_type_5_35, box_2_type_5_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_2_type_6_20, box_2_type_6_21, box_2_type_6_22, box_2_type_6_23, box_2_type_6_24, box_2_type_6_25, box_2_type_6_26, box_2_type_6_27, box_2_type_6_28, box_2_type_6_29, box_2_type_6_30, box_2_type_6_31, box_2_type_6_32, box_2_type_6_33, box_2_type_6_34, box_2_type_6_35, box_2_type_6_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_2_type_7_20, box_2_type_7_21, box_2_type_7_22, box_2_type_7_23, box_2_type_7_24, box_2_type_7_25, box_2_type_7_26, box_2_type_7_27, box_2_type_7_28, box_2_type_7_29, box_2_type_7_30, box_2_type_7_31, box_2_type_7_32, box_2_type_7_33, box_2_type_7_34, box_2_type_7_35, box_2_type_7_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_2_type_8_20, box_2_type_8_21, box_2_type_8_22, box_2_type_8_23, box_2_type_8_24, box_2_type_8_25, box_2_type_8_26, box_2_type_8_27, box_2_type_8_28, box_2_type_8_29, box_2_type_8_30, box_2_type_8_31, box_2_type_8_32, box_2_type_8_33, box_2_type_8_34, box_2_type_8_35, box_2_type_8_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_2_type_9_20, box_2_type_9_21, box_2_type_9_22, box_2_type_9_23, box_2_type_9_24, box_2_type_9_25, box_2_type_9_26, box_2_type_9_27, box_2_type_9_28, box_2_type_9_29, box_2_type_9_30, box_2_type_9_31, box_2_type_9_32, box_2_type_9_33, box_2_type_9_34, box_2_type_9_35, box_2_type_9_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_2_type_10_20, box_2_type_10_21, box_2_type_10_22, box_2_type_10_23, box_2_type_10_24, box_2_type_10_25, box_2_type_10_26, box_2_type_10_27, box_2_type_10_28, box_2_type_10_29, box_2_type_10_30, box_2_type_10_31, box_2_type_10_32, box_2_type_10_33, box_2_type_10_34, box_2_type_10_35, box_2_type_10_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_2_type_11_20, box_2_type_11_21, box_2_type_11_22, box_2_type_11_23, box_2_type_11_24, box_2_type_11_25, box_2_type_11_26, box_2_type_11_27, box_2_type_11_28, box_2_type_11_29, box_2_type_11_30, box_2_type_11_31, box_2_type_11_32, box_2_type_11_33, box_2_type_11_34, box_2_type_11_35, box_2_type_11_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_2_type_12_20, box_2_type_12_21, box_2_type_12_22, box_2_type_12_23, box_2_type_12_24, box_2_type_12_25, box_2_type_12_26, box_2_type_12_27, box_2_type_12_28, box_2_type_12_29, box_2_type_12_30, box_2_type_12_31, box_2_type_12_32, box_2_type_12_33, box_2_type_12_34, box_2_type_12_35, box_2_type_12_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_2_type_13_20, box_2_type_13_21, box_2_type_13_22, box_2_type_13_23, box_2_type_13_24, box_2_type_13_25, box_2_type_13_26, box_2_type_13_27, box_2_type_13_28, box_2_type_13_29, box_2_type_13_30, box_2_type_13_31, box_2_type_13_32, box_2_type_13_33, box_2_type_13_34, box_2_type_13_35, box_2_type_13_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_2_type_14_20, box_2_type_14_21, box_2_type_14_22, box_2_type_14_23, box_2_type_14_24, box_2_type_14_25, box_2_type_14_26, box_2_type_14_27, box_2_type_14_28, box_2_type_14_29, box_2_type_14_30, box_2_type_14_31, box_2_type_14_32, box_2_type_14_33, box_2_type_14_34, box_2_type_14_35, box_2_type_14_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_2_type_15_20, box_2_type_15_21, box_2_type_15_22, box_2_type_15_23, box_2_type_15_24, box_2_type_15_25, box_2_type_15_26, box_2_type_15_27, box_2_type_15_28, box_2_type_15_29, box_2_type_15_30, box_2_type_15_31, box_2_type_15_32, box_2_type_15_33, box_2_type_15_34, box_2_type_15_35, box_2_type_15_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_2_type_16_20, box_2_type_16_21, box_2_type_16_22, box_2_type_16_23, box_2_type_16_24, box_2_type_16_25, box_2_type_16_26, box_2_type_16_27, box_2_type_16_28, box_2_type_16_29, box_2_type_16_30, box_2_type_16_31, box_2_type_16_32, box_2_type_16_33, box_2_type_16_34, box_2_type_16_35, box_2_type_16_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_2_type_17_20, box_2_type_17_21, box_2_type_17_22, box_2_type_17_23, box_2_type_17_24, box_2_type_17_25, box_2_type_17_26, box_2_type_17_27, box_2_type_17_28, box_2_type_17_29, box_2_type_17_30, box_2_type_17_31, box_2_type_17_32, box_2_type_17_33, box_2_type_17_34, box_2_type_17_35, box_2_type_17_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        box_2_type_18_20, box_2_type_18_21, box_2_type_18_22, box_2_type_18_23, box_2_type_18_24, box_2_type_18_25, box_2_type_18_26, box_2_type_18_27, box_2_type_18_28, box_2_type_18_29, box_2_type_18_30, box_2_type_18_31, box_2_type_18_32, box_2_type_18_33, box_2_type_18_34, box_2_type_18_35, box_2_type_18_36 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []

        big_type_box_2 = [
            [box_2_type_2_20, box_2_type_2_21, box_2_type_2_22, box_2_type_2_23, box_2_type_2_24, box_2_type_2_25,
             box_2_type_2_26, box_2_type_2_27, box_2_type_2_28, box_2_type_2_29, box_2_type_2_30, box_2_type_2_31,
             box_2_type_2_32, box_2_type_2_33, box_2_type_2_34, box_2_type_2_35, box_2_type_2_36],
            [box_2_type_3_20, box_2_type_3_21, box_2_type_3_22, box_2_type_3_23, box_2_type_3_24, box_2_type_3_25,
             box_2_type_3_26, box_2_type_3_27, box_2_type_3_28, box_2_type_3_29, box_2_type_3_30, box_2_type_3_31,
             box_2_type_3_32, box_2_type_3_33, box_2_type_3_34, box_2_type_3_35, box_2_type_3_36],
            [box_2_type_4_20, box_2_type_4_21, box_2_type_4_22, box_2_type_4_23, box_2_type_4_24, box_2_type_4_25,
             box_2_type_4_26, box_2_type_4_27, box_2_type_4_28, box_2_type_4_29, box_2_type_4_30, box_2_type_4_31,
             box_2_type_4_32, box_2_type_4_33, box_2_type_4_34, box_2_type_4_35, box_2_type_4_36],
            [box_2_type_5_20, box_2_type_5_21, box_2_type_5_22, box_2_type_5_23, box_2_type_5_24, box_2_type_5_25,
             box_2_type_5_26, box_2_type_5_27, box_2_type_5_28, box_2_type_5_29, box_2_type_5_30, box_2_type_5_31,
             box_2_type_5_32, box_2_type_5_33, box_2_type_5_34, box_2_type_5_35, box_2_type_5_36],
            [box_2_type_6_20, box_2_type_6_21, box_2_type_6_22, box_2_type_6_23, box_2_type_6_24, box_2_type_6_25,
             box_2_type_6_26, box_2_type_6_27, box_2_type_6_28, box_2_type_6_29, box_2_type_6_30, box_2_type_6_31,
             box_2_type_6_32, box_2_type_6_33, box_2_type_6_34, box_2_type_6_35, box_2_type_6_36],
            [box_2_type_7_20, box_2_type_7_21, box_2_type_7_22, box_2_type_7_23, box_2_type_7_24, box_2_type_7_25,
             box_2_type_7_26, box_2_type_7_27, box_2_type_7_28, box_2_type_7_29, box_2_type_7_30, box_2_type_7_31,
             box_2_type_7_32, box_2_type_7_33, box_2_type_7_34, box_2_type_7_35, box_2_type_7_36],
            [box_2_type_8_20, box_2_type_8_21, box_2_type_8_22, box_2_type_8_23, box_2_type_8_24, box_2_type_8_25,
             box_2_type_8_26, box_2_type_8_27, box_2_type_8_28, box_2_type_8_29, box_2_type_8_30, box_2_type_8_31,
             box_2_type_8_32, box_2_type_8_33, box_2_type_8_34, box_2_type_8_35, box_2_type_8_36],
            [box_2_type_9_20, box_2_type_9_21, box_2_type_9_22, box_2_type_9_23, box_2_type_9_24, box_2_type_9_25,
             box_2_type_9_26, box_2_type_9_27, box_2_type_9_28, box_2_type_9_29, box_2_type_9_30, box_2_type_9_31,
             box_2_type_9_32, box_2_type_9_33, box_2_type_9_34, box_2_type_9_35, box_2_type_9_36],
            [box_2_type_10_20, box_2_type_10_21, box_2_type_10_22, box_2_type_10_23, box_2_type_10_24, box_2_type_10_25,
             box_2_type_10_26, box_2_type_10_27, box_2_type_10_28, box_2_type_10_29, box_2_type_10_30, box_2_type_10_31,
             box_2_type_10_32, box_2_type_10_33, box_2_type_10_34, box_2_type_10_35, box_2_type_10_36],
            [box_2_type_11_20, box_2_type_11_21, box_2_type_11_22, box_2_type_11_23, box_2_type_11_24, box_2_type_11_25,
             box_2_type_11_26, box_2_type_11_27, box_2_type_11_28, box_2_type_11_29, box_2_type_11_30, box_2_type_11_31,
             box_2_type_11_32, box_2_type_11_33, box_2_type_11_34, box_2_type_11_35, box_2_type_11_36],
            [box_2_type_12_20, box_2_type_12_21, box_2_type_12_22, box_2_type_12_23, box_2_type_12_24, box_2_type_12_25,
             box_2_type_12_26, box_2_type_12_27, box_2_type_12_28, box_2_type_12_29, box_2_type_12_30, box_2_type_12_31,
             box_2_type_12_32, box_2_type_12_33, box_2_type_12_34, box_2_type_12_35, box_2_type_12_36],
            [box_2_type_13_20, box_2_type_13_21, box_2_type_13_22, box_2_type_13_23, box_2_type_13_24, box_2_type_13_25,
             box_2_type_13_26, box_2_type_13_27, box_2_type_13_28, box_2_type_13_29, box_2_type_13_30, box_2_type_13_31,
             box_2_type_13_32, box_2_type_13_33, box_2_type_13_34, box_2_type_13_35, box_2_type_13_36],
            [box_2_type_14_20, box_2_type_14_21, box_2_type_14_22, box_2_type_14_23, box_2_type_14_24, box_2_type_14_25,
             box_2_type_14_26, box_2_type_14_27, box_2_type_14_28, box_2_type_14_29, box_2_type_14_30, box_2_type_14_31,
             box_2_type_14_32, box_2_type_14_33, box_2_type_14_34, box_2_type_14_35, box_2_type_14_36],
            [box_2_type_15_20, box_2_type_15_21, box_2_type_15_22, box_2_type_15_23, box_2_type_15_24, box_2_type_15_25,
             box_2_type_15_26, box_2_type_15_27, box_2_type_15_28, box_2_type_15_29, box_2_type_15_30, box_2_type_15_31,
             box_2_type_15_32, box_2_type_15_33, box_2_type_15_34, box_2_type_15_35, box_2_type_15_36],
            [box_2_type_16_20, box_2_type_16_21, box_2_type_16_22, box_2_type_16_23, box_2_type_16_24, box_2_type_16_25,
             box_2_type_16_26, box_2_type_16_27, box_2_type_16_28, box_2_type_16_29, box_2_type_16_30, box_2_type_16_31,
             box_2_type_16_32, box_2_type_16_33, box_2_type_16_34, box_2_type_16_35, box_2_type_16_36],
            [box_2_type_17_20, box_2_type_17_21, box_2_type_17_22, box_2_type_17_23, box_2_type_17_24, box_2_type_17_25,
             box_2_type_17_26, box_2_type_17_27, box_2_type_17_28, box_2_type_17_29, box_2_type_17_30, box_2_type_17_31,
             box_2_type_17_32, box_2_type_17_33, box_2_type_17_34, box_2_type_17_35, box_2_type_17_36],
            [box_2_type_18_20, box_2_type_18_21, box_2_type_18_22, box_2_type_18_23, box_2_type_18_24, box_2_type_18_25,
             box_2_type_18_26, box_2_type_18_27, box_2_type_18_28, box_2_type_18_29, box_2_type_18_30, box_2_type_18_31,
             box_2_type_18_32, box_2_type_18_33, box_2_type_18_34, box_2_type_18_35, box_2_type_18_36]
            ]
        print(start)
        for x in range(2, 19):
            for y in range(20, 37):
                if x + 18 == y:
                    pass
                else:
                    departed = x
                    arrived = y
                    driver = webdriver.Chrome('chromedriver.exe')  # ,chrome_options=options)
                    time.sleep(1)
                    driver.get('https://etk.srail.co.kr/main.do#n')
                    elem = driver.find_element_by_id('wrap')
                    elem = elem.find_element_by_class_name('container-e')
                    elem = elem.find_element_by_class_name('clear')
                    elem = elem.find_element_by_class_name('drop100p')
                    elem = elem.find_element_by_id('search-form')
                    # 출발역 도착역 접근하는 코드 기본 큰 폼
                    # 아래 코드가 출발역 il 태그에 접근하는 문
                    elem = elem.find_elements_by_class_name('ui-icon')
                    ac = ActionChains(driver)
                    ac.move_to_element(elem[0])
                    ac.click()
                    ac.perform()
                    # 리스트 중에 출발지 선택
                    elem1 = driver.find_element_by_class_name('ui-selectmenu-open')
                    elem2 = elem1.find_element_by_id('dptRsStnCd-menu')
                    elem2 = elem2.find_element_by_id('ui-id-%s' % (departed))
                    ac = ActionChains(driver)
                    ac.move_to_element(elem2)
                    ac.click()
                    ac.perform()
                    # 다시 드라이브에서 가져와서 다시 접근 >> 다시 코드 줄일수 잇음 코드가 중복되엇기에
                    elem = driver.find_element_by_id('wrap')
                    elem = elem.find_element_by_class_name('container-e')
                    elem = elem.find_element_by_class_name('clear')
                    elem = elem.find_element_by_class_name('drop100p')
                    elem = elem.find_element_by_id('search-form')
                    elem = elem.find_elements_by_class_name('ui-icon')
                    # elem 안에 출발지 도착지 선택할수 잇는 정보가 잇기에 출발지는 0 도착지는 1로 하면 선택 가능하다
                    ac = ActionChains(driver)
                    ac.move_to_element(elem[1])
                    ac.click()
                    ac.perform()
                    # 도착역 선택 버튼
                    elem1 = driver.find_element_by_class_name('ui-selectmenu-open')
                    elem1 = elem1.find_element_by_id('arvRsStnCd-menu')
                    elem1 = elem1.find_element_by_id('ui-id-%d' % (arrived))
                    ac = ActionChains(driver)
                    ac.move_to_element(elem1)
                    ac.click()
                    ac.perform()
                    # 조회하기 클릭 버튼
                    elem = driver.find_element_by_id('wrap')
                    elem = elem.find_element_by_class_name('container-e')
                    elem = elem.find_element_by_class_name('clear')
                    elem = elem.find_element_by_class_name('drop100p')
                    elem = elem.find_element_by_class_name('btn_burgundy_dark')
                    ac = ActionChains(driver)
                    ac.move_to_element(elem)
                    ac.click()
                    ac.perform()
                    # 데이터를 로드할때까지 시간이 걸리기 때문에 로딩할때까지 3초정도 기다린다
                    count_Day = 0
                    for i in range(80):
                        time.sleep(2)
                        # 시간을 담는 box , 기차 타입을 담는 type_boxes
                        box = find_text()
                        type_boxes, length = type_train()
                        #                         print(length)
                        if (length != 10 or count_Day != 0):
                            # 내일 데이터 가져오는 코드
                            if (count_Day == 1 and length == 10):
                                try:
                                    # 시간을 담을 18*18의 변수에 담을 정보를 입력 리스트 +리스트
                                    big_box_1[x - 2][y - 20] = big_box_1[x - 2][y - 20] + box
                                    # 기차 타입을 담을 18*18의 변수에 담을 정보를 입력 리스트 +리스트
                                    big_type_box_1[x - 2][y - 20] = big_type_box_1[x - 2][y - 20] + type_boxes
                                except TypeError:
                                    pass
                                time.sleep(1)
                                elem1 = driver.find_element_by_id('wrap')
                                elem1 = driver.find_element_by_class_name('container-e')
                                elem1 = driver.find_element_by_class_name('sub_wrap')
                                elem1 = driver.find_element_by_class_name('etk-seat')
                                elem1 = driver.find_element_by_id('result-form')
                                elem1 = elem1.find_elements_by_class_name('tal_r')
                                elem1 = elem1[1].find_element_by_class_name('btn_burgundy_dark')
                                # 다음 버튼 클릭하기
                                ac = ActionChains(driver)
                                ac.move_to_element(elem1)
                                ac.click()
                                ac.perform()
                            # 모레 데이터 가져오는 코드
                            elif (count_Day == 2 and length == 10):
                                try:
                                    # 시간을 담을 18*18의 변수에 담을 정보를 입력 리스트 +리스트
                                    big_box_2[x - 2][y - 20] = big_box_2[x - 2][y - 20] + box
                                    # 기차 타입을 담을 18*18의 변수에 담을 정보를 입력 리스트 +리스트
                                    big_type_box_2[x - 2][y - 20] = big_type_box_2[x - 2][y - 20] + type_boxes
                                except TypeError:
                                    pass
                                time.sleep(1)
                                elem1 = driver.find_element_by_class_name('container-e')
                                elem1 = driver.find_element_by_class_name('sub_wrap')
                                elem1 = driver.find_element_by_class_name('etk-seat')
                                elem1 = driver.find_element_by_id('result-form')
                                elem1 = elem1.find_elements_by_class_name('tal_r')
                                elem1 = elem1[1].find_element_by_class_name('btn_burgundy_dark')
                                # 다음 버튼 클릭하기
                                ac = ActionChains(driver)
                                ac.move_to_element(elem1)
                                ac.click()
                                ac.perform()
                            if length != 10:
                                if count_Day == 0:
                                    try:
                                        # 시간을 담을 18*18의 변수에 담을 정보를 입력 리스트 +리스트
                                        big_box[x - 2][y - 20] = big_box[x - 2][y - 20] + box
                                        # 기차 타입을 담을 18*18의 변수에 담을 정보를 입력 리스트 +리스트
                                        big_type_box[x - 2][y - 20] = big_type_box[x - 2][y - 20] + type_boxes
                                    except TypeError:
                                        pass

                                    time.sleep(1)
                                    try:
                                        elem1 = driver.find_element_by_class_name('container-e')
                                        elem1 = driver.find_element_by_class_name('sub_wrap')
                                        elem1 = driver.find_element_by_class_name('etk-seat')
                                        elem1 = driver.find_element_by_id('result-form')
                                        elem1 = elem1.find_elements_by_class_name('tal_r')
                                        elem1 = elem1[1].find_element_by_class_name('btn_burgundy_dark')
                                        # 다음 버튼 클릭하기
                                        ac = ActionChains(driver)
                                        ac.move_to_element(elem1)
                                        ac.click()
                                        ac.perform()
                                        count_Day = count_Day + 1
                                    except IndexError:
                                        break
                                elif count_Day == 1:
                                    try:
                                        # 시간을 담을 18*18의 변수에 담을 정보를 입력 리스트 +리스트
                                        big_box_1[x - 2][y - 20] = big_box_1[x - 2][y - 20] + box
                                        # 기차 타입을 담을 18*18의 변수에 담을 정보를 입력 리스트 +리스트
                                        big_type_box_1[x - 2][y - 20] = big_type_box_1[x - 2][y - 20] + type_boxes
                                    except TypeError:
                                        pass
                                    time.sleep(1)
                                    elem1 = driver.find_element_by_class_name('container-e')
                                    elem1 = driver.find_element_by_class_name('sub_wrap')
                                    elem1 = driver.find_element_by_class_name('etk-seat')
                                    elem1 = driver.find_element_by_id('result-form')
                                    elem1 = elem1.find_elements_by_class_name('tal_r')
                                    elem1 = elem1[1].find_element_by_class_name('btn_burgundy_dark')
                                    # 다음 버튼 클릭하기
                                    ac = ActionChains(driver)
                                    ac.move_to_element(elem1)
                                    ac.click()
                                    ac.perform()
                                    count_Day = count_Day + 1
                                elif count_Day == 2:
                                    try:
                                        # 시간을 담을 18*18의 변수에 담을 정보를 입력 리스트 +리스트
                                        big_box_2[x - 2][y - 20] = big_box_2[x - 2][y - 20] + box
                                        # 기차 타입을 담을 18*18의 변수에 담을 정보를 입력 리스트 +리스트
                                        big_type_box_2[x - 2][y - 20] = big_type_box_2[x - 2][y - 20] + type_boxes
                                    except TypeError:
                                        pass
                                    time.sleep(1)
                                    break
                        # 당일 시실간 데이터 저장
                        else:
                            try:
                                # 시간을 담을 18*18의 변수에 담을 정보를 입력 리스트 +리스트
                                big_box[x - 2][y - 20] = big_box[x - 2][y - 20] + box
                                # 기차 타입을 담을 18*18의 변수에 담을 정보를 입력 리스트 +리스트
                                big_type_box[x - 2][y - 20] = big_type_box[x - 2][y - 20] + type_boxes
                            except TypeError:
                                pass
                            time.sleep(1)
                            elem1 = driver.find_element_by_id('wrap')
                            elem1 = driver.find_element_by_class_name('container-e')
                            elem1 = driver.find_element_by_class_name('sub_wrap')
                            elem1 = driver.find_element_by_class_name('etk-seat')
                            elem1 = driver.find_element_by_id('result-form')
                            elem1 = elem1.find_elements_by_class_name('tal_r')
                            elem1 = elem1[1].find_element_by_class_name('btn_burgundy_dark')
                            # 다음 버튼 클릭하기
                            ac = ActionChains(driver)
                            ac.move_to_element(elem1)
                            ac.click()
                            ac.perform()
                    driver.quit()
        ###########################################################################################
        # 오늘 데이터에 대해서
        print('오늘 데이터 저장')
        for row in range(len(big_box)):
            # pandas의 DataFrame형태를 만들기전에 리스트를 배열로 만들고 전치 시킨다
            test = np.array(big_box[row]).T
            test_type = np.array(big_type_box[row]).T
            # 이 배열들이 각각 안맞는 사이즈 이기때문에 dataFrame형태로 만들면 오류가 발생한다
            # 그러므로 제일 큰 배열의 크기를 맞쳐서 값을 1로 다채운 2차원 배열을 만든다
            blank_box = np.ones((len(test), max_size(test)), dtype=np.object)
            blank_type_box = np.ones((len(test), max_size(test)), dtype=np.object)
            # test의 배열 크기나 test_type의 크기는 같기 때문에 어디 넣든 상관없다
            # 2차원에서 axis =1 축의 크기가 18개가 i
            # 2차원에서 axis =2 축의 크기가 18개가 j
            # 접근해서 아까 만들엇던 배열을 수정하는데 값을 우리가 얻어온 배열을 넣어준다
            # 그러면서 3차원 형태로 변경해주는 역할을 한다
            for i in range(len(test)):
                for j in range(len(blank_box[1])):
                    try:
                        blank_box[i][j] = test[i][j]
                        blank_type_box[i][j] = test_type[i][j]
                    except IndexError:
                        pass
            # 2차원인데 3차원 같은 배열을 만들엇으면
            # 그 배열의 첫번째 축의 길이은 18개 역이므로 18을 가지고
            # 딕셔너리 형태로 바꿔주는데 이때 namebox의 인덱스 값을 가져와서 값을 넣어준다
            # 아래도 마찬가지로 한다
            for idx in range(len(blank_box)):
                dic[name_box[idx]] = blank_box[idx]
                dic_type[name_box[idx]] = blank_type_box[idx]
            # 이젠 DataFrame 형태로 변형해준다
            train = pd.DataFrame(dic)
            train_type = pd.DataFrame(dic_type)
            # name_box에 들어잇는 영어 이름 역을 가져와서 값이 1인것을 비교하고 값이 True인 애들은
            # blank라고 값을 넣어둔다
            for data in name_box:
                train.loc[train[data] == 1, data] = 'blank'
                train_type.loc[train_type[data] == 1, data] = 'blank'
            # 저장된 엑셀 파일은 저장한다
            train.to_csv("train/today/SRT_%s.csv" % (name_box[row]), index=False)
            train_type.to_csv("train/today/SRT_type_%s.csv" % (name_box[row]), index=False)
        time.sleep(5)

        print('내일 데이터 저장')
        # 내일 데이터를 가져올때
        for row in range(len(big_box_1)):
            # pandas의 DataFrame형태를 만들기전에 리스트를 배열로 만들고 전치 시킨다
            test_1 = np.array(big_box_1[row]).T
            test_type_1 = np.array(big_type_box_1[row]).T
            # 이 배열들이 각각 안맞는 사이즈 이기때문에 dataFrame형태로 만들면 오류가 발생한다
            # 그러므로 제일 큰 배열의 크기를 맞쳐서 값을 1로 다채운 2차원 배열을 만든다
            blank_box = np.ones((len(test_1), max_size(test_1)), dtype=np.object)
            blank_type_box = np.ones((len(test_1), max_size(test_1)), dtype=np.object)
            # test의 배열 크기나 test_type의 크기는 같기 때문에 어디 넣든 상관없다
            # 2차원에서 axis =1 축의 크기가 18개가 i
            # 2차원에서 axis =2 축의 크기가 18개가 j
            # 접근해서 아까 만들엇던 배열을 수정하는데 값을 우리가 얻어온 배열을 넣어준다
            # 그러면서 3차원 형태로 변경해주는 역할을 한다
            for i in range(len(test_1)):
                for j in range(len(blank_box[1])):
                    try:
                        blank_box[i][j] = test_1[i][j]
                        blank_type_box[i][j] = test_type_1[i][j]
                    except:
                        pass
            # 2차원인데 3차원 같은 배열을 만들엇으면
            # 그 배열의 첫번째 축의 길이은 18개 역이므로 18을 가지고
            # 딕셔너리 형태로 바꿔주는데 이때 namebox의 인덱스 값을 가져와서 값을 넣어준다
            # 아래도 마찬가지로 한다
            for idx in range(len(blank_box)):
                dic_1[name_box[idx]] = blank_box[idx]
                dic_type_1[name_box[idx]] = blank_type_box[idx]
            # 이젠 DataFrame 형태로 변형해준다
            train = pd.DataFrame(dic_1)
            train_type = pd.DataFrame(dic_type_1)
            # name_box에 들어잇는 영어 이름 역을 가져와서 값이 1인것을 비교하고 값이 True인 애들은
            # blank라고 값을 넣어둔다
            for data in name_box:
                train.loc[train[data] == 1, data] = 'blank'
                train_type.loc[train_type[data] == 1, data] = 'blank'
            # 저장된 엑셀 파일은 저장한다
            train.to_csv("train/tomorrow/SRT_%s.csv" % (name_box[row]), index=False)
            train_type.to_csv("train/tomorrow/SRT_type_%s.csv" % (name_box[row]), index=False)
        time.sleep(5)

        print('모레 데이터 저장')
        # 모레 데이터를 가져올때
        for row in range(len(big_box_2)):
            # pandas의 DataFrame형태를 만들기전에 리스트를 배열로 만들고 전치 시킨다
            test_2 = np.array(big_box_2[row]).T
            test_type_2 = np.array(big_type_box_2[row]).T
            # 이 배열들이 각각 안맞는 사이즈 이기때문에 dataFrame형태로 만들면 오류가 발생한다
            # 그러므로 제일 큰 배열의 크기를 맞쳐서 값을 1로 다채운 2차원 배열을 만든다
            blank_box = np.ones((len(test_2), max_size(test_2)), dtype=np.object)
            blank_type_box = np.ones((len(test_2), max_size(test_2)), dtype=np.object)
            # test의 배열 크기나 test_type의 크기는 같기 때문에 어디 넣든 상관없다
            # 2차원에서 axis =1 축의 크기가 18개가 i
            # 2차원에서 axis =2 축의 크기가 18개가 j
            # 접근해서 아까 만들엇던 배열을 수정하는데 값을 우리가 얻어온 배열을 넣어준다
            # 그러면서 3차원 형태로 변경해주는 역할을 한다
            for i in range(len(test_2)):
                for j in range(len(blank_box[1])):
                    try:
                        blank_box[i][j] = test_2[i][j]
                        blank_type_box[i][j] = test_type_2[i][j]
                    except:
                        pass
            # 2차원인데 3차원 같은 배열을 만들엇으면
            # 그 배열의 첫번째 축의 길이은 18개 역이므로 18을 가지고
            # 딕셔너리 형태로 바꿔주는데 이때 namebox의 인덱스 값을 가져와서 값을 넣어준다
            # 아래도 마찬가지로 한다
            for idx in range(len(blank_box)):
                dic_2[name_box[idx]] = blank_box[idx]
                dic_type_2[name_box[idx]] = blank_type_box[idx]
            # 이젠 DataFrame 형태로 변형해준다
            train = pd.DataFrame(dic_2)
            train_type = pd.DataFrame(dic_type_2)
            # name_box에 들어잇는 영어 이름 역을 가져와서 값이 1인것을 비교하고 값이 True인 애들은
            # blank라고 값을 넣어둔다
            for data in name_box:
                train.loc[train[data] == 1, data] = 'blank'
                train_type.loc[train_type[data] == 1, data] = 'blank'
            # 저장된 엑셀 파일은 저장한다
            train.to_csv("train/tomorrowAdd/SRT_%s.csv" % (name_box[row]), index=False)
            train_type.to_csv("train/tomorrowAdd/SRT_type_%s.csv" % (name_box[row]), index=False)
        time.sleep(5)
        #############################################################################################
        print('오늘')
        # 시간 정보를 담고잇는 엑셀 파일을 읽어서 데이터를 전처리 한다
        # 시간 , 분으로 구분해서 하는데 비교 할수잇게 형태를 숫자로 변형한다
        for iw in range(len(name_box)):
            train = pd.read_csv('train/today/SRT_%s.csv' % (name_box[iw]))
            w, h = train.shape
            for idx in range(len(name_box)):
                hours = []
                minmut = []
                for i in range(w):
                    try:
                        h, m = train[name_box[idx]][i].split(':')
                        hours.append(int(h))
                        minmut.append(int(m))
                    except ValueError:
                        # blank는 split함수로 나누어도 값이 하나만 리턴되서 오류가 발생한다
                        # 그래서 그것을 이용해서 각 리스트 변수에 100이라는 임이의 숫자를 넣는다
                        minmut.append(100)
                        hours.append(100)
                # 딕셔너리 형태를 만들기위해 리스트를 배열로 만들고 전치 시킨다
                dicts[name_boxs[idx]] = np.array(hours).T
                dicts[name_boxs[idx + 17]] = np.array(minmut).T
                # 데이터 프레임 형태로 변환밑 엑셀 저장
            train = pd.DataFrame(dicts)
            train.to_csv("train/today/SRT_time_%s.csv" % (name_box[iw]), index=False)

        # 내일 데이터 전처리
        # 시간 정보를 담고잇는 엑셀 파일을 읽어서 데이터를 전처리 한다
        # 시간 , 분으로 구분해서 하는데 비교 할수잇게 형태를 숫자로 변형한다
        print('내일')
        for iw in range(len(name_box)):
            train = pd.read_csv('train/tomorrow/SRT_%s.csv' % (name_box[iw]))
            w, h = train.shape
            for idx in range(len(name_box)):
                hours = []
                minmut = []
                for i in range(w):
                    try:
                        h, m = train[name_box[idx]][i].split(':')
                        hours.append(int(h))
                        minmut.append(int(m))
                    except ValueError:
                        # blank는 split함수로 나누어도 값이 하나만 리턴되서 오류가 발생한다
                        # 그래서 그것을 이용해서 각 리스트 변수에 100이라는 임이의 숫자를 넣는다
                        minmut.append(100)
                        hours.append(100)
                # 딕셔너리 형태를 만들기위해 리스트를 배열로 만들고 전치 시킨다
                dicts_1[name_boxs[idx]] = np.array(hours).T
                dicts_1[name_boxs[idx + 17]] = np.array(minmut).T
                # 데이터 프레임 형태로 변환밑 엑셀 저장
            train = pd.DataFrame(dicts_1)
            train.to_csv("train/tomorrow/SRT_time_%s.csv" % (name_box[iw]), index=False)

        # 모레 데이터 전처리
        # 시간 정보를 담고잇는 엑셀 파일을 읽어서 데이터를 전처리 한다
        # 시간 , 분으로 구분해서 하는데 비교 할수잇게 형태를 숫자로 변형한다
        print('모레')
        for iw in range(len(name_box)):
            train = pd.read_csv('train/tomorrowAdd/SRT_%s.csv' % (name_box[iw]))
            w, h = train.shape
            for idx in range(len(name_box)):
                hours = []
                minmut = []
                for i in range(w):
                    try:
                        h, m = train[name_box[idx]][i].split(':')
                        hours.append(int(h))
                        minmut.append(int(m))
                    except ValueError:
                        # blank는 split함수로 나누어도 값이 하나만 리턴되서 오류가 발생한다
                        # 그래서 그것을 이용해서 각 리스트 변수에 100이라는 임이의 숫자를 넣는다
                        minmut.append(100)
                        hours.append(100)
                # 딕셔너리 형태를 만들기위해 리스트를 배열로 만들고 전치 시킨다
                dicts_2[name_boxs[idx]] = np.array(hours).T
                dicts_2[name_boxs[idx + 17]] = np.array(minmut).T
                # 데이터 프레임 형태로 변환밑 엑셀 저장
            train = pd.DataFrame(dicts_2)
            train.to_csv("train/tomorrowAdd/SRT_time_%s.csv" % (name_box[iw]), index=False)

        # 종료 시점을 시간으로 알린다
        finish = datetime.datetime.now()
        finish = finish.hour
        print(finish)
        print('완료')
        time.sleep(60 * 10)
    else:
        print("혼자 돌아가는 중입니다")
        time.sleep(60 * 60)
        pass



