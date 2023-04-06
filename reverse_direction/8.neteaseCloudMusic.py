import requests
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62',
    'Content-Type': "application/x-www-form-urlencoded",
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
        "csrf_token": ""
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
        url = 'https://music.163.com/weapi/cloudsearch/get/web?csrf_token='
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
        self.original_data['ids'] = f"[{ids}]"
        encrypt_data = os.popen(
            f'node 8.download.js "{self.original_data["ids"]}" "{self.original_data["level"]}" "{self.original_data["encodeType"]}" "{self.original_data["csrf_token"]}"').readlines()
        self.data['params'] = encrypt_data[0].strip()
        self.data['encSecKey'] = encrypt_data[1].strip()
        url = 'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token='
        print(self.data)
        resp_json = requests.post(url=url, headers=headers, data=self.data).json()
        download_link = resp_json.get('data')[0].get('url')
        return download_link

    def download_song(self, link, name):
        print(link)
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62',
            }
            suffix = link.rsplit('.')[-1]
            song = requests.get(url=link, headers=headers).content
            with open(f'./{name}.{suffix}', 'wb') as f:
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
        print(ids)
        name = song.get('name')
        print(name)
        song_link = self.get_songs_link(ids)
        self.download_song(song_link, name)

if __name__ == '__main__':
    song = input("请输入要下载的歌曲：")
    neteaseCloudMusic = NeteaseCloudMusic(song)
    neteaseCloudMusic.run()