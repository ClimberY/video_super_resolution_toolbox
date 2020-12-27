import os

im_dir = 'Vid4/sub_img/'
im_list = os.listdir(im_dir)
# im_list.sort(key=lambda x: int(x.replace("_RBPNF7", "").split('.')[0]))
with open("./Vid4/sub_img.txt",'a') as f:
    for i in range(3343, len(im_list)+1):
        for j in range(0, 4):
            im_name = os.path.join("sub_img/" + "%04d" % i + '_%d.jpg' % j)
            f.write(im_name+"\n")
f.close()