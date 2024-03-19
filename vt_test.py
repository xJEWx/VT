import requests
import json
import csv
import re

url_vt = 'https://www.virustotal.com/gui/domain/google.com'
apikey = 'apikey'


def vt_reports():
    params = ('q', 'requests+language:python')
    # params = {
    #           'apikey': apikey,
    #           'resource': get_resource
    #          }
    response = requests.get(url_vt,
                            params=params,
                            proxies=proxies,
                            verify=False
                            )
    return response

print(vt_reports())

params = {
    'apikey': apikey,
    'resource': get_resource
}
response = requests.get(url_vt, params=params, proxies=proxies, verify=False, timeout=4)
return response.json()
