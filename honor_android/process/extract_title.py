# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-----------------------------------------
@Author: zz
@Email: 21212010059@m.fudan.edu.cn
@Created: 2022/05/16
------------------------------------------
@Modify: 2022/05/16
------------------------------------------
@Description:
"""
import os
from lxml import etree
from honor_android.util.file_util import FileUtil
from definitions import OUTPUT_DIR
file = os.path.join(OUTPUT_DIR, 'android_developerandroid_html.jl')
data = FileUtil.load_data_list(file)
count = 0
print(len(data))
one_count = 0
zero_count = 0
mui_count = 0

error_count = 0

for data_ in data:
    html = data_.get('html')
    count = count + 1
    try:
        html = etree.HTML(html)

        title = html.xpath('//h1/text()')
        if len(title) == 1:
            data_['title'] = title[0]
            one_count = one_count + 1
            print("process", one_count, data_.get('url'))
        if len(title) >1:
            mui_count = mui_count + 1
            now_title = title[0]
            for title_ in title:
                if len(title_) > len(now_title):
                    now_title = title_
            data_['title'] = title[0]
            one_count = one_count + 1
            print("meet_multi", mui_count, data_.get('url'))
        if len(title) == 0:
            zero_count = zero_count + 1
            print("meet_zero", zero_count, data_.get('url'))
    except BaseException as e:
        error_count = error_count + 1
        print('meet error', error_count, data_.get('url'))


print("process ok")
print("zero", zero_count)
print("one", one_count)
print("mulit", mui_count)
print("error", error_count)


FileUtil.write2jl(data, 'android_developerandroid_add_title_html.jl')

