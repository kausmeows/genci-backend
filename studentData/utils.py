import requests

def getCertiURL(url):
    certi_url = requests.post(url)
    return certi_url.certificate_url
    

