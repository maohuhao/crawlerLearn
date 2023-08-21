import re
import requests

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}

def get_video_set(num: int) -> str:
    url = 'https://a2.m1907.top:404/api/v/'
    params = {
        "z": "02268e51de6c56b0da64d31ca1928446",
        "jx": "https://www.iqiyi.com/v_xkt6z3z798.html?r_area=pcw_rec_like",
        "s1ig": "11399",
        "g":''
        }
    
    response = requests.get(url=url, headers=headers, params=params)

    json_set = response.json()

    video_url = json_set.get('data')[0].get('source').get('eps')[num-1].get('url')
    video_name = json_set.get('data')[0].get('source').get('eps')[num-1].get('name')
    return video_url


def get_m3u8_url(url: str)->str:
    prefix = re.match('(https://.*?)/', url).group(1)
    headers.update({
        'referer': 'https://z2.m1907.top:404/'
        })
    first_url = requests.get(url=url, headers=headers)
    suffix = first_url.text.split('\n')[-2]

    return prefix + suffix


if __name__ == '__main__':
    video_url = get_video_set(1)
    source_url = get_m3u8_url(video_url)
    print(source_url)
