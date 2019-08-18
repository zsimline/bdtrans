API = 'https://api.fanyi.baidu.com/api/trans/vip/translate?appid=%s&q=%s&from=%s&to=%s&salt=%s&sign=%s'

PROFILE_PATH = {
    'linux': '/home/%s/.bdtrans',
    'macosx': '/Users/%s/.bdtrans',
    'windows': 'C:/Users/%s/AppData/Local/.bdtrans',
    'unknowOS': './.bdtrans'
}
