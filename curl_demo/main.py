import pycurl
from io import BytesIO

def post_req(url, data, headers={}):
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.POSTFIELDS, data)
    c.setopt(c.HTTPHEADER, headers)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    return buffer.getvalue().decode('utf-8')

def get_req(url):
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    return buffer.getvalue().decode('utf-8')


if __name__ == '__main__':
    url = 'https://a279623002.github.io/code/note/question/'
    print(get_req(url))