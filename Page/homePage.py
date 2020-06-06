from Base.base import Base
from Page.pageElements import PageElements
from selenium.common.exceptions import TimeoutException


class HomePage(Base):

    def __init__(self):
        super().__init__()

    def close_update(self):
        """关闭更新按钮"""
        try:
            self.click_ele(PageElements.home_update_dis_btn_xpath)
        except TimeoutException:
            print("当前版本app 没有提示更新操作")

    def click_my_btn(self):
        """点击我的"""
        self.click_ele(PageElements.home_my_btn_id)
