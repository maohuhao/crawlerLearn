import json

import requests
import execjs
import time
import hashlib

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62'
}

with open('9.五矿.js', 'r', encoding='utf-8') as f:
    js = f.read()
ctx = execjs.compile(js)


class Wukuang():
    sign = ''
    public_key = ''
    sign_data = ''

    def __init__(self, page):
        self.page = page

    def get_sign(self):
        md5 = hashlib.md5()
        md5.update(self.sign_data.encode('utf-8'))
        self.sign = md5.hexdigest()
        print(self.sign)

    def get_public_key(self):
        url = 'https://ec.minmetals.com.cn/open/homepage/public'
        self.public_key = requests.post(url=url, headers=headers).text
        print(self.public_key)

    def get_data(self, page):
        url = 'https://ec.minmetals.com.cn/open/homepage/zbs/by-lx-page'

        explicit_data = '{"inviteMethod":"","businessClassfication":"","mc":"","lx":"ZBGG","dwmc":"","pageIndex":%s,"sign":"%s","timeStamp":%s}' % (
        page,
        self.sign, str(
            int(time.time() * 1000)))

        print(explicit_data)
        param = ctx.call('getRsa', self.public_key, explicit_data)
        print(param)
        data = {
            'param':param
        }

        resp_json = requests.post(url=url, headers=headers, json=data).json()
        print(resp_json)

    def run(self):
        for i in range(1, self.page + 1):
            self.sign_data = '{"inviteMethod":"","businessClassfication":"","mc":"","lx":"ZBGG","dwmc":"","pageIndex":%s}' % str(
                i)
            self.get_sign()
            self.get_public_key()
            self.get_data(i)
            time.sleep(1)


if __name__ == '__main__':
    obj = Wukuang(5)
    obj.run()
