import cv2
import os
import numpy as np
from PIL import Image


def frame2video(im_dir, video_dir, fps):
    im_list = os.listdir(im_dir)
    im_list.sort(key=lambda x: int(x.replace("_RBPNF7", "").split('.')[0]))
    img = Image.open(os.path.join(im_dir, im_list[0]))
    img_size = img.size  # 获得图片分辨率，im_dir文件夹下的图片分辨率需要一致
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    videoWriter = cv2.VideoWriter(video_dir, fourcc, fps, img_size)
    for i in im_list:
        im_name = os.path.join(im_dir + i)
        frame = cv2.imdecode(np.fromfile(im_name, dtype=np.uint8), -1)
        videoWriter.write(frame)
    videoWriter.release()


if __name__ == '__main__':
    im_dir = '/media/hy/Seagate Expansion Drive/Results/merge_dir/'  # 帧存放路径
    video_dir = '/media/hy/Seagate Expansion Drive/Results/sandy.mp4'  # 合成视频存放的路径
    fps = 15  # 帧率
    frame2video(im_dir, video_dir, fps)
