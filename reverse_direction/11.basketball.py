
import requests
from Crypto.Cipher import AES
import base64
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import execjs


def ase_decrypt(key:str, data: bytes) -> str:
    ase = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    return ase.decrypt(data).decode()


if __name__ == '__main__':
    key = 'uVayqL4ONKjFbVzQ'
    data = 'OtyNnseqYEeuEMxhHuTq7vdlRxWR8In2hDp4/z/G3osvshkfY+P9yNrbDAb4B496adyqHR7kHzd4bD2C9/dMOXVPOubUY4Ntj+ydB7yLCPuRCLQHHBDgqgTL3NxZQ2V5PmD94P3TaRtfnbGTVSSL8LGmWiXgpntrDjeHbmZfAbi9eBoQ0I4NTOjRtH+gd/ly9XoAJc6ocykL+ct5cEKVwZF/JsxJcAiWJDCICzjswU5WDbUZOmxhRNVBl2p2yE69cANvsbOSTYP6eSTvZ+5Nn4NaQCgnhb/y23pwMkl9ksEmw/Uy0wVrB2F/WCiguM6DEDnQ8VuQSnIAP5IkGylZy/dlJIsMVpjuEyu6qDEfuB0q0MxVVoAlSmUESnBF+DQQmIjXsM7m8PTMjCrDI70RdpZG0582x9j2DYK+UlPtZ4eBKInmAvrOx+LEA/QqQOj3vnvR0ZCbQE/7mzIgMJfPKmF6q02bqVB+vcv36nR9oZ+roKVIgUCKw8YAj5GEgWg9tqUVtsRAK+DclGc2INBCYgo8c+iDP6cb0MU7CC+iPOOBDVcoTm86jjejd5RMJnfou+CQI/WWI/COKcnSRC8j4Qs7ZX5P1VxOueeQeP8nSbbxUOOjFFq5xK/6TFUtYs9HKsTgbdfIEWKTgb9THA9umuO4EPd8oAsYFhtwqChN3gfCDOCTK0m+7qgbufxRhjuyk208exVXo8qB9gN+aPVcX3Fk/ruT8GP5kHal9t/Icu5Nb+PK+SGMzA2ZYuZDc9fhnLEEcmY8G7WrRNC4/GPgckcrvImI5hSXiW9bxEnL4fPuWdyEU0PfIv6lfjHJETYmSAt8/rbY+o390j6mCHB2X4Amk9KDs6XKSGpAicLgupGaGiv1AW+FF/SaqLDcGdXm2ry9kBQ1UAqlZVObIOSBO7ZNctFL50K33O7TNix/DHQrUl9PQ8ovrmEi5AUOM3N5WTpqPU8hp5KHc5V+X3T4UGBVjfOknytZkQBETQcmo7IYyKeFtLcH6YXRDZ/09c4qxgsa97J/NUPt0gCF30crOHxX5Rrf7RHVTQBMbxCW9nXFnEj6MmKaBIwyN0wjNUUmNuDpnRfF1RDwUaSQrsjqbdx/Gk7u4SR4utF695eqAEfFz3/ydVg+BqsdR/z3ba1w'

    url = 'https://data-server.cbaleague.com/api/teams/teamList'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.34'
    }

    resp = requests.get(url=url, headers=headers)
    # print(resp.text)

    with open('11.basketball.js', 'r', encoding='utf-8') as f:
        js = f.read()
    ctx = execjs.compile(js)

    result = eval("ctx.call('getDecrypt', eval(resp.text))")
    print(result)