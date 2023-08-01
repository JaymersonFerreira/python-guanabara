import urllib
import urllib.request

try: 
    site = urllib.request.urlopen('http://pudim.com.br')
except urllib.error.URLErro:
    print('Deu erro')
else:
    print('Tudo Ok')
    # print(site.read())