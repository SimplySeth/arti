from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import urllib2
import re
from datetime import datetime
import pytz
from bs4 import BeautifulSoup as soup

from ansible.errors import AnsibleError
from ansible.plugins.lookup import LookupBase
from ansible.module_utils.urls import open_url, ConnectionError, SSLValidationError
from ansible.utils.unicode import to_unicode

try:
    from __main__ import display
except ImportError:
    from ansible.utils.display import Display
    display = Display()


class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        validate_certs = kwargs.get('validate_certs', True)

        ret = list()
        temp_list = list()
        for term in terms:
            display.vvvv("url lookup connecting to %s" % term)
            try:
                response = open_url(term, validate_certs=validate_certs)
                s = soup(response, 'html.parser').get_text()
                for z in s.replace('/','').split('\n'):
                  line =  re.split('[ ]{2,}',z)
                  if len(line) >2 and 'Name' not in line:
                    d =  datetime.strptime(line[1],"%d-%b-%Y %H:%M")
                    line[2] = d
                    temp_list.append(line)
                out = max(temp_list, key=lambda x: x[2])

            except urllib2.HTTPError as e:
                raise AnsibleError("Received HTTP error for %s : %s" % (term, str(e)))
            except urllib2.URLError as e:
                raise AnsibleError("Failed lookup url for %s : %s" % (term, str(e)))
            except SSLValidationError as e:
                raise AnsibleError("Error validating the server's certificate for %s: %s" % (term, str(e)))
            except ConnectionError as e:
                raise AnsibleError("Error connecting to %s: %s" % (term, str(e)))

            ret.append(to_unicode({"path": out[0],"date": out[1]}))
        return ret

