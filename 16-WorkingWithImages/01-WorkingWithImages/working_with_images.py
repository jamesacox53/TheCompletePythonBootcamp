import os
from PIL import Image

project_path = os.getcwd()
directory_path = os.path.join(project_path, "16-WorkingWithImages", "01-WorkingWithImages")

example_image_path = os.path.join(directory_path, "example.jpg")
pencils_image_path = os.path.join(directory_path, "pencils.jpg")

mac_image = Image.open(example_image_path)
# mac_image.show()

cropped_mac_image = mac_image.crop((0, 0, 100, 100))
# cropped_mac_image.show()

pencils_image = Image.open(pencils_image_path)
# pencils_image.show()

print(pencils_image.size)

# THese are coordinates, not a measure of width and height
# To get top 3 pencils:
x = 0
y = 0
w = 1950 / 3
h = 1300 / 10

cropped_pencils_image = pencils_image.crop((x, y, w, h))
# cropped_pencils_image.show()

# To get bottom 3 pencils:
x = 0
y = 1100
w = 1950 / 3
h = 1300

cropped_pencils_image_2 = pencils_image.crop((x, y, w, h))
# cropped_pencils_image_2.show()

halfway = 1993 / 2
x = halfway - 200
w = halfway + 200
y = 800
h = 1257

computer_image = mac_image.crop((x, y, w, h))
# computer_image.show()

mac_image.paste(im=computer_image, box=(0, 0))
# mac_image.show()

mac_image.paste(im=computer_image, box=(796, 0))
# mac_image.show()

mac_image = mac_image.resize((3000, 500))
# mac_image.show()

mac_image = mac_image.rotate(90)
# mac_image.show()

# RGBA

red_image_path = os.path.join(directory_path, "red_color.jpg")
blue_image_path = os.path.join(directory_path, "blue_color.jpg")

red_image = Image.open(red_image_path)
blue_image = Image.open(blue_image_path)

# Completely transparent
red_image.putalpha(0)
# red_image.show()

red_image.putalpha(128)
# red_image.show()

blue_image.putalpha(128)

blue_image.paste(im=red_image, box=(0, 0), mask=red_image)
# blue_image.show()

purple2_image_path = os.path.join(directory_path, "purple2_color.png")
blue_image.save(purple2_image_path)