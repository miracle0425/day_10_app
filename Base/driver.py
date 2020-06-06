from appium import webdriver


class Driver:
    # app驱动
    app_driver = None

    @classmethod
    def get_app_driver(cls):
        """声明driver"""
        if not cls.app_driver:
            desired_caps = {
                'platformName': "Android",
                'platformVersion': '5.1',
                'deviceName': 'sanxing',
                'resetKeyboard': True,
                'unicodeKeyboard': True,
                'automationName': 'uiautomator2',
                'appPackage': 'com.bjcsxq.chat.carfriend',
                'appActivity': '.module_main.activity.MainActivity'
            }
            # 声明driver
            cls.app_driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
            # 返回
            return cls.app_driver
        else:
            return cls.app_driver

    @classmethod
    def quit_app_driver(cls):
        """退出driver"""
        if cls.app_driver:
            # 退出
            cls.app_driver.quit()
            # 置为None
            cls.app_driver = None
