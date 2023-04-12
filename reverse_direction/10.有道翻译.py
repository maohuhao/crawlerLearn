import json

import requests
import time
import hashlib

# 解决execjs执行js代码报编码错误
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import execjs
from fake_useragent import UserAgent

if __name__ == '__main__':
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': 'https://fanyi.youdao.com/',
        'Host': 'dict.youdao.com',
        'Origin': 'https://fanyi.youdao.com',
        'Cookie': 'OUTFOX_SEARCH_USER_ID=-867100222@10.112.57.88; OUTFOX_SEARCH_USER_ID_NCOO=894553334.5490068'
    }

    with open('10.有道翻译.js', 'r', encoding='utf-8') as f:
        js = f.read()
    ctx = execjs.compile(js)

    url = 'https://dict.youdao.com/webtranslate'
    timestamp = str(int(time.time() * 1000))
    md5 = hashlib.md5()
    md5.update(f'client=fanyideskweb&mysticTime={timestamp}&product=webfanyi&key=fsdsogkndfokasodnaso'.encode('utf-8'))
    sign = md5.hexdigest()

    data = {
        'i': 'china',
        'from': 'auto',
        'to': '',
        'domain': '0',
        'dictResult': 'true',
        'keyid': 'webfanyi',
        'sign': sign,
        'client': 'fanyideskweb',
        'product': 'webfanyi',
        'appVersion': '1.0.0',
        'vendor': 'web',
        'pointParam': 'client,mysticTime,product',
        'mysticTime': timestamp,
        'keyfrom': 'fanyi.web'
    }

    resp = requests.post(url=url, data=data, headers=headers)
    translate = ctx.call('getText', resp.text)


    json = json.loads(translate)
    print(f"翻译结果为：{json.get('translateResult')[0][0].get('tgt')}")

    resp.close()