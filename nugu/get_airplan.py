from selenium import webdriver
import pandas as pd
import numpy as np
import time,datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os


def calender(first_day, last_day):
    week1_6, week1_0, week1_1, week1_2, week1_3, week1_4, week1_5 = 0, 0, 0, 0, 0, 0, 0
    week2_6, week2_0, week2_1, week2_2, week2_3, week2_4, week2_5 = 0, 0, 0, 0, 0, 0, 0
    week3_6, week3_0, week3_1, week3_2, week3_3, week3_4, week3_5 = 0, 0, 0, 0, 0, 0, 0
    week4_6, week4_0, week4_1, week4_2, week4_3, week4_4, week4_5 = 0, 0, 0, 0, 0, 0, 0
    week5_6, week5_0, week5_1, week5_2, week5_3, week5_4, week5_5 = 0, 0, 0, 0, 0, 0, 0
    week6_6, week6_0, week6_1, week6_2, week6_3, week6_4, week6_5 = 0, 0, 0, 0, 0, 0, 0
    weekes = [[week1_6, week1_0, week1_1, week1_2, week1_3, week1_4, week1_5],
              [week2_6, week2_0, week2_1, week2_2, week2_3, week2_4, week2_5],
              [week3_6, week3_0, week3_1, week3_2, week3_3, week3_4, week3_5],
              [week4_6, week4_0, week4_1, week4_2, week4_3, week4_4, week4_5],
              [week5_6, week5_0, week5_1, week5_2, week5_3, week5_4, week5_5],
              [week6_6, week6_0, week6_1, week6_2, week6_3, week6_4, week6_5],
              ]
    axis_x = [-70, -35, 0, 35, 70, 105, 140]
    axis_y = [120, 150, 180, 210, 240, 290]
    a = np.arange(1, last_day + 1)
    if first_day == 6:
        num = 0
        try:
            for cc in range(first_day + 1):
                weekes[0][cc] = a[cc]
            for j in range(1, 7):
                num = j * 7
                for jj in range(7):
                    weekes[j][jj] = a[num + jj]
        except IndexError:
            pass

    elif first_day == 0:
        num = 0
        try:
            for cc in range(first_day + 1, 7):
                weekes[0][cc] = a[cc - 1]
            for j in range(1, 6):
                num = j * 7
                for jj in range(7):
                    weekes[j][jj] = a[num - first_day + jj - 1]
        except IndexError:
            pass

    elif first_day == 1:
        num = 0
        try:
            for cc in range(first_day + 1, 7):
                weekes[0][cc] = a[cc - 2]
            for j in range(1, 6):
                num = j * 7
                for jj in range(7):
                    weekes[j][jj] = a[num - first_day + jj - 1]
        except IndexError:
            pass

    elif first_day == 2:
        num = 0
        try:
            for cc in range(first_day + 1, 7):
                weekes[0][cc] = a[cc - 3]
            for j in range(1, 6):
                num = j * 7
                for jj in range(7):
                    weekes[j][jj] = a[num - first_day + jj - 1]
        except IndexError:
            pass

    elif first_day == 3:
        num = 0
        try:
            for cc in range(first_day + 1, 7):
                weekes[0][cc] = a[cc - 4]
            for j in range(1, 6):
                num = j * 7
                print(num)
                for jj in range(7):
                    weekes[j][jj] = a[num - first_day + jj - 1]
        except IndexError:
            pass



    elif first_day == 4:
        num = 0
        try:
            for cc in range(first_day + 1, 7):
                weekes[0][cc] = a[cc - 5]
            for j in range(1, 6):
                num = j * 7
                for jj in range(7):
                    weekes[j][jj] = a[num - first_day + jj - 1]
        except IndexError:
            pass

    else:
        num = 0
        try:
            for cc in range(first_day + 1, 7):
                weekes[0][cc] = a[cc - 6]
            for j in range(1, 6):
                num = j * 7
                for jj in range(7):
                    weekes[j][jj] = a[num - first_day + jj - 1]
        except IndexError:
            pass
    return weekes


