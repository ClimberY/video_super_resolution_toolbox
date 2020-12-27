import cv2

for big_i in range(1, 3344):
    src = cv2.imread('Vid4/sandy/%04d.jpg' % big_i, -1)
    cnt = 1
    num = 1
    sub_images = []
    sub_image_num = 2
    src_height, src_width = src.shape[0], src.shape[1]
    sub_height = src_height // sub_image_num
    sub_width = src_width // sub_image_num
    for j in range(sub_image_num):
        for i in range(sub_image_num):
            if j < sub_image_num - 1 and i < sub_image_num - 1:
                image_roi = src[j * sub_height: (j + 1) * sub_height, i * sub_width: (i + 1) * sub_width, :]
            elif j < sub_image_num - 1:
                image_roi = src[j * sub_height: (j + 1) * sub_height, i * sub_width:, :]
            elif i < sub_image_num - 1:
                image_roi = src[j * sub_height:, i * sub_width: (i + 1) * sub_width, :]
            else:
                image_roi = src[j * sub_height:, i * sub_width:, :]
            sub_images.append(image_roi)
    for i, img in enumerate(sub_images):
        cv2.imwrite('Vid4/sub_img/%04d_' % big_i + str(i) + '.jpg', img)

