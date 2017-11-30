# coding=utf-8

import re


def translate(string):
    # 比如匹配时间
    if not string:
        return None
    string = string.encode('utf-8')
    string = str(string).replace('：', ':')
    pattern = re.compile(r'\d{4}\s*-\s*\d{1,2}\s*-\s*\d{1,2}\s*\d{1,2}:\d{1,2}\s*\d{1,2}:\d{1,2}')
    pattern_second = re.compile(r'\d{4}\s*-\s*\d{1,2}\s*-\s*\d{1,2}\s*\d{1,2}:\d{1,2}\s*-\s*\d{1,2}:\d{1,2}')
    match = pattern.search(string)
    match_second = pattern_second.search(string)
    if match:
        return string
    if match_second:
        # 正则表达式匹配之后去掉时间中间的横线
        string = re.sub(r'\d{1,2}:\d{1,2}\s*-\s*\d{1,2}:\d{1,2}', replacement, string)
        return string
    else:
        return None


def replacement(m):
    p_str = m.group()
    p_str = str(p_str).replace('-', ' ')
    return p_str
