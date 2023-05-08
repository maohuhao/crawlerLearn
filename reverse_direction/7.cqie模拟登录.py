import hashlib
import random
import re
import time
import json
import getpass

import requests
from fake_useragent import UserAgent

from DESEncypt import get_encrypt_pwd
from configTool import *

ua = UserAgent()

class CqieLogin():

    data = {
        'authCode': '',
        'lt': 'abcd1234',
        'execution': 'e1s1',
        '_eventId': 'submit',
        'isQrSubmit': "false",
        'qrValue': '',
        'isMobileLogin': 'false'
    }

    def __init__(self):
        self.JSESSIONID = ''
        self.active_list = ''
        self.session = requests.session()
    
    def print_add_user(self):
        # 添加账号
        user_total = user_info_total('config.ini')
        user_num = 'User' + str(user_total+1)
        num = None
        if user_total != 0:
            print_user_info('config.ini')
            num = int(input('选择要登陆的账号(序号)\(输入0添加新账号)：'))
        
        if user_total != 0 and num != 0:
            user_info = select_user_info('config.ini', 'User' + str(num))
            self.data['username'] = user_info['user'] 
            self.data['password'] = user_info['pwd']
        else: 
            self.data['username'] = input('Student Number: ')
            self.data['password'] = get_encrypt_pwd(getpass.getpass())
            add_user_info('config.ini', user_num, username=self.data['username'], password=self.data['password'])

    def login(self):
        # 登录
        url = 'http://a.cqie.edu.cn/cas/login?service=http://i.cqie.edu.cn/portal_main/toPortalPage'
        self.session.headers.update({
            'uesr-agent': ua.random 
        })
        self.session.get(url=url)
        self.JSESSIONID = self.session.cookies.get('JSESSIONID')

        url2 = f"http://a.cqie.edu.cn/cas/login;jsessionid={self.session.cookies.get('JSESSIONID')}?service=http%3A%2F%2Fi.cqie.edu.cn%2Fportal_main%2FtoPortalPage"
        self.session.post(url2, data=self.data)
    
    def set_active_session(self):
        # 设置cookie为空
        self.session.cookies.set('JSESSIONID', None)
        #
        # 更新cookie
        c = requests.cookies.RequestsCookieJar()
        c.set('JSESSIONID', self.JSESSIONID)
        self.session.cookies.update(c)

        # 获取活动列表JSESSIONID
        url3 = 'http://a.cqie.edu.cn/cas/login?service=http%3a%2f%2fxs.cqie.edu.cn%2fxg%2fssoLogin.jsp%3frdPath%3dbackstageNoNav.jsp%3floadMainPage%3dspring%3aallhdzyz%2fFromQXHDMHViewMH'
        resp1 = self.session.get(url3, allow_redirects=False)
        resp2 = requests.get(url=resp1.headers.get('Location'), headers={'uesr-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}, allow_redirects=False)
        # 更新cookie
        self.session.cookies.set('JSESSIONID', resp2.cookies.get('JSESSIONID'))

        # 将JSESSIONID保存在服务器
        url4 = 'http://xs.cqie.edu.cn/xg/acp/system/login?_rd=100&rdPath=backstageNoNav.jsp?loadMainPage=spring:allhdzyz/FromQXHDMHViewMH'
        self.session.post(url4)

    def get_active_list(self):
        # 获取活动
        get_active = 'http://xs.cqie.edu.cn/xg/allhdzyz/getHDbyPage'
        params = {
            "random": str(random.random()),
            "type": "1",
            "hdlb": "",
            "hdxn": "",
            "hdxq": ""
            }
        
        self.session.headers.update({'Referer': 'http://xs.cqie.edu.cn/xg/backstageNoNav.jsp?loadMainPage=spring:allhdzyz/FromQXHDMHView'})
        self.session.headers.update({
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9"})
        res = self.session.get(get_active, params=params)
        self.active_json = res.json()

    
    def get_page_list(self):
        # 获取第一页活动
        self.active_list = self.active_json.get('data')

        if not self.active_list:
            print("没有活动")
            exit()

        # 获取总页数
        max_page = self.active_json.get('maxPage')
        
        # 获取详细信息
        self.session.headers.update({
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest'
        })

        index = 1
        print('序号 活动名称\t 活动开始时间\t 活动结束时间\t' 
              f'活动属性\t 活动地点')
        for item in self.active_list:
            url = f'http://xs.cqie.edu.cn/xg/allhdzyz/FromHDSQView?random={random.random()}&random={random.random()}'
            post_data = {
                "dataId": item.get('ID')
            }
            detail_resp = self.session.post(url=url, data=post_data)

            detail_data = json.loads(re.search('var data = (.*);', detail_resp.text).group(1))

            self.print_active(index, item, detail_data)

            index += 1

    def print_active(self, index:int, data: dict, detail_data: dict)-> None:
        print(f'{index}\t {data.get("HDMC")}\t {data.get("HDKSSJ")}\t {data.get("HDJSSJ")}\t' 
            f'{detail_data.get("HDSX")}\t {detail_data.get("HDDD")}')
    

    def run(self):
        self.print_add_user()
        self.login()
        self.set_active_session()
        self.get_active_list()
        self.get_page_list()
        # 申请活动
        while True:
            apply_num = input('请输入要申请的序号(退出q)：')
            if apply_num == 'q':
                break

            apply_url = 'http://xs.cqie.edu.cn/xg/szjyhdzyz/insertSQ'
            apply_data = {
                    'hdid':self.active_list[int(apply_num)-1].get('ID')
                }

            apply_resp = self.session.post(url = apply_url, data = apply_data)
            apply_json = apply_resp.json()
            if apply_json.get('flag'):
                print('申请成功')
            else:
                print('参与人数上限')


if __name__ == '__main__':
    cqie = CqieLogin()
    cqie.run()

