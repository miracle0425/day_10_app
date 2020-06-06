from Base.base import Base
from Page.pageElements import PageElements


class LoginPage(Base):

    def __init__(self):
        super().__init__()

    def login(self, phone, password):
        """
        登录操作
        :param phone: 手机号
        :param password: 密码
        :return:
        """
        # 输入手机号
        self.send_ele(PageElements.login_account_id, phone)
        # 输入密码
        self.send_ele(PageElements.login_passwd_id, password)
        # 点击登录按钮
        self.click_ele(PageElements.login_sub_btn_id)

    def login_return(self):
        """登录页面返回"""
        self.click_ele(PageElements.login_return_btn_id)

    def login_acc(self):
        """登录成功确认按钮"""
        self.click_ele(PageElements.login_suc_acc_btn_id)
