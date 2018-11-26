# Python Webdriver 重新使用已经打开的浏览器实例
from selenium.webdriver import Remote
from selenium.webdriver.chrome import options
from selenium.common.exceptions import InvalidArgumentException

class ReuseChrome(Remote):
    def __init__(self,command_executor,session_id):
        self.r_session_id=session_id
        Remote.__init__(self,command_executor=command_executor,desired_capabilities={})
    def start_session(self, capabilities, browser_profile=None):
        #重写start_session方法
        if not isinstance(capabilities,dict):
            raise InvalidArgumentException("Capabilities must be a dictionary")
        if browser_profile:
            if "moz:firefoxOptions" in capabilities:
                capabilities["moz:firefoxOptions"]["profile"]=browser_profile.encoded
            else:
                capabilities.update({'firefox_profile':browser_profile.encoded})
        self.capabilities=options.Options().to_capabilities()
        self.session_id=self.r_session_id
        self.w3c=False

from selenium import webdriver
driver=webdriver.Chrome()
#记录excutor_url和session_id，以便复用session
executor_url=driver.command_executor._url
session_id=driver.session_id
driver.get('http://buyer19.jiaohuilian.com/html/web-login.html')
print(session_id)  #会话sessionID
print(executor_url)#命令执行连接
#假如driver对象不存在，但浏览器未关闭
del driver
#使用ReuseChrome()复用上次的session
driver2=ReuseChrome(command_executor=executor_url,session_id=session_id)
print(driver2.current_url)

# 写完啦，但是不太明白，start_session方法重写那段看不明白嘤嘤嘤


#不打开浏览器运行脚本
from selenium import webdriver
option=webdriver.ChromeOptions()
option.add_argument('headless')
driver=webdriver.Chrome(options=option)

#Chrome下载文件
# download.default_directory:设置下载路径
# profile.default_content_settings.popups:设置为0禁止弹出窗口
options=webdriver.ChromeOptions()
prefs={'profile.default_content_settings.popups':0,'download.default_directory':'F:/pyselenium下载文件'}
options.add_experimental_option('prefs',prefs)
driver=webdriver.Chrome(options=options)


# 下拉滚动条到底部
js="window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(js)
wait3()

# 滑动滚动条到顶部
js="window.scrollTo(0,0)"
driver.execute_script(js)