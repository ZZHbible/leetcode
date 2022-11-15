#!/usr/bin/env python
# author = 'ZZH'
# time = 2022/11/15
# project = png2eps
from PIL import Image


def transparence2white(img):
    #     img=img.convert('RGBA')  # 此步骤是将图像转为灰度(RGBA表示4x8位像素，带透明度掩模的真彩色；CMYK为4x8位像素，分色等)，可以省略
    sp = img.size
    width = sp[0]
    height = sp[1]
    print(sp)
    for yh in range(height):
        for xw in range(width):
            dot = (xw, yh)
            color_d = img.getpixel(dot)  # 与cv2不同的是，这里需要用getpixel方法来获取维度数据
            if (color_d[3] == 0):
                color_d = (255, 255, 255, 255)
                img.putpixel(dot, color_d)  # 赋值的方法是通过putpixel
    return img


def pngtoeps(name):
    file = '/Users/zhangzhenhua/Desktop/' + name + '.png'

    print(file)

    last_file = '/Users/zhangzhenhua/Desktop/' + name + '.eps'

    print(last_file)

    img = Image.open(file)
    img = transparence2white(img)
    img = img.convert('RGB')
    Img = img.resize(())

    img.save(last_file, quality=100, dpi=(1200.0, 1200.0), lossless=True)


if __name__ == '__main__':
    pngtoeps(name="5")