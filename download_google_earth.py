import requests
import shutil

url = "https://earthview.withgoogle.com/download/{}.jpg"
for i in range(1, 10000):
    response = requests.get(url.format(i), stream=True)
    with open("/home/carter/Downloads/ge_wallpapers/google_earth_{}.jpg".format(i), "wb") as out_img:
        shutil.copyfileobj(response.raw, out_img)
    print("Save image {}".format(i))

