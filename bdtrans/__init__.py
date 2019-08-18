import os

from bdtrans.baidu  import trans
from bdtrans.baidu  import set_lang
from bdtrans.baidu  import reverse_lang
from bdtrans.baidu  import display_rules
from bdtrans.common import list_langs
from bdtrans.common import get_profile_path
from bdtrans.deploy import initialize_app
from bdtrans.deploy import change_info
from bdtrans.deploy import change_lang


__version__ = 'v1.0'
__all__= ['trans','set_lang','reverse_lang','display_rules',
          'list_lags()','get_profile_path','initialize_app',
          'change_info','change_lang']
