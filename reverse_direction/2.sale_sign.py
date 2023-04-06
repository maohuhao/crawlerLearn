import requests
import time
import execjs
import math

if __name__ == '__main__':
    with open('2.sale_sign.js', 'r') as f:
        js = f.read()
    ctx = execjs.compile(js)

    token = '57e52806dd28c2a825ff770cefe4d8d1'
    g = '12574478'
    timestamp = math.floor(time.time() * 1000)
    print(timestamp)
    data = '{"cid":"FactoryRankServiceWidget:FactoryRankServiceWidget","methodName":"execute","params":"{\\"extParam\\":{\\"methodName\\":\\"readRelatedRankEntries\\",\\"cateId\\":\\"10166\\",\\"size\\":\\"15\\"}}"}'
    sign = ctx.call('h', token + "&" + str(timestamp) + "&" + g + "&" + data)
    print(sign)