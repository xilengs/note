# PIL: python imaging library, python平台的图像处理标准库
# PIL仅支持到python 2.7，所以一群志愿者在PIL的基础上创建了兼容的版本，叫Pillow,支持python 3.x
# 安装pillow
# pip install pillow
# 操作图像
from PIL import Image
im = Image.open('python/LiaoLearning/17/test.png')
# 获得图像尺寸
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
# 保存
im.save(r'python/LiaoLearning/17/thumbanil.png', 'PNG')

# 加模糊
from PIL import ImageFilter
im = Image.open('python/LiaoLearning/17/test.png')
im2 = im.filter(ImageFilter.BLUR)
im2.save(r'python/LiaoLearning/17/blur.png', 'PNG')

# PIL绘图
# 生成字母验证码图
from PIL import ImageDraw, ImageFont, ImageFilter
import random

# 随机字母
def rndChar():
    return chr(random.randint(65, 90))

def rndColor():
    return (random.randint(64, 225), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象：
font = ImageFont.truetype('python/LiaoLearning/17/ARIAL.TTF', 36)
# 创建Draw对象
draw = ImageDraw.Draw(image)
# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x,y), fill=rndColor())

for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())

image = image.filter(ImageFilter.BLUR)
image.save('python/LiaoLearning/17/code.jpg','jpeg')