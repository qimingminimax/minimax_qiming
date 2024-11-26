from distutils.core import  setup
import setuptools
packages = ['minimax_qiming']# 唯一的包名，自己取名
setup(name='qiming',
	version='1.0',
	author='qiming',
    packages=packages, 
    package_dir={'requests': 'requests'},)
