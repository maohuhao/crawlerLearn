import requests

if __name__ == '__main__':
    url = 'http://a.cqie.edu.cn/cas/login?service=http%3A%2F%2Fi.cqie.edu.cn%2Fportal_main%2FtoPortalPage'
    session = requests.session()
    session.headers.update({
        'uesr-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    })
    session.get(url=url)

    url2 = 'http://a.cqie.edu.cn/cas/login;jsessionid=' + session.cookies.get('JSESSIONID')

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

    resp = session.post(url2, data=data)
    # print(session.cookies.get_dict())

    # session.get(url='http://xs.cqie.edu.cn/xg/NoticeNewsList/viewListPage?type=1')
    resp2 = session.get(url='http://xs.cqie.edu.cn/xg/ssoLogin.jsp?rdPath=backstageNoNav.jsp?loadMainPage=spring:allhdzyz/FromQXHDMHViewMH&ticket=ST-534824-OtaoJ6xlgYh4FXebP1TC-http%3A%2F%2Fa.cqie.edu.cn%2Fcas')
    print(session.cookies.get_dict())
    print(resp2.text)

    # session.headers.update({'X-Requested-With': 'XMLHttpRequest'})
    # session.headers.update({'Referer': 'http://xs.cqie.edu.cn/xg/backstageNoNav.jsp?loadMainPage=spring:allhdzyz/FromQXHDMHView'})

    # url4 = 'http://xs.cqie.edu.cn/xg/allhdzyz/FromQXHDMHView?random=0.7484653543381663&random=0.10908594765094759'
    # url4 = 'http://xs.cqie.edu.cn/xg/acp/system/login?_rd=100&rdPath=backstageNoNav.jsp?loadMainPage=spring:allhdzyz/FromQXHDMHViewMH'
    # resp3 = session.post(url4)
    # print(resp3.text)

