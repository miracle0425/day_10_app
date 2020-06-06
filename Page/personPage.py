from Base.base import Base
from Page.pageElements import PageElements


class PersonPage(Base):

    def __init__(self):
        super().__init__()

    def click_login_sigin(self):
        """点击登录注册"""
        self.click_ele(PageElements.person_login_sigin_btn_xpath)

    def get_user_name(self):
        """获取用户名"""
        return self.search_ele(PageElements.person_username_id).text

    def click_setting_btn(self):
        """点击设置"""
        # 向上滑动
        self.swipe_screen()
        # 点击设置
        self.click_ele(PageElements.person_setting_btn_id)
