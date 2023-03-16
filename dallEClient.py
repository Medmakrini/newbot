import os
import requests
import openai
from PIL import Image

openai.api_key = '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'  # your api key


def generate(promptText):
    url = openai.Image.create(prompt=promptText, n=1, size="1024x1024")["data"][0]["url"]
    print("Generated img url: ", url)

    img = requests.get(url).content
    imgPath = os.path.join(os.getcwd(), "img.png")
    with open(imgPath, "wb+") as f:
        f.write(img)

    imgPath = pngToJpj(imgPath)
    print("img saved to: ", imgPath)
    return imgPath


def pngToJpj(path):
    im = Image.open(path)
    rgb_im = im.convert('RGB')
    newPath = path.replace(".png", ".jpg")
    rgb_im.save(newPath)
    return newPath
