import os
import PIL.Image as Image

IMAGES_PATH = '/media/hy/Seagate Expansion Drive/Results/Vid4/sub_img_8x/'  # 图片集地址
IMAGES_FORMAT = ['.jpg', '.png', '.JPG']  # 图片格式
IMAGE_SIZE_row = 1104  # 每张小图片的大小
IMAGE_SIZE_column = 1472
IMAGE_ROW = 2  # 图片间隔，也就是合并成一张图后，一共有几行
IMAGE_COLUMN = 2  # 图片间隔，也就是合并成一张图后，一共有几列


# 定义图像拼接函数
def image_compose(IMAGE_SAVE_PATH):
    to_image = Image.new('RGB', (IMAGE_COLUMN * IMAGE_SIZE_column, IMAGE_ROW * IMAGE_SIZE_row))  # 创建一个新图
    # 循环遍历，把每张图片按顺序粘贴到对应位置上
    for y in range(1, IMAGE_ROW + 1):
        for x in range(1, IMAGE_COLUMN + 1):
            from_image = Image.open(IMAGES_PATH + image_names[IMAGE_COLUMN * (y - 1) + x - 1]).resize(
                (IMAGE_SIZE_column, IMAGE_SIZE_row), Image.ANTIALIAS)
            to_image.paste(from_image, ((x - 1) * IMAGE_SIZE_column, (y - 1) * IMAGE_SIZE_row))
    return to_image.save(IMAGE_SAVE_PATH)  # 保存新图


for i in range(0, 3344):
    IMAGE_SAVE_PATH = '/media/hy/Seagate Expansion Drive/Results/merge_dir/%4d_RBPNF7.png' % i  # 图片转换后的地址
    im_list = os.listdir(IMAGES_PATH)
    im_list.sort(key=lambda x: int(x.replace("_RBPNF7", "").split('.')[0]))
    # 获取图片集地址下的所有图片名称
    # image_names = [name for name in im_list for item in IMAGES_FORMAT if
    #                os.path.splitext(name)[1] == item]
    image_names = im_list[(i*4):(i*4)+4]
    # print("image_names", image_names)
    # 简单的对于参数的设定和实际图片集的大小进行数量判断
    # if len(image_names) != IMAGE_ROW * IMAGE_COLUMN:
    #     raise ValueError("合成图片的参数和要求的数量不能匹配！")
    image_compose(IMAGE_SAVE_PATH)  # 调用函数

