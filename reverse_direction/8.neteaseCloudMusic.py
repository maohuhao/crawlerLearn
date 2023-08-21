import os
from pathlib import Path

import requests
from fake_useragent import UserAgent

ua = UserAgent()

user_agent = ua.random

headers = {
    'User-Agent': user_agent, 
    'Content-Type': "application/x-www-form-urlencoded",
    'cookie': 'MUSIC_R_T=1612075548887; MUSIC_A_T=1612075548879; _ntes_nnid=af914f4fa5fbded30cc576a48fbc9660,1682996191000; _ntes_nuid=af914f4fa5fbded30cc576a48fbc9660; NMTID=00OGxnIEBjEGuQ8mk10jJRRsBag6_YAAAGH2mPfwQ; WEVNSM=1.0.0; WNMCID=jaqgtr.1682996191339.01.0; JSESSIONID-WYYY=zANxuCWR7TaT9M9ypdnwpj%2BJudYwrAm9GqoCz%2F4f%2F8A3BMdUBkUCbqTGtbnEQ3rfqaH0oMqRPuJ4AyYj%2FpGQzUxzaplWn9YBJfjPK%2Fz%2BWgei0NFkfo8vbgE6wNi2IVn8CAVFoafRlIEAPbd%2BMnXua%5CO%2Brqbm5CoOsROFK78oBdvMKZBR%3A1682997991427; _iuqxldmzr_=33; WM_NI=qSF%2FW%2B%2F2aLRQGuUybPxp6Z%2FpdE6zGLFGO45VG%2Fxzz3KnHQ%2FL2fMv90lb%2FuHwpqoBYJTxSI%2BgHk0YHRGG3oN9LfGhciov4%2Fsaeayj%2BE9BxHNECoCjVDVBQ6xl9fyA87HGa2U%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeacd26b918aa3bacb3f9cef8ab6d54b969f8ab1c15cb791ad82c83ef79c8699db2af0fea7c3b92ab38d8ad0d621edeeafadd15b85ab9b9ae15cbcb0fabbae7ca89bfa9bc648869981d5b85e85f1b89bf93989b288b2ae48f2ba8397bc3cb0bee196cb7db4afa1a3dc4298a89daaaa6d8cb500bacb5a8599fd90cd3390ba8989e263adaafcd0f26ba7bfb78baa4ffb9eb8a9cd4f81b18d8bd550969e9fd7fb68fbbab7a2bb3d8c99afd3d837e2a3; WM_TID=PSLg5DmB7k1AREUFEQbFOqeILAu9Hd1X; __snaker__id=QamC84H4YXL0cd9l; gdxidpyhxdE=2mCnjBMEQzVdAidGTQcuZE8zV7KjDBioz7vK4CYVqghjMoyL3DAlSJ6%2BPA8vdbv0zAwIl4azm5oHLjihWdmkW%5CUBoHL5cqLcZGpI3clJQRwVc5zBSry690vPO72LggftpCImf39sa5YWJ97dBYUwb8vh43Et4mk6ILkaupUAELVYHVaY%3A1682997101072; YD00000558929251%3AWM_NI=wh11g%2Fsh3myWNWYlMGNqJaSBV0CSOlhHrZARp%2BCJ8rR0fATyE2ZphY5feiaWzR8Pm%2BZfS2br4mAw4%2BH2g%2BldTTEozKigowr5H4qHoCbSEjTBM8v8YhaUOSO2EN2KfAFpcko%3D; YD00000558929251%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eea3e570b3908493f259fcb08fb6c85e838f8ab0c16ee9bb8786c65b96be84ccce2af0fea7c3b92ab5b8ffd2e625b1b8fd8efc5d8e89978dd04d8eaf8682d24a96f08db4ce68ac98bebbc45ab4f58dabbb7a92f0aaa2d77387ee9691eb53f7baab8ae45dba8ef8b1f0219aba9dd3e17af8b38f98b7218ceea9ccef70988c8b90f941abb9a198f13f8cecbfa9ee49a28d8b8bd74a8fe8bad9dc64a38b81b4ce3a8792feace54b86b0ad8cee37e2a3; YD00000558929251%3AWM_TID=ezZMQXbRULFBQBBARQbEf7bNeDEQOLrL; MUSIC_U=b8114db0db3c254785f3af6499969ee8c3f34e89b2f143b7cea7a4406f0fb6e51e8907c67206e1ed89c59d0757496b65df1e5924ea40105762a72e38b0a14d7c37638c1837f67a2dd4dbf082a8813684; __csrf=9fe258d9a413469f81f0c65a775a3133; ntes_kaola_ad=1'
}


