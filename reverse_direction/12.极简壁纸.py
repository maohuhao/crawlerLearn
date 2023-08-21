import requests
import execjs
from fake_useragent import UserAgent

from py_mini_racer import MiniRacer

user_agent = UserAgent()

headers = {
    'User-Agent': user_agent.random
}


class MiniWallpaper():
    payload = {
        "size": 24,
        "sort": 0,
        "category": 0,
        "resolution": 0,
        "color": 0,
        "categoryId": 0,
        "ratio": 0
    }

    def __init__(self, url: str) -> None:
        self.ctx = None
        self.result = None
        self.url = url

    # 初始化解密模块
    def init_decrypt(self) -> None:
        with open('12.极简壁纸.js', 'r') as f:
            js = f.read()
        self.ctx = execjs.compile(js)

    # 获取加密数据
    def get_data(self, page: int) -> str:
        # requests.post(url=self.url, headers=headers, data=data) 请求返回的结果：{"msg":"未知异常，请联系管理员","result":{},"code":500}
        self.payload.update({'current': page})
        response = requests.post(
            url=self.url, headers=headers, json=self.payload)

        print(response.text)
        self.result = response.json()['result']

    def run(self):
        self.init_decrypt()
        self.get_data(1)

        print(self.ctx.call('decrypt', self.result))


if __name__ == '__main__':

    url = 'https://api.zzzmh.cn/bz/v3/getData'
    crawler_wallpaper = MiniWallpaper(url)
    crawler_wallpaper.run()
