# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-----------------------------------------
@Author: zz
@Email: 21212010059@m.fudan.edu.cn
@Created: 2022/05/13
------------------------------------------
@Modify: 2022/05/13
------------------------------------------
@Description:
"""
import os
from lxml import etree
from honor_android.util.file_util import FileUtil
from definitions import OUTPUT_DIR
file = os.path.join(OUTPUT_DIR, 'android_jianshu_html.jl')
data = FileUtil.load_data_list(file)
count = 0

for data_ in data:
    html = data_.get('html')
    count = count + 1
    print('process', count, data_.get('url'))
    html = etree.HTML(html)
    article = html.xpath('/html/body/div/div[1]/div/div/section[1]/article')[0]
    data_['html'] = etree.tostring(article, encoding='utf-8').decode('utf-8')

FileUtil.write2jl(data, 'android_jianshu_only_article_html.jl')

