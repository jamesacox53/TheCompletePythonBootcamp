import os
from PIL import Image

project_path = os.getcwd()
directory_path = os.path.join(project_path, "16-WorkingWithImages", "02-Exercise")

mask_image_path = os.path.join(directory_path, "mask.jpg")
word_matrix_image_path = os.path.join(directory_path, "word_matrix.jpg")

mask_image = Image.open(mask_image_path)
word_matrix_image = Image.open(word_matrix_image_path)

# mask_image.show()

mask_image = mask_image.resize(word_matrix_image.size)
# mask_image.show()

mask_image.putalpha(100)
# mask_image.show()

word_matrix_image.paste(mask_image, (0, 0), mask_image)
word_matrix_image.show()

print("GREAT WORK WITH IMAGES YOU ARE THE BEST")