# 图像增强
# 图像增强是指通过一系列变换方法，在保持图像语义不变的前提下，生成多样化的新图像数据
# 图像增强可以分为以下几类:
# 几何变换
# 颜色变换
# 噪声与模糊
# 遮罩
# 其他技术

import torch
from PIL import Image
import matplotlib.pyplot as plt
import torchvision.transforms as transforms
from pathlib import Path
import os
import numpy as np
import random

# 几何变换
## 旋转
def imshow(img_path, transform):
    """
    Function to show data augmentation
    Param img_path: path of the image
    Param transform: data augmentation technique to apply
    """
    
    img_path = Path(img_path)
    img_path = img_path if img_path.is_absolute() else os.path.abspath(img_path)
    
    img = Image.open(img_path)
    fig, ax = plt.subplots(1, 2, figsize=(15,4))
    ax[0].set_title(f'Original image {img.size}')
    ax[0].imshow(img)
    img = transform(img)
    ax[1].set_title(f'Transformed image {img.size}')
    ax[1].imshow(img)
    plt.show()

def cutout_pil_multi(image, mask_size=50, num_masks=3):
    """
    对图像应用多个Cutout遮挡块

    参数：
    - image: PIL.Image 对象
    - mask_size: 每个遮挡块的大小（正方形边长）
    - num_masks: 遮挡块的数量
    """

    image_np = np.array(image).copy()
    h, w = image_np.shape[0], image_np.shape[1]

    for _ in range(num_masks):
        y = random.randint(0, h-1)
        x = random.randint(0, w-1)

        y1 = max(0, y - mask_size // 2)
        y2 = min(h, y + mask_size // 2)
        x1 = max(0, x - mask_size // 2)
        x2 = min(w, x + mask_size // 2)

        # 遮挡区域设置为黑色
        image_np[y1:y2, x1:x2, :] = 0

    return Image.fromarray(image_np)



if __name__ == '__main__':
    img_path = r'rethink/10/images/59.jpg'

    # 旋转
    # 旋转度数随机设置为-30到30度之间
    transform = transforms.RandomRotation(degrees=30)
    imshow(img_path, transform)
    # 翻转
    # p表示翻转的概率
    # 水平翻转
    transform = transforms.RandomHorizontalFlip(p=1.0)
    imshow(img_path, transform)
    # 垂直翻转
    transform = transforms.RandomVerticalFlip(p=1.0)
    imshow(img_path, transform)
    # 随机裁剪
    transform = transforms.RandomCrop(size=(120, 120))
    imshow(img_path, transform)
    # 透视变换 用于模拟图像拍摄时角度扭曲的效果
    transform = transforms.RandomPerspective(
        distortion_scale = 0.5,   # 控制变形强度，0~1，越大越扭曲
        p = 1.0, # 应用该变换的概率
        # 图像缩放时的插值方式，BILINEAR:双线性插值，平滑效果
        interpolation=transforms.InterpolationMode.BILINEAR
    )
    imshow(img_path, transform)
    # 颜色对比
    # 亮度、对比度、饱和度、色调
    transform = transforms.ColorJitter(
        brightness=0.5,     # 亮度
        contrast=0.5,       # 对比度
        saturation=0.5,     # 图像颜色的鲜艳程度
        hue=0.1             # 控制色调在色环上旋转
    )
    imshow(img_path, transform)

    # 模糊
    # 高斯模糊
    # 对图像进行高斯模糊， kernel size为5， sigma可调节模糊强度
    transform = transforms.GaussianBlur(kernel_size=5, sigma=(0.1, 3.0))
    imshow(img_path, transform)

    # 遮罩
    # 通过在训练图像上随即遮挡一个或多个连续的方形区域，从而让模型学会忽略局部特征，更关注整体上下文特征
    imshow(img_path, cutout_pil_multi)