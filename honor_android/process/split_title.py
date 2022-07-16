# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-----------------------------------------
@Author: zz
@Email: 21212010059@m.fudan.edu.cn
@Created: 2022/06/09
------------------------------------------
@Modify: 2022/06/09
------------------------------------------
@Description:
"""
import os
from lxml import etree
from honor_android.util.file_util import FileUtil
from definitions import OUTPUT_DIR
file = os.path.join(OUTPUT_DIR, 'android_issuetracker_html.jl')
data = FileUtil.load_data_list(file)
count = 0
for data_ in data:
    if count > 100:
        break
    title = data_['title']
    if title != "":
        count = count + 1
        print("-", title[1:])


print(len(data))

# file = os.path.join(OUTPUT_DIR, 'issuetracker.json')
# data = FileUtil.load_data_list(file)
# print(len(data))