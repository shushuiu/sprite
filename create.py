import os
from PIL import Image
import re
import random
import datetime
import sprite

'''
代码中一些字符注释：
w:图片宽度
h:图片高度

'''

# 生成雪碧图片和css，放在哪里的路径
spritePath = '/Users/watson/PycharmProjects/sprite/publish/'

# 需要合成雪碧图片的小图片路径
imagesPath = '/Users/watson/PycharmProjects/sprite/pic/'

# class 前缀
prefix = 'review'

# class 标识符
classSign = '-'

files = os.listdir(imagesPath)

# 生成 sprite 的名字
now = datetime.datetime.now()
d1 = '%d-' % int(random.random() * 10000)
d2 = '%d-%d-%d' % (now.year, now.month, now.day)

spriteName = prefix + classSign + d1 + d2 + '.png'

sizeList = []
imgList = []
imgNameList = []

for f in files:
    imgNameList.append(f)

    img = Image.open(imagesPath + f)
    imgList.append(img)

    w, h = img.size
    sizeList.append([w, h])

result = sprite.createSprite(sizeList)
print(result)

width = result['w']
height = result['h']
r = result['r']

# 创建画布 画布为10*10大小，最多可以存放100张图片
canvas = Image.new('RGBA', (width, height))

# 合并图片
for v in r:
    p = v['p']
    img = imgList[p]
    # 原本图片大小缩放十倍
    img = img.resize((width // 10, height // 10), Image.ANTIALIAS)
    x = v['x']
    y = v['y']
    canvas.paste(img, (x, y))

    name = imgNameList[p]
    imgName = re.sub(r'[^\w]', '-', name)
    classname = prefix + classSign + imgName

# end for v in r

# 输出图片
canvas.save(spritePath + spriteName, 'png')

print('生成完毕')
