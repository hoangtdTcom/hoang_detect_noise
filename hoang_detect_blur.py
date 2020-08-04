import numpy as np
import cv2
import os

val_resize = 160
number_out_image = 150
threshold_dark = 70
min_size = 200
min_var_image = 100

def save_file(dir_out_path , path , img):
    if not os.path.exists(dir_out_path):
        os.makedirs(dir_out_path)    
    save_path = dir_out_path + path
    cv2.imwrite(save_path, img)


# dir_in = 'Le_Van_Long_TC1001045'
for dir_in in os.listdir('Dataset/align_noresize'):
    dir_in_path = 'Dataset/align_noresize/' + dir_in
    list_var_image = []
    list_var = []
    print(dir_in_path)
    if os.path.isdir(dir_in_path):
        for path in os.listdir(dir_in_path):
            image_path = dir_in_path + "/" + path
            if os.path.isfile(image_path):
                image = cv2.imread(image_path)
                image_resize = cv2.resize(image, (val_resize, val_resize))
                gray = cv2.cvtColor(image_resize, cv2.COLOR_BGR2GRAY)
                mean_dark = np.mean(gray)
                if image.shape[1] >= min_size:
                    if mean_dark >= threshold_dark:
                        var_image_gray = cv2.Laplacian(gray, cv2.CV_64F, ksize=1).var()
                        list_var_image.append((var_image_gray, path))
                        list_var.append(var_image_gray)
        mean_var = np.mean(list_var)
        print(mean_var)
        for i in list_var_image:
            if i[0] >= mean_var:
                image_top = cv2.imread(dir_in_path + "/" + i[1])
                image_top = cv2.resize(image_top , (val_resize, val_resize))
                cv2.putText(image_top, "{:.2f}".format(i[0]), (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
                dir_out_path = 'noise/' + dir_in + '/image normal 2/'
                save_file(dir_out_path, i[1], image_top)

