# coding: utf-8
from setuptools import setup


setup(name='assembla',
      version='0.0.2',
      description='Assembla API Wrapper',
      author=u'QMágico',
      test_suite='test.testall.suite',
      include_package_data=True,
      packages=['assembla'],
      install_requires=['requests'])