class NeteaseCloudMusic():
    original_data = {
        "hlpretag": '<span class=\"s-fc7\">',
        "hlposttag": "</span>",
        "type": "1",
        "offset": "0",
        "total": "true",
        "limit": "30",
        "level": "standard",
        "encodeType": "aac",
        "csrf_token": '9fe258d9a413469f81f0c65a775a3133'
    }
    data = dict()
    songs_list = []

    def __init__(self, song):
        self.original_data['s'] = song

    def get_encrypt_data(self):
        encrypt_data = os.popen(
            f'node 8.neteaseCloudMusic.js "{self.original_data["hlpretag"]}" "{self.original_data["hlposttag"]}" "{self.original_data["s"]}" "{self.original_data["type"]}" "{self.original_data["offset"]}" "{self.original_data["total"]}" "{self.original_data["limit"]}" "{self.original_data["csrf_token"]}"').readlines()
        self.data['params'] = encrypt_data[0].strip()
        self.data['encSecKey'] = encrypt_data[1].strip()

    def get_songs_list(self):
        url = f'https://music.163.com/weapi/cloudsearch/get/web?csrf_token={self.original_data["csrf_token"]}'
        self.get_encrypt_data()
        resp_json = requests.post(url=url, headers=headers, data=self.data).json()
        return resp_json

    def print_songs_list(self):
        resp_json = self.get_songs_list()
        songs_dict = resp_json.get('result', '暂无歌曲')
        if songs_dict == '暂无歌曲':
            print("没有搜索到对应的歌曲")
            return
        self.songs_list = songs_dict.get('songs')
        if not self.songs_list:
            print("没有歌曲")
            return
        i = 1
        for song in self.songs_list:
            print(f'{i}\t歌名：{song.get("name")}\t歌手：{song.get("ar")[0].get("name")}')
            i += 1

    def get_songs_link(self, ids):
        try:
            self.original_data['ids'] = f"[{ids}]"
            encrypt_data = os.popen(
                f'node 8.download.js "{self.original_data["ids"]}" "{self.original_data["level"]}" "{self.original_data["encodeType"]}" "{self.original_data["csrf_token"]}"').readlines()
            self.data['params'] = encrypt_data[0].strip()
            self.data['encSecKey'] = encrypt_data[1].strip()
            url = f'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token={self.original_data["csrf_token"]}'
            
            resp_json = requests.post(url=url, headers=headers, data=self.data).json()
            download_link = resp_json.get('data')[0].get('url')
        except Exception as e:
            return "无法获取"

        return download_link

    def download_song(self, link, name):
        print(link)
        try:
            headers = {
                'User-Agent': user_agent
            }
            suffix = link.rsplit('.')[-1]
            suffix = suffix.split('?')[0]
            song = requests.get(url=link, headers=headers).content
            music_file = Path(f'/home/dwmMhh/Music/{name}.{suffix}')            
            music_file.touch(exist_ok=False)
            print(music_file.resolve())
            with open(music_file.resolve(), 'wb') as f:
                f.write(song)
                print('下载成功')
        except Exception as e:
            print(e)

    def run(self):
        self.print_songs_list()
        num = int(input("请输入要下载歌曲的序号："))
        if num < 1:
            print("序号不能小于1")
            return
        song = self.songs_list[num - 1]
        ids = song.get('id')
        name = song.get('name')
        song_link = self.get_songs_link(ids)
        if not song_link:
            print("下载失败")
            return 1

        self.download_song(song_link, name)

if __name__ == '__main__':
    while True:
        song = input("请输入要下载的歌曲：")
        neteaseCloudMusic = NeteaseCloudMusic(song)
        neteaseCloudMusic.run()
        flag = input("是否继续下载音乐：（y/n）")
        if flag == 'n' or flag == 'N':
            break
