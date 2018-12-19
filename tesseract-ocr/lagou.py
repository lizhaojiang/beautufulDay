import pytesseract
from PIL import Image
from urllib import request
import time


def main():
    # 指定tesseract图形识别库的安装路径
    pytesseract.pytesseract.tesseract_cmd = r"D:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
    url = "www.baidu.com"
    while True:
        request.urlretrieve(url,'yanzhenma.png') #下载url地址中的文件,下载文件命名为 验证码.png
        image = Image.open('yanzhengma.png') #打开下载好的图片
        text = pytesseract.image_to_string(image) #识别图片

        time.sleep(2) #防止请求的太频繁



if __name__ == '__main__':
    main()