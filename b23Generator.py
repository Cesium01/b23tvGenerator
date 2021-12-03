import random
import requests
import json
import string

api = 'http://api.bilibili.com/x/share/click'

def random_buvid():
    return ''.join(random.choices(string.digits+string.ascii_letters, k=32))+'infoc'

def get_b23of(long_url):
    data = {
        'build': '6500300',
        'buvid': random_buvid(),
        'oid': long_url,
        'platform': 'android',
        'share_channel': 'COPY',
        'share_id': 'public.webview.0.0.pv',
        'share_mode': '3'
    }
    res = requests.post(api, data=data, timeout=9)
    data = json.loads(res.content)
    if data['data'].__contains__('content'):
        return data['data']['content']
    else:
        print(json.dumps(data))
        return

print(get_b23of('https://space.bilibili.com/36700106/video'))
print(get_b23of('https://www.bilibili.com/video/BV1e44y147nb'))
print(get_b23of('https://t.bilibili.com/599449444500820929'))
print(get_b23of('https://i0.hdslb.com/bfs/album/bd13c332b21a61628132118d6e39c2f94ed80270.gif'))
