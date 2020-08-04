import cv2
import numpy as np
import os

threshold_dark = 70
threshold_blur = 70 
def save_file(dir_out_path , path , img):
    if not os.path.exists(dir_out_path):
        os.makedirs(dir_out_path)    
    save_path = dir_out_path + path
    cv2.imwrite(save_path, img)

for dir_in in os.listdir('Dataset/align_noresize'):
    dir_in_path = 'Dataset/align_noresize/' + dir_in
    print(dir_in_path)
    try:
        for path in os.listdir(dir_in_path):
            img_path = dir_in_path + '/' + path
            img = cv2.imread(img_path)
            # img = cv2.resize(img, (int(img.shape[1]/4),int(img.shape[0]/4)))
            if img.shape[1] >=300 and img.shape[0] >= 300:
                img = cv2.resize(img , (160,160))
                gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

                fm = cv2.Laplacian(gray, cv2.CV_64F).var()
                text = "Not"
                mean = np.mean(gray)
                mess = ""
                if mean <threshold_dark:
                    print('dark :' ,mean ,'fm: ', fm)
                    mess = 'Dark'
                    cv2.putText(img, "{}: {:.2f}".format(mess, mean), (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
                    # cv2.imshow("Image", img)
                    dir_out_path = dir_in_path + '/noise/dark/'
                    save_file(dir_out_path , path , img)
                    # if not os.path.exists(dir_out_path):
                    #     os.makedirs(dir_out_path)
                    # save_path = dir_out_path + path
                    # cv2.imwrite(save_path, img)
                else:
                    print('light :',mean ,'fm: ', fm)
                    if fm <= threshold_blur:
                        text = "Blur"
                        mess = text
                        cv2.putText(img, "{}: {:.2f}".format(mess, fm), (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
                        # cv2.imshow("Image", img)
                        dir_out_path = dir_in_path + '/noise/blur/'
                        save_file(dir_out_path , path , img)
                        # if not os.path.exists(dir_out_path):
                        #     os.makedirs(dir_out_path)
                        # save_path = dir_out_path + path
                        # cv2.imwrite(save_path, img)
                    else:
                        mess = text
                        cv2.putText(img, "{}: {:.2f}".format(mess, fm), (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
                        # cv2.imshow("Image", img)
                        dir_out_path = dir_in_path + '/noise/normal/'
                        save_file(dir_out_path , path , img)
                        # if not os.path.exists(dir_out_path):
                        #     os.makedirs(dir_out_path)
                        # save_path = dir_out_path + path
                        # cv2.imwrite(save_path, img)
            else:
                dir_out_path = dir_in_path + '/noise/image_small/'  
                save_file(dir_out_path , path , img)
                # if not os.path.exists(dir_out_path):
                #     os.makedirs(dir_out_path)    
                # save_path = dir_out_path + path
                # cv2.imwrite(save_path, img)    
    except:
        continue
        # if cv2.waitKey(1) == ord('q'):
        #     break
        # cv2.waitKey(0)


####################33
# import cv2

# cap = cv2.VideoCapture('Dataset/raw/Do_Thi_Lan_TC1001076/Do_Thi_Lan_TC1001076_14475530062020.h264')
# num = 0
# while True:
#     __, img = cap.read()
#     savename = 'Dataset/raw/Do_Thi_Lan_TC1001076/' + str(num) + '.png'
#     cv2.imwrite(savename,img)
#     num +=1