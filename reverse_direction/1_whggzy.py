import requests

"""
接口校验 路径 -> XHR断点
"""

if __name__ == '__main__':
    url = 'http://www.whggzy.com/front/search/category'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'Referer': 'http://www.whggzy.com/PoliciesAndRegulations/index.html?utm=sites_group_front.2ef5001f.0.0.682e3b30c08f11ed9c0e8f2546c4b7b8',
        'Accept': "*/*",
        'Content-Type': "application/json",
        'X-Requested-With': "XMLHttpRequest"
    }

    data = '''{"utm": "sites_group_front.2ef5001f.0.0.682e3b30c08f11ed9c0e8f2546c4b7b8",
         "categoryCode": "GovernmentProcurement", "pageSize": 15, "pageNo": 1}'''

    response = requests.post(url=url, headers=headers, data=data).text

    print(response)
