# -*- coding: UTF-8 -*-
from DBOperator.dbException import *
import shutil
import csv
import os


class CSVOperator:
    """
    操作CSV数据库的类
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        单例模式创建 CSVOperator
        :param args:
        :param kwargs:
        :return:
        """
        if not cls._instance:
            cls._instance = super(CSVOperator, cls).__new__(cls)
        return cls._instance

    def __init__(self, database_name):

        # 设定数据库名称
        self.databaseName = database_name
        # 判断数据库文件夹是否存在,如果不存在则创建
        self.databasePath = "\\".join(["D:", "database", self.databaseName]) + "\\"
        if not os.path.exists(self.databasePath):
            os.makedirs(self.databasePath)

    @staticmethod
    def roll_back(backup_path):
        """
        回滚数据库。
        :param backup_path:
        """
        original_path = ".".join(backup_path.split(".")[0:-1])
        os.remove(original_path)
        os.rename(backup_path, original_path)

    @staticmethod
    def backup(original_path):
        """
        对要修改数据库进行备份。
        :param original_path:
        """
        if os.path.exists(original_path):
            backup_path = original_path + ".bak"
            shutil.copy(original_path, backup_path)

    def save_data(self, filename, data, mode="a"):
        """
        存储数据，以.csv文件形式存储。
        :param filename: 文件名称，无需.csv后缀
        :param data: 可迭代对象
        :param mode: 模式 str，制定数据库写入模式，默认追加
        """
        complete_path = self.databasePath + filename + ".csv"
        # 在写入数据库前，先对目标库原始版本进行复制备份，以便以后回滚
        self.backup(complete_path)

        with open(complete_path, mode, newline="", encoding="utf-8") as f:
            # 判断data是否为可迭代对象，否则抛出异常
            if not isinstance(data, list):
                raise ClassErrorException("variable data")
            csv.writer(f).writerows(data)

    def read_data(self, filename):
        """
        读取数据并返回。
        :param filename: 文件名称，无需.csv后缀
        :return: 可迭代对象 reader
        """
        complete_path = self.databasePath + filename + ".csv"
        # 判断要读取的文件是否存在，不存在则抛出异常
        if not os.path.exists(complete_path):
            raise FileNotFoundError(complete_path)
        with open(complete_path, "r") as f:
            return csv.reader(f)
