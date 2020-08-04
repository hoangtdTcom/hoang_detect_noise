import matplotlib.pyplot as plt
import numpy as np

def detect_blur_fft(image, size =60):
    (h, w) = image.shape
    (cx, cy) = (int(w/2), int(h/2))
    
    fft = np.fft.fft2(image)
    fftShift = np.fft.fftshift(fft)
    
    fftShift[cy - size:cy + size, cx - size:cx + size] = 0
    fftShift = np.fft.ifftshift(fftShift)
    recon = np.fft.ifft2(fftShift)

    magnitude = 20 * np.log(np.abs(recon))
    mean = np.mean(magnitude)
    return mean

import imutils
import cv2
import os

val_resize = 160
min_size = 200
threshold_dark = 70

dir_in = 'Le_Van_Long_TC1001045'
dir_in_path = 'Dataset/align_noresize/' + dir_in
list_fft_image = []
list_mean_fft = []
list_var_image = []
list_var = []
print(dir_in_path)

def save_file(dir_out_path , path , img):
    if not os.path.exists(dir_out_path):
        os.makedirs(dir_out_path)    
    save_path = dir_out_path + path
    cv2.imwrite(save_path, img)

for path in os.listdir(dir_in_path):
    image_path = dir_in_path + "/" + path
    if os.path.isfile(image_path):
        image = cv2.imread(image_path)
        image_resize = cv2.resize(image, (val_resize, val_resize))
        gray = cv2.cvtColor(image_resize, cv2.COLOR_BGR2GRAY)
        mean_dark = np.mean(gray)
        if image.shape[1] >= min_size:
            if mean_dark >= threshold_dark:
                (mean) = detect_blur_fft(gray, size=60)

                image_gray = np.dstack([gray] * 3)

                var_image_gray = cv2.Laplacian(gray, cv2.CV_64F, ksize=1).var()
                list_var_image.append((var_image_gray, path))
                list_var.append(var_image_gray)
                list_fft_image.append((mean, path))
                list_mean_fft.append(mean)
mean_list_mean_fft = np.mean(list_mean_fft)
mean_var = np.mean(list_var)
normal = 0
blur = 0
ss_list_normal = []
ss_list_blur = [] 
for i in list_fft_image:
    if i[0] >= mean_list_mean_fft:
        image = cv2.imread(dir_in_path + "/" + i[1])
        image = cv2.resize(image, (val_resize,val_resize))
        cv2.putText(image, '{:.2f}'.format(i[0]), (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.7 , (0,255,0), 3)
        normal +=1
        dir_out_path = 'noise/' + dir_in + '/image normal fft/'
        save_file(dir_out_path, i[1], image)

    else:
        image = cv2.imread(dir_in_path + "/" + i[1])
        image = cv2.resize(image, (val_resize,val_resize))
        cv2.putText(image, '{:.2f}'.format(i[0]), (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.7 , (0,0,255), 3)
        blur += 1
        dir_out_path = 'noise/' + dir_in + '/blur fft/'
        save_file(dir_out_path, i[1], image)
    if i[0] >= mean_var:
        ss_list_normal.append((i[0],i[1]))
    else:
        ss_list_blur.append((i[0],i[1]))
while True:

    # cv2.imshow('out', image)
    # if cv2.waitKey() == ord('q'):
    #     break
print('Mean list: ', mean_list_mean_fft)
print('Normal: ', normal )
print('Blur: ', blur)
print('Rate normal: ', (normal/len(list_mean_fft)))
print('Rate blur: ', (blur/len(list_mean_fft)))
print('Giong nhau normal:' ,)


