# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-----------------------------------------
@Author: zz
@Email: 21212010059@m.fudan.edu.cn
@Created: 2022/05/11
------------------------------------------
@Modify: 2022/05/11
------------------------------------------
@Description:
"""
from scrapy.cmdline import execute  # 调用此函数可以执行scrapy的脚本
import sys
import os

# 用来设置工程目录，有了它才可以让命令行生效
pa1 = os.path.dirname(os.path.abspath(__file__))
pa2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(pa1)
sys.path.append(pa2)
print(sys.path)


execute(['scarpy', 'crawl', 'android_issuetracker_component'])