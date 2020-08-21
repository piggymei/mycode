import requests
import wget

datepic = input("what date do you like for the image? (YYYY-MM-DD) ")
resolution = input("would you like the image in High definition or standard definition?(High or Standard) ").lower()

API_KEY = "8EWWTP0IkiMrdVGucP6AOEMJsviwqjbPzHZ3zqLr"
url = "https://api.nasa.gov/planetary/apod?date=" + datepic +"&api_key=" + API_KEY

r = requests.get(url)
resp = r.json()
#print(resp)
dateofpicture = resp["date"] 
titleofpicture = resp["title"]
descriptionofpicture = ["explanation"]
pic_url = resp["url"]
pic_hurl = resp["hdurl"]
if resolution == "high":
    wget.download(pic_hurl, 'dateofpicturehigh.jpg')
    wget.download("https://www.chanel.com/images/t_fashionzoom1/f_jpg/classic-handbag-black-velvet-gold-tone-metal-velvet-gold-tone-metal-packshot-default-as1939b0339894305-8826166935582.jpg")
else:
    wget.download(pic_url, 'dateofpicture.jpg')

