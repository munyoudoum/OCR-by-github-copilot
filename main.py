# read an image using opencv
# and display it using matplotlib
import pytesseract
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image2.jpeg')
# use pytesseract to extract text from image
text = pytesseract.image_to_string(img)
print(text)

plt.imshow(img)
plt.show()
