# import sys, os
#
# # 添加python的搜索路径
# sys.path.append(os.getcwd())

from Base.page import Page
from Base.driver import Driver
from Base.analysisData import AnalysisData
import pytest


def login_data():
    """解析数据 组装成[(),()]"""
    # 空列表存数据
    value = []
    # 遍历解析数据
    data = AnalysisData.get_yaml_data("login.yml")
    for i in data.values():
        # 组装数据
        value.append((i.get("phone"), i.get("passwd"), i.get("toast"), i.get("exp")))

    return value


class TestLogin:

    @pytest.fixture(scope="class", autouse=True)
    def goto_person(self):
        """进入个人中心 -依赖一次"""
        # 关闭更新提示
        Page.get_home().close_update()
        # 点击首页我的
        Page.get_home().click_my_btn()

    @pytest.fixture(autouse=True)
    def click_login_sign(self):
        """个人中心点击登录 -每次依赖"""
        Page.get_person().click_login_sigin()

    @pytest.mark.parametrize("phone, passwd, toast, exp", login_data())
    def test_login(self, phone, passwd, toast, exp):
        """
        测试方法
        :param phone: 手机号
        :param passwd: 密码
        :param toast: toast拼接xpath
        :param exp: 预期结果
        :return:
        """
        # 登录
        Page.get_login().login(phone, passwd)
        if toast:
            """预期失败用例"""
            # 获取toast提示消息
            message = Page.get_login().get_toast(toast)
            try:
                # 断言
                assert message == exp
            except AssertionError as e:  # 断言失败异常
                # 截图
                Page.get_setting().screen_png()
                # 抛出断言失败异常
                raise e
            finally:
                # 点击返回按钮
                Page.get_login().login_return()

        else:
            """预期成功用例"""
            # 点击登录确认
            Page.get_login().login_acc()
            # 获取用户名
            username = Page.get_person().get_user_name()
            try:
                # 断言
                assert username == exp
            except AssertionError as e:
                # 截图
                Page.get_setting().screen_png()
                # 抛出断言失败异常
                raise e
            finally:
                # 点击设置
                Page.get_person().click_setting_btn()
                # 退出操作
                Page.get_setting().logout()

    def teardown_class(self):
        """退出driver"""
        Driver.quit_app_driver()
