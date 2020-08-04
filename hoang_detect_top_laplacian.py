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


for dir_in in os.listdir('Dataset/align_noresize'):
    dir_in_path = 'Dataset/align_noresize/' + dir_in
    top_var_image = []
    list_image_blur = []
    print(dir_in_path)
    
    if os.path.isdir(dir_in_path):
        for path in os.listdir(dir_in_path):
            image_path = dir_in_path + "/" + path
            if os.path.isfile(image_path):
                image = cv2.imread(image_path)
                image_resize = cv2.resize(image, (val_resize, val_resize))
                # blur = cv2.GaussianBlur(image_resize,(3,3),0)
                gray = cv2.cvtColor(image_resize, cv2.COLOR_BGR2GRAY)
                mean_dark = np.mean(gray)
                if image.shape[1] <= min_size:
                    cv2.putText(image, "W: {:.2f} H: {:.2f}".format(image.shape[1],image.shape[0]), (10, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
                    dir_out_path = 'noise/' + dir_in + '/image_small/'
                    save_file(dir_out_path, path, image)
                else:   
                    if mean_dark >= threshold_dark:
                        var_image_gray = cv2.Laplacian(gray, cv2.CV_64F, ksize=1).var()
                        if var_image_gray >= min_var_image:
                            if len(top_var_image) < number_out_image:
                                top_var_image.append((var_image_gray,path))
                                top_var_image.sort(reverse=True)
                            else:
                                if top_var_image[-1][0] < var_image_gray:
                                    list_image_blur.append((top_var_image[-1][0],top_var_image[-1][1]))
                                    top_var_image.pop()
                                    top_var_image.append((var_image_gray,path))
                                    top_var_image.sort(reverse=True)
                        else:
                            list_image_blur.append((var_image_gray, path))           
                        cv2.putText(image_resize, "{:.2f}".format(var_image_gray), (10, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
                        dir_out_path = 'noise/' + dir_in + '/scores_laplacian/'
                        save_file(dir_out_path , path , image_resize)

                    else: 
                        cv2.putText(image, "Mean Dark: {:.2f}".format(mean_dark), (10, 30),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
                        dir_out_path = 'noise/' + dir_in + '/image_dark/'
                        save_file(dir_out_path, path, image)
        print('Length top_var_image: ' , len(top_var_image))
        print('Length list_motion_blur: ', len(list_image_blur))
        for i in range(len(top_var_image)):
            image_top = cv2.imread(dir_in_path + "/" + top_var_image[i][1])
            image_top = cv2.resize(image_top , (val_resize, val_resize))
            cv2.putText(image_top, "{:.2f}".format(top_var_image[i][0]), (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
            dir_out_path = 'noise/' + dir_in + '/image normal/'
            save_file(dir_out_path, top_var_image[i][1], image_top)

        for a in range(len(list_image_blur)):
            image_blur = cv2.imread(dir_in_path + "/" + list_image_blur[a][1])
            image_blur = cv2.resize(image_blur, (val_resize,val_resize))
            cv2.putText(image_blur, "{:.2f}".format(list_image_blur[a][0]), (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
            dir_out_path = 'noise/' + dir_in + '/motion_blur/'
            save_file(dir_out_path, list_image_blur[a][1], image_blur)
        
    