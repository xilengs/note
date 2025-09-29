# 选择性搜索
# 该方法结合了层次化分割和多样化策略，在生成候选目标区域时兼顾了目标位置的质量和计算效率。
"""
现在看来效果很差，处理一张图片，时间都很长：
    对于photo中的简单猫咪图片,fast用时1s左右,quality用时6s多;
    如果是复杂人物场景图片，fast用时15s, quality用时41s！而且效果很差，场景中的人物无法找到
"""
import time

import cv2
import matplotlib.pyplot as plt

# 读取图像
img = cv2.imread("photo/R.jpg")
new_img_f = img.copy()
new_img_q = img.copy()

# 创建 selective search 对象
ssf = cv2.ximgproc.segmentation.createSelectiveSearchSegmentation()
ssq = cv2.ximgproc.segmentation.createSelectiveSearchSegmentation()
ssf.setBaseImage(img)
ssq.setBaseImage(img)

# 选择模式: 'f' 快速, 'q' 质量高
ssf.switchToSelectiveSearchFast()
ssq.switchToSelectiveSearchQuality()

# 得到候选区域
start = time.time()
rects_f = ssf.process()
end = time.time()
print(f"ssf 得到总共 {len(rects_f)} 个候选区域, 用时 {end-start:.4f} sec")
start = time.time()
rects_q = ssq.process()
end = time.time()
print(f"ssq 得到总共 {len(rects_q)} 个候选区域, 用时 {end-start:.4f} sec")

for i, (x, y, w, h) in enumerate(rects_f[:100]):
    cv2.rectangle(new_img_f, (x, y), (x+w, y+h), (0, 255, 0), 2)
for i, (x, y, w, h) in enumerate(rects_q[:100]):
    cv2.rectangle(new_img_q, (x, y), (x+w, y+h), (0, 255, 0), 2)

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(new_img_f, cv2.COLOR_BGR2RGB))
plt.title("Selective Search Fast")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(new_img_q, cv2.COLOR_BGR2RGB))
plt.title("Selective Search Quality")
plt.axis("off")

# 保存图片
"""
cv2.imwrite("python/algorithm_use/photo/ssf.jpg", new_img_f)
cv2.imwrite("python/algorithm_use/photo/ssq.jpg", new_img_q)
"""

plt.savefig("photo/selective_search_R.png", dpi=300)

# 展示
plt.tight_layout()
plt.show()
