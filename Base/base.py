from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Base.driver import Driver
import time, os, allure


class Base:

    def __init__(self):
        self.driver = Driver.get_app_driver()

    def search_ele(self, loc, timeout=5, poll_frequency=1.0):
        """
        定位单个元素
        :param loc: 元祖 (By.ID, 属性值) (By.CLASS_NAME, 属性值) (By.XPATH, 属性值)
        :param timeout: 元素搜索超时时间
        :param poll_frequency: 搜索元素间隔
        :return: 定位对象
        """
        #
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    def search_eles(self, loc, timeout=5, poll_frequency=1.0):
        """
        定位一组元素
        :param loc: 元祖 (By.ID, 属性值) (By.CLASS_NAME, 属性值) (By.XPATH, 属性值)
        :param timeout: 元素搜索超时时间
        :param poll_frequency: 搜索元素间隔
        :return: 定位对象列表
        """
        #
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))

    def click_ele(self, loc, timeout=5, poll_frequency=1.0):
        """
        点击元素
        :param loc: 元祖 (By.ID, 属性值) (By.CLASS_NAME, 属性值) (By.XPATH, 属性值)
        :param timeout: 元素搜索超时时间
        :param poll_frequency: 搜索元素间隔
        :return:
        """
        self.search_ele(loc, timeout, poll_frequency).click()

    def send_ele(self, loc, text, timeout=5, poll_frequency=1.0):
        """
        输入内容
        :param loc: 元祖 (By.ID, 属性值) (By.CLASS_NAME, 属性值) (By.XPATH, 属性值)
        :param text: 输入的文本内容
        :param timeout: 元素搜索超时时间
        :param poll_frequency: 搜索元素间隔
        :return:
        """
        # 定位输入框元素
        inp = self.search_ele(loc, timeout, poll_frequency)
        # 清空输入框
        inp.clear()
        # 输入信息
        inp.send_keys(text)

    def swipe_screen(self, tag=1):
        """
        滑动屏幕
        :param tag: 1:向上 2:向下 3:向左 4:向右
        :return:
        """
        # 获取屏幕分辨率 {"width":xx,"height":yy}
        size = self.driver.get_window_size()
        # 宽
        width = size.get("width")
        # 高
        height = size.get("height")
        # 等待1s
        time.sleep(1)

        if tag == 1:  # 向上
            # 宽*50%，高*80%  宽*50%，高*20%
            self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.2, 1500)
        if tag == 2:  # 向下
            # 宽*50%，高*20%  宽*50%，高*80%
            self.driver.swipe(width * 0.5, height * 0.2, width * 0.5, height * 0.8, 1500)
        if tag == 3:  # 向左
            # 宽*80%，高*50%  宽*20%，高*50%
            self.driver.swipe(width * 0.8, height * 0.5, width * 0.2, height * 0.5, 1500)
        if tag == 4:  # 向右
            # 宽*20%，高*50%  宽*80%，高*50%
            self.driver.swipe(width * 0.2, height * 0.5, width * 0.8, height * 0.5, 1500)

    def get_toast(self, mess):
        """
        获取toast提示消息
        :param mess: 拼接xpath语句
        :return:
        """
        # 定位提示消息
        mess_xpath = (By.XPATH, "//*[contains(@text,'%s')]" % mess)
        # 定位toast消息
        return self.search_ele(mess_xpath, timeout=3, poll_frequency=0.3).text

    def screen_png(self):
        """截图"""
        # 当前appiumv1.12.0版本会和uiautomator2有冲突 导致截图会卡死
        # self.driver.get_screenshot_as_file("某个路径截图")

        # ----替代方案 ---
        # 定义图片名字
        png_name = "%d.png" % (int(time.time() * 1000))
        # adb方式进行截图 -截图只能保存到手机上(/sdcard/某个图片)
        os.system("adb shell screencap -p /sdcard/%s" % png_name)
        # adb 从手机在把图片拉回项目
        os.system("adb pull /sdcard/%s ./Image" % png_name)
        # 添加截图到测试报告
        with open("./Image" + os.sep + png_name, "rb") as f:
            allure.attach(f.read(), name="截图", attachment_type=allure.attachment_type.PNG)
