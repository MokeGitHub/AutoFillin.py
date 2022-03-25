from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge

import time
import configparser

if __name__ == '__main__':

    config = configparser.ConfigParser()
    # 后续
    # config['config'] = {
    #     'Login_user_name':'',
    #     'Login_user_password':'',
    #     }
    # # #写入
    # with open('configg.ini','w') as cfg:
    #     config.write(cfg)
    config.read("config.ini")
    Login_user_name = config.get("config", "Login_user_name")
    Login_user_password = config.get("config", "Login_user_password")
    print(Login_user_name,Login_user_password)

    #这里改成你的统一认证用户名和密码
    user_name = Login_user_name
    pwd = Login_user_password
    
    #Google浏览器，定位不准
    #option = webdriver.ChromeOptions() 
    #option.add_argument('headless') # 设置option，不显示浏览器界面
    #browser = webdriver.Chrome(options=option)

    edge_options = EdgeOptions()
    # edge_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    edge_options.use_chromium = True
    edge_options.add_argument('--disable-blink-features=AutomationControlled')
    # 设置无界面模式，也可以添加其它设置
    # edge_options.add_argument('headless')
    browser = Edge(options=edge_options)
    # browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'})
    # 用浏览器打开打卡的网址
    browser.get("https://tyutgs.wjx.cn/user/loginForm.aspx?user_token=RzCs8KPQb4VEfycFVJ8OMztE5FTgJGXpBj0M1NsuatiZzuullOcE2qNhFz1gNCLMf2Rz0IoQ2%2b%2fQvHgDWQRylqbGCNwf9At747llgCvdCidNf%2fEPUf6k4g%3d%3d&returnUrl=%2fuser%2fqlist.aspx%3fu%3d%25e6%2589%258b%25e6%259c%25ba%25e7%2594%25a8%25e6%2588%25b7tivliw38j0y8djcff6vstq%26userSystem%3d1%26systemId%3d55677040")

    # 输用户名和密码
    user_name_input = browser.find_element_by_id("register-user-name")
    user_name_input.send_keys(user_name)
    user_pwd_input = browser.find_element_by_id("register-user-password")
    user_pwd_input.send_keys(pwd)

    login_button = browser.find_element_by_id("btnSubmit")
    ActionChains(browser).move_to_element(login_button).click(login_button).perform()
    time.sleep(3)
    print('点击登陆')

    try:
        # 全体研究生健康状况报告[上午]
        AM_Fillin = browser.find_element_by_link_text('全体研究生健康状况报告[上午]').click()
    except:
        # 全体研究生健康状况报告[下午]
        PM_Fillin = browser.find_element_by_link_text('全体研究生健康状况报告[下午]').click()
    time.sleep(3)

    # 1.当前你是否在校？ 在校
    At_school = browser.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[1]/div[2]/ul/li[1]/label")
    ActionChains(browser).move_to_element(At_school).click(At_school).perform()
    time.sleep(1)

    # 4.您的地理位置：
    Positioning = browser.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[4]/div[2]/label/label/textarea")
    ActionChains(browser).move_to_element(Positioning).click(Positioning).perform()
    time.sleep(30)

    # 6.您的住宿情况为：
    # 迎西校区住宿
    Accommodation = browser.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[6]/div[2]/ul/li[1]/label")
    # # 虎裕校区住宿
    # Positioning = browser.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[6]/div[2]/ul/li[2]/label")
    # # 明向校区住宿
    # Positioning = browser.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[6]/div[2]/ul/li[3]/label")
    # # 校内有宿舍，当前在校外居住
    # Positioning = browser.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[6]/div[2]/ul/li[4]/label")
    # # 校内无宿舍，校外居住
    # Positioning = browser.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[6]/div[2]/ul/li[5]/label")
    ActionChains(browser).move_to_element(Accommodation).click(Accommodation).perform()
    time.sleep(1)

    # 8.当前个人体温：
    Bodytemp = browser.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[8]/div[2]/ul/li[1]/label")
    ActionChains(browser).move_to_element(Bodytemp).click(Bodytemp).perform()
    time.sleep(1)

    # # 9.个人疑似症状：(点击可能会将默认点击的取消)
    # SSII = browser.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[9]/div[2]/ul/li[1]/label")
    # ActionChains(browser).move_to_element(SSII).click(SSII).perform()
    # time.sleep(1)
    
    # # 系统默认已填写
    # # 10.本人或共同居住人近14天是否有中高风险地区或境外旅居史、经停史及此类人员密切接触史：
    # A10 = browser.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[10]/div[2]/ul/li[3]/label")
    # ActionChains(browser).move_to_element(A10).click(A10).perform()
    # time.sleep(1)

    # # 12.本人或共同居住人是否为确诊病例、疑似病例、无症状感染者、密接者、次密接者：
    # A12 = browser.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[12]/div[2]/ul/li[3]/label")
    # ActionChains(browser).move_to_element(A12).click(A12).perform()
    # time.sleep(1)    

    # # 14.本人近14天是否有中高风险地区或境外旅居史、经停史及此类人员密切接触史：
    # A14 = browser.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[14]/div[2]/ul/li[2]/label")
    # ActionChains(browser).move_to_element(A14).click(A14).perform()
    # time.sleep(1)   

    # 16.本次填报信息承诺：
    A16 = browser.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[16]/div[2]/ul/li/label")
    ActionChains(browser).move_to_element(A16).click(A16).perform()
    time.sleep(1)
    
    # 提交
    submit_button = browser.find_element_by_id("submit_button")
    ActionChains(browser).move_to_element(submit_button).click(submit_button).perform()   
    print("填报完毕")

    # 验证
    Validation = browser.find_element_by_xpath("/html/body/div[9]/div[2]/div[2]/div[2]/button")
    ActionChains(browser).move_to_element(Validation).click(Validation).perform()   
    time.sleep(1)

    # 验证2
    Validation2 = browser.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[5]/div[1]/div/div/div[1]/div[1]/div[4]")
    ActionChains(browser).move_to_element(Validation2).click(Validation2).perform()   
    time.sleep(1)


    time.sleep(10)
    #关闭浏览器
    browser.quit()