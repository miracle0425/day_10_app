import yaml, os


class AnalysisData:

    @classmethod
    def get_yaml_data(cls, name):
        """解析yaml文件"""
        # 打开
        with open("./Data" + os.sep + name, "r", encoding="utf-8") as f:
            # 返回解析数据
            return yaml.safe_load(f)
