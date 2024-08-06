import requests
import bs4
import os

result = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")

soup = bs4.BeautifulSoup(result.text, "lxml")

img_elems = soup.select('.mw-body-content img')

images_want = []

for elem in img_elems:
    src = elem['src']

    if 'Deep_Blue.jpg' in src:
        images_want.append(str(src))
    
    if 'Kasparov_Magath' in src:
        images_want.append(str(src))

print(images_want)

directory_path = os.path.join(os.getcwd(), "15-WebScraping", "03-GrabbingAnImage")

for image_src in images_want:
    image_link = requests.get("https:" + image_src)
    image_name = image_src.split("/")[-1]

    file_path = os.path.join(directory_path, image_name)

    f = open(file_path, 'wb')
    f.write(image_link.content)
    f.close()