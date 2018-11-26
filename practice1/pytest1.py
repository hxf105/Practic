from selenium import webdriver
browser=webdriver.Chrome()
browser.get('http://buyer19.jiaohuilian.com/')
# browser.quit()
# 笔记：若可以打开谷歌浏览器，但是打不开指定URL，则可能是 chromedriver.exe 的版本与安装的谷歌浏览器版本不对应，找到对应版本问题即解决

from selenium import webdriver
browser=webdriver.Firefox()
browser.maximize_window()
browser.implicitly_wait(30)
browser.get('http://buyer19.jiaohuilian.com/')
# browser.quit()



from selenium import webdriver
# import loginbuyer
from loginbuyer import add

from Practic2.loginbuyer import *


driver=webdriver.Chrome()


# from loginbuyer import login


driver.maximize_window()     #窗口最大化
# driver.set_window_size(1366,768)   #设置窗口大小

# 输入URL
driver.get('http://buyer19.jiaohuilian.com/')
driver.implicitly_wait(30)
# login(driver)
# browser.quit()
# 笔记：若可以打开谷歌浏览器，但是打不开指定URL，则可能是 chromedriver.exe 的版本与安装的谷歌浏览器版本不对应，找到对应版本问题即解决

# 打印元素的宽高
size=driver.find_element_by_id('uname').size
print(size)

# 打印元素的文本内容
text=driver.find_element_by_class_name('itext').text
print(text)

# 返回元素的属性
attribute=driver.find_element_by_id('uname').get_attribute('type')
print(attribute)


findID()


username=driver.find_element_by_id('uname')
password=driver.find_element_by_id('psd')
submit=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[2]/div[1]/div[1]/form/button')

username.send_keys('18292678346')
password.send_keys('123456')


# 输入用户名、密码，登入
driver.find_element_by_id('uname').clear()
driver.find_element_by_id('uname').send_keys('18292678346')
driver.find_element_by_id('psd').clear()
driver.find_element_by_id('psd').send_keys('123456')
driver.implicitly_wait(10)
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[2]/div[1]/div[1]/form/button').click()  #单击登录按钮
driver.implicitly_wait(10)
# driver.find_element_by_xpath('/html/body/div/div/div[3]/div/div/div/div/div/div[1]/div[2]/a[2]').click()    #单击“发布任务监管单”按钮
driver.find_element_by_class_name('auv-btn btn-info').click()
driver.implicitly_wait(10)
# 单击下一步按钮
driver.find_element_by_xpath('//*[@id="task-tab"]/div[2]/div[1]/div[2]/div').click()
driver.implicitly_wait(10)
# 断言：弹出“请选择项目信息”的弹窗
driver.assert_Text('//*[@id="auv-message"]/div[2]/div/div[2]/div')
driver.find_element_by_id('#select-project-button').click()    #单击“选择在建项目”按钮
driver.implicitly_wait(10)
driver.find_element_by_id('search-project-text').send_keys('中交一公局第六工程有限公司')
driver.find_element_by_id('select-project-search-button').click()
driver.implicitly_wait(10)
driver.find_element_by_name('btSelectItem').click()
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[3]/div').click()

# 提交表单
driver.find_element_by_xpath('//*[@id="task-tab"]/div[2]/div[3]/div[3]/div[2]').submit()
driver.implicitly_wait(30)

# driver.quit()