while True:
    name_station = ['서울특별시', '부산', '제주도']
    now = datetime.datetime.today()
    day = 1
    first_day = datetime.date(now.year, now.month, day)
    first_day = first_day.weekday()
    print(first_day)
    d = datetime.date(now.year, now.month + 1, day)
    t = datetime.timedelta(days=1)
    k = d - t
    last_day = k.day
    axis_x = [-70, -35, 0, 35, 70, 105, 140]
    axis_y = [110, 150, 180, 210, 240, 290]
    weekes = calender(first_day, last_day)
    now_day = now.day
    for nums in range(7):
        if last_day < (nums + now_day):  # (now.day+num):
            if now.month != 12:
                except_firstday = datetime.date(now.year, now.month + 1, 1)
                except_firstday = except_firstday.weekday()
                except_d = datetime.date(now.year, now.month + 1, 1)
                except_t = datetime.timedelta(days=1)
                except_k = except_d - except_t
                except_lastday = except_k.day
                except_weekes = calender(except_firstday, except_lastday)  # 달력 생성
                result_day = (now_day + nums) - last_day
                for i in range(len(except_weekes)):
                    for j in range(len(except_weekes[0])):
                        if except_weekes[i][j] == result_day:
                            except_find_idx = j
                            except_find_idy = i
                            print(except_find_idx, except_find_idy)
                            print('다음달로 넘어갈때 :', axis_x[except_find_idx], axis_y[except_find_idy])
                            break
            else:
                except_firstday = datetime.date(now.year + 1, 1, 1)
                except_firstday = except_firstday.weekday()
                except_d = datetime.date(now.year + 1, 2, 1)
                except_t = datetime.timedelta(days=1)
                except_k = except_d - except_t
                except_lastday = except_k.day
                except_weekes = calender(except_firstday, except_lastday)
                result_day = (now_day + nums) - last_day
                for i in range(len(except_weekes)):
                    for j in range(len(except_weekes[0])):
                        if except_weekes[i][j] == result_day:
                            except_find_idx = j
                            except_find_idy = i
                            print(except_find_idx, except_find_idy)
                            print('12월일때 : ', axis_x[except_find_idx], axis_y[except_find_idy])
                            break
        else:
            for i in range(len(weekes)):
                for j in range(len(weekes[0])):
                    if weekes[i][j] == (now_day + nums):
                        find_idx = j
                        find_idy = i
                        print('일반', find_idx, find_idy)
                        break

        for num in range(len(name_station)):
            for num1 in range(len(name_station)):
                if name_station[num] == name_station[num1]:
                    pass
                else:
                    options = webdriver.ChromeOptions()
                    options.add_argument('headless')
                    options.add_argument('window-size=1920x1080')
                    options.add_argument("disable-gpu")
                    driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)
                    driver.get('https://kr.trip.com/flights/?allianceid=14887&sid=1621876&ouid=nsd0043451&utm_source=naver&utm_medium=cpc&utm_term=nsd0043451&utm_campaign=flight&n_media=27758&n_query=%EB%B9%84%ED%96%89%EA%B8%B0%ED%91%9C%EC%98%88%EC%95%BD&n_rank=1&n_ad_group=grp-a001-01-000000005306659&n_ad=nad-a001-01-000000053067766&n_keyword_id=nkw-a001-01-000000984968160&n_keyword=%EB%B9%84%ED%96%89%EA%B8%B0%ED%91%9C%EC%98%88%EC%95%BD&n_campaign_type=1&NaPm=ct%3Djrqlt2r4%7Cci%3D0yq0003Yr5vqssTx-1m1%7Ctr%3Dsa%7Chk%3D2dc63f741cefb0576f2b86867fca2d8d49e15524&gclid=CLvDzvnLouACFUWavAodZGgGOg&gclsrc=ds')
                    elem = driver.find_element_by_id('FlightSearchBox')
                    elem11 = elem.find_element_by_id('SearchBoxTabSwitch')
                    elem11 = elem11.find_elements_by_tag_name('a')
                    for i in elem11:
                        if i.text == '편도':
                            ac = ActionChains(driver)
                            ac.move_to_element(i)
                            ac.click()
                            ac.perform()
                            time.sleep(1)
                    elem = driver.find_element_by_id('RoundRoute')
                    elem = driver.find_element_by_class_name('clearfix')
                    elem1 = driver.find_element_by_class_name('s-item-l')
                    elem1 = driver.find_element_by_class_name('ipt-borderless')
                    elem1.send_keys(Keys.DELETE)
                    elem1.send_keys(name_station[num])
                    elem1.send_keys(Keys.RETURN)
                    time.sleep(1)
                    elem2 = driver.find_element_by_class_name('s-item-r')
                    elem2 = elem2.find_element_by_class_name('ipt-borderless')
                    elem2.send_keys(Keys.DELETE)
                    elem2.send_keys(name_station[num1])
                    elem2.send_keys(Keys.RETURN)
                    time.sleep(1)
                    # 출발하는날
                    elem3 = driver.find_element_by_class_name('s-item-cln')
                    elem3 = elem3.find_element_by_class_name('ipt-borderless')
                    try:
                        if str(except_find_idx).isdigit():
                            print('다음달로 넘어갈때 처리반')
                            for i in range(1):
                                print('예외처리1')
                                ac = ActionChains(driver)
                                ac.move_to_element(elem3)
                                ac.click()
                                ac.perform()
                                ac.reset_actions()
                                ac.move_by_offset(37 * 11, 150)
                                ac.click()
                                ac.perform()
                            time.sleep(1)
                            elem3 = driver.find_element_by_class_name('s-item-cln')
                            elem3 = elem3.find_element_by_class_name('ipt-borderless')
                            ac = ActionChains(driver)
                            ac.move_to_element(elem3)
                            ac.click()
                            ac.perform()
                            ac.move_to_element(elem3)
                            #                             print(axis_x[except_find_idx],axis_y[except_find_idy])
                            ac.move_by_offset(axis_x[except_find_idx], axis_y[except_find_idy])
                            ac.click()
                            ac.perform()
                            time.sleep(1)

                    except:
                        ac = ActionChains(driver)
                        ac.move_to_element(elem3)
                        ac.click()
                        ac.perform()
                        time.sleep(1)
                        ac.reset_actions()
                        ac.move_to_element(elem3)
                        ac.move_by_offset(axis_x[find_idx], axis_y[find_idy])
                        ac.click()
                        ac.perform()
                        time.sleep(1)
                        pass
                    elem6 = driver.find_element_by_class_name('search-btn')
                    elem6 = elem6.find_element_by_id('SearchSubmit')
                    ac = ActionChains(driver)
                    ac.move_to_element(elem6)
                    ac.click()
                    ac.perform()
                    time.sleep(10)
                    depart_time = []
                    Name = []
                    price = []
                    elem1111 = driver.find_element_by_class_name('m-result-list')
                    elem22222 = elem1111.find_elements_by_class_name('J_FlightItem')
                    if len(elem22222) != 0:
                        for i in range(len(elem22222)):
                            time.sleep(1)
                            elem = driver.find_element_by_class_name('m-result-list')
                            elem = elem.find_element_by_xpath("//div[@data-index=%d]" % i)
                            elem = elem.find_element_by_class_name('J_FlightItem')

                            elem1 = elem.find_element_by_class_name('result-item-table')
                            elem8 = elem1.find_element_by_class_name('result-airline')
                            elem8 = elem8.find_element_by_class_name("c-result-airline__name")
                            Name1 = elem8.text
                            Name.append(Name1)

                            elem2 = elem1.find_element_by_class_name('result-period')
                            elem2 = elem2.find_element_by_class_name('c-result-period__cell')
                            elem2 = elem2.find_element_by_class_name('c-result-period__depart')
                            elem2 = elem2.find_element_by_class_name('c-result-period__time')
                            depart_time.append(elem2.text[:5])
                            time.sleep(1)

                            elem = driver.find_element_by_class_name('m-result-list')
                            elem = elem.find_element_by_xpath("//div[@data-index=%d]" % i)
                            elem = elem.find_element_by_class_name('J_FlightItem')
                            elem4 = elem.find_element_by_class_name('result-item-con')
                            elem4 = elem4.find_element_by_class_name('result-item-con-status')
                            elem4 = elem4.find_element_by_class_name('result-item-price')
                            elem4 = elem4.find_element_by_class_name('o-price-flight')
                            elem4 = elem4.find_element_by_class_name('o-price-flight__num')
                            price1 = elem4.text
                            price1 = int(''.join(price1.split(',')))
                            price.append(price1)
                        driver.quit()
                    else:
                        driver.quit()
                        Name, depart_time, price = ['blank'], ['blank'], ['blank']
                    print('@@@@@@@@@@@@@@@@@@@' * 2)
                    train = pd.DataFrame({'Name': Name, 'depart_time': depart_time, 'price': price})
                    # os.mkdir('airplan')
                    train['depart_time_hour'], train['depart_time_minute'] = range(train.shape[0]), range(
                        train.shape[0])
                    for i in range(train.shape[0]):
                        train['depart_time_hour'][i], train['depart_time_minute'][i] = train['depart_time'][i].split(
                            ':')
                        train['depart_time_hour'] = train['depart_time_hour'].astype('int64')
                        train['depart_time_minute'] = train['depart_time_minute'].astype('int64')
                    train.sort_values(by=['depart_time_hour', 'depart_time_minute'], ascending=True, inplace=True)
                    train.to_csv('airplan/trip_airplan_%s_%s_%s.csv' % (nums, num, num1), index=False)
        # nums 가 오늘 0 내일 1 이틀뒤 2 3일뒤 3 4일뒤 4 5일뒤 5 6일뒤 6
        # num 출발도시 num1 도착도시
        # 서울  0  부산 1 제주도 2
        # 서울에서 부산 0 _ 1
        print('하루 정보를 다가져왓습니다')
    print('일주일치를 다 가져왓습니다')
    time.sleep(60 * 60)


















