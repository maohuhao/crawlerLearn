import requests
import random

if __name__ == '__main__':
    url = 'http://a.cqie.edu.cn/cas/login?service=http://i.cqie.edu.cn/portal_main/toPortalPage'
    session = requests.session()
    session.headers.update({
        'uesr-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    })
    session.get(url=url)
    JSESSIONID = session.cookies.get('JSESSIONID')

    url2 = f"http://a.cqie.edu.cn/cas/login;jsessionid={session.cookies.get('JSESSIONID')}?service=http%3A%2F%2Fi.cqie.edu.cn%2Fportal_main%2FtoPortalPage"

    data = {
        "username": "209030111",
        "password": "zJ4USwj8itfIg95h2lSQjg==",
        "authCode": "",
        "lt": "abcd1234",
        "execution": "e1s1",
        "_eventId": "submit",
        "isQrSubmit": "false",
        "qrValue": "",
        "isMobileLogin": "false"
    }

    session.post(url2, data=data)

    # 设置cookie为空
    session.cookies.set('JSESSIONID', None)
    #
    # 更新cookie
    c = requests.cookies.RequestsCookieJar()
    c.set('JSESSIONID', JSESSIONID)
    session.cookies.update(c)
    print(session.cookies.get_dict())

    # 获取活动列表JSESSIONID
    url3 = 'http://a.cqie.edu.cn/cas/login?service=http%3a%2f%2fxs.cqie.edu.cn%2fxg%2fssoLogin.jsp%3frdPath%3dbackstageNoNav.jsp%3floadMainPage%3dspring%3aallhdzyz%2fFromQXHDMHViewMH'
    resp1 = session.get(url3, allow_redirects=False)
    resp2 = requests.get(url=resp1.headers.get('Location'), headers={'uesr-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}, allow_redirects=False)
    # 更新cookie
    session.cookies.set('JSESSIONID', resp2.cookies.get('JSESSIONID'))

    # 将JSESSIONID保存在服务器
    url4 = 'http://xs.cqie.edu.cn/xg/acp/system/login?_rd=100&rdPath=backstageNoNav.jsp?loadMainPage=spring:allhdzyz/FromQXHDMHViewMH'
    session.post(url4)

    # 获取活动
    res = session.get(f'http://xs.cqie.edu.cn/xg/allhdzyz/FromQXHDMHViewMH?random={random.random()}&random={random.random()}')
    print(res.text)
