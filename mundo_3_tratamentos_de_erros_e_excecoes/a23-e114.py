import urllib.request
from urllib.error import URLError, HTTPError

try:
    site = urllib.request.urlopen("https://www.youtube.com/", timeout=5)
except HTTPError as e:
    print(f"Erro HTTP: {e.code}")
except URLError:
    print("Site inacessível ou sem conexão.")
else:
    print(f"Site acessível! Código: {site.getcode()}")







