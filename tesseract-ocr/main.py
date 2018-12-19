import pytesseract
from PIL import Image

#指定tesseract的安装路径
pytesseract.pytesseract.tesseract_cmd = r"D:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
#打开图片
image = Image.open('c.jpg')


#转化为文本信息

#识别英文的图形
# text = pytesseract.image_to_string(image)

#识别中文图形
text = pytesseract.image_to_string(image,lang='chi_sim')
print(text)