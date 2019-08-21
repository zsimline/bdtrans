""" The languages code are defined here.
"""

import os
import gettext

def i18n():
    app_name = 'translate'
    local_dir = os.path.abspath("locale")
    gettext.bindtextdomain(app_name, local_dir)
    gettext.textdomain(app_name)
    return gettext.gettext

_ = i18n()


class Code(object):
    zh = 'zh'
    en = 'en'
    de = 'de'
    it = 'it'
    cs = 'cs'
    jp = 'jp'
    th = 'th'
    ry = 'ru'
    pt = 'pt'
    el = 'el'
    nl = 'nl'
    pl = 'pl'
    hu = 'hu'
    yue = 'yue'
    wyw = 'wyw'
    kor = 'kor'
    fra = 'fra'
    spa = 'spa'
    ara = 'ara'
    bul = 'bul'
    est = 'est'
    dan = 'dan'
    fin = 'fin'
    rom = 'rom'
    slo = 'slo'
    swe = 'swe'
    cht = 'cht'
    vie = 'vie'


class SourceCode(Code):
    """ 
    Defines the source language code.
    """
    auto = 'auto'


class TargetCode(Code):
    """ 
    Defines the target language code.
    Notice that: Target language code cannot be auto.
    """
    pass


LANGUAGES = {
    'zh':  _('中文'),
    'en':  _('英语'),
    'yue': _('粤语'),
    'wyw': _('文言文'),
    'jp':  _('日语'),
    'kor': _('韩语'),
    'fra': _('法语'),
    'spa': _('西班牙语'),
    'th':  _('泰语'),
    'ara': _('阿拉伯语'),
    'ru':  _('俄语'),
    'pt':  _('葡萄牙语'),
    'de':  _('德语'),
    'it':  _('意大利语'),
    'el':  _('希腊语'),
    'nl':  _('荷兰语'),
    'pl':  _('波兰语'),
    'bul': _('保加利亚语'),
    'est': _('爱沙尼亚语'),
    'dan': _('丹麦语'),
    'fin': _('芬兰语'),
    'cs':  _('捷克语'),
    'rom': _('罗马尼亚语'),
    'slo': _('斯洛文尼亚语'),
    'swe': _('瑞典语'),
    'hu':  _('匈牙利语'),
    'cht': _('繁体中文'),
    'vie': _('越南语'),
    'auto':_('自动检测')
}


DEFAULT_SOURCE_LANG = 'en'
DEFAULT_TARGET_LANG = 'zh'
