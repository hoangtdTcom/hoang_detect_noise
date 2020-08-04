import cv2
import imagehash
from PIL import Image

image1 = Image.open('Dataset/align_noresize/Dao_Hoang_Son_TC1001037/Dao_Hoang_Son_TC1001037_14344130062020_277.png')
image2 = Image.open('Dataset/align_noresize/Dao_Hoang_Son_TC1001037/Dao_Hoang_Son_TC1001037_14344130062020_27.png')

# image_1 = cv2.imread('Dataset/align_noresize/Dao_Hoang_Son_TC1001037/Dao_Hoang_Son_TC1001037_14344130062020_26.png')
# image_2 = cv2.imread('Dataset/align_noresize/Dao_Hoang_Son_TC1001037/Dao_Hoang_Son_TC1001037_14344130062020_27.png')

hash_1 = imagehash.average_hash(image1)
print(hash_1)
hash_2 = imagehash.average_hash(image2)
print(hash_2)



print(hash_1-hash_2)
