import allure


class Test_001:

    def test_001(self):
        """添加一个截图到当前测试方法"""
        # 读取图片 rb:二进制
        with open("./Image/111.png", "rb") as f:
            # 添加图片到报告
            allure.attach(f.read(), name="截图", attachment_type=allure.attachment_type.PNG)
