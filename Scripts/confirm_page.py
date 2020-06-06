from selenium.webdriver.common.by import By

from Base.page import Page

# 首页关闭更新
Page.get_home().close_update()
# 首页 -我的
Page.get_home().click_my_btn()
# 个人中心 -登录注册
Page.get_person().click_login_sigin()
# 登录操作
Page.get_login().login("13488834010", "159357")

# # 定位提示消息
# mess_xpath = (By.XPATH, "//*[contains(@text,'错误')]")
# # 任意页面类都继承了Base类 所以可以调用Base类方法
# message = Page.get_setting().search_ele(mess_xpath, timeout=3, poll_frequency=0.3).text
print("提示消息:", Page.get_login().get_toast("错误"))

# 点击返回按钮
Page.get_login().login_return()

# # 登录确认按钮
# Page.get_login().login_acc()
# # 个人中心 -打印用户名
# print("用户名:", Page.get_person().get_user_name())
# # 个人中心 -设置
# Page.get_person().click_setting_btn()
# # 设置页面 -退出
# Page.get_setting().logout()
