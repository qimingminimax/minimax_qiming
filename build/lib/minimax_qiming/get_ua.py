import random
import csv
from importlib.resources import files

__all__ = ["get_pc_ua", "get_mobile_ua"]

PC_USER_AGENTS = []

# 动态获取 CSV 文件路径
csv_path = files('minimax_qiming').joinpath('data/export_file.csv')

mb_ua_list = []

# 打开 CSV 文件
with open(csv_path, mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        mb_ua_list.append(row[0])

MOBILE_USER_AGENTS = mb_ua_list

def get_pc_ua() -> str:
    """随机选择一个 PC 端 UserAgent"""
    return random.choice(PC_USER_AGENTS)


def get_mobile_ua() -> str:
    """随机选择一个 MOBILE 端 UserAgent"""
    return random.choice(MOBILE_USER_AGENTS)
