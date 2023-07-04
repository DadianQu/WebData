from urllib import request
from base64 import b64encode
import requests

captcha_url = ""

request.urlretrieve(captcha_url,'captcha.png')


#API
recognize_url = "https.....?type=e"

fromdata = {}
with open ('captcha.png', 'rb') as fp:
    data = fp.read()
    pic = b64encode(data)
    fromdata['pic'] = pic

appcode = ''

headers = {
    'content-type':'',
    'Authorization':'APPCODE'+appcode
}

response = requests.post(url = recognize_url, data=fromdata, headers=headers)
# print (response.json())
result = response.json()
code = result['result']['code']
print (code)




#Input captcha
def regonize_captcha(self, img_url):
    request.urlretrieve(img_url, "captcha.png")
    image = Image.open("captcha.png")
    image.show()
    image.close()
    captcha = input("Input: ")
    return captcha