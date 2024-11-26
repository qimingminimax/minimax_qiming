from distutils.core import  setup
import setuptools
packages = ['minimax_qiming']# 唯一的包名，自己取名
setup(name='minimax_qiming',
	version='1.1.5',
	author='qiming',
    packages=packages, # 包含所有包
    package_data={
        'minimax_qiming': ['data/*.csv'],  # 包含 CSV 文件
    },
    )
