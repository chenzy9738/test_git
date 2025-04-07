import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector
from PIL import Image

#img_path = "D:/研究生课件/研二上/keypoints_detection/可视化对比图筛选/正文中放的图片/chair/161/gt00.png"

#交互式选择
if __name__ == '__main__':
    from PIL import Image
    import os

    # 设置路径
    # input_folder = "D:/研究生课件/研二上/keypoints_detection/可视化对比图筛选/正文中放的图片/chair/161/"
    # output_folder = "D:/研究生课件/研二上/keypoints_detection/可视化对比图筛选/裁剪后的图片/chair/"
    # 2025/3/18 更多实验补充
    input_folder = "D:/研究生课件/研二上/keypoints_detection/可视化对比图筛选/正文中放的图片/chair/161/"
    output_folder = "D:/研究生课件/研二上/keypoints_detection/可视化对比图筛选/裁剪后的图片/chair/"

    os.makedirs(output_folder, exist_ok=True)

    # 裁剪参数
    x, y, width, height = 500, 100, 1000, 1000
    crop_box = (x, y, x + width, y + height)  # (左, 上, 右, 下)

    # 遍历文件夹中的图片
    for filename in os.listdir(input_folder):
        if filename.endswith(".png"):  # 修改扩展名适配你的图片格式
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)

            # 裁剪图片
            cropped_img = img.crop(crop_box)

            # 保存裁剪后的图片
            cropped_img.save(os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_cropped.png"))

    print("批量裁剪完成！")





