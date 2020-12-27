import cv2


def video2frame(videos_path, frames_save_path, time_interval):
    vidcap = cv2.VideoCapture(videos_path)
    fps = int(vidcap.get(cv2.CAP_PROP_FPS))
    success, image = vidcap.read()
    count = 0
    while success:
        success, image = vidcap.read()
        count = count + 1
    # if count % time_interval == 0:
    #     cv2.imencode('.jpg', image)[1].tofile(frames_save_path + "frame%d.jpg" % count)
        cv2.imencode('.jpg', image)[1].tofile(frames_save_path + "%04d.jpg" % count)
    # print('一共{}张，选取其中{}张'.format(count, int(count / time_interval)))
    print( "fps=====>", fps)


if __name__ == '__main__':
    videos_path = 'linyilian.mp4'  # 视频的存放路径
    frames_save_path = 'Vid4/sandy/'  # 视频切分成帧之后图片的保存路径
    time_interval = 1  # 每5帧保存一次
    video2frame(videos_path, frames_save_path, time_interval)
