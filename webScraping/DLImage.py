import random
import urllib.request

def download_web_image(url):
        name = random.randrange(1, 1000)
        full_name = str(name) + ".jpg"
        urllib.request.urlretrieve(url, full_name)

download_web_image("https://s-media-cache-ak0.pinimg.com/originals/4a/4f/ee/4a4fee091e0254bb603242067f4def7d.jpg")
# will download in the same directory as our program is running (webScraping?)