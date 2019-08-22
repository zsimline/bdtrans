import os 
import gettext
import getpass
import platform


def i18n():
    app_name = 'translate'
    local_dir = os.path.abspath("locale")
    gettext.bindtextdomain(app_name, local_dir)
    gettext.textdomain(app_name)
    return gettext.gettext


def check_platform():
    """
    Return the Operating System used by the user.
    """
    platform_ = platform.system() 
    if platform_ == 'Linux':
        return 'linux'
    if platform_ == 'Darwin':
        return 'macosx'
    if platform_ == 'Windows':
        return 'windows'
    return 'unkownOS'


def get_profile_path():
    """
    Get the program configuration file path
    """
    profile_path = {
        'linux': '/home/%s/.bdtrans',
        'macosx': '/Users/%s/.bdtrans',
        'windows': 'C:/Users/%s/AppData/Local/.bdtrans',
        'unknowOS': './.bdtrans'
    }
    platform = check_platform()
    username = getpass.getuser()
    return profile_path[platform] % username


_ = i18n()

# Global Profile
PROFILE = get_profile_path()

# API of Baidu Translation
API = ('https://api.fanyi.baidu.com/api/trans/vip/translate?'
       'appid=%s&q=%s&from=%s&to=%s&salt=%s&sign=%s')
