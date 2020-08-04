

import os
import shutil


key = input('1. Xoa folder \n2. Dem file \n3. Coyy file noise \nNhap so: ')
if key == '1':
    input_folder = input('Nhap folder muon xoa: ')
    for dir_in in os.listdir('Dataset/align_noresize'):
        dir_in_path = 'Dataset/align_noresize/' + dir_in
        
        ############# REMOVE FOLDER #############################
        try:
            # remove_file = dir_in_path + '/noise/top_laplacian_2'
            remove_file = 'noise/' + dir_in + '/' + input_folder
            shutil.rmtree(remove_file)
        except:
            continue

        
        ############# COUNT FILE ##############################
if key == '2':
    for dir_in in os.listdir('Dataset/align_noresize'):
        dir_in_path = 'Dataset/align_noresize/' + dir_in
        print('###############################################################')
        try:
            print(dir_in_path, "\t\tcount laplacian: {:.2f}".format (len(os.listdir(dir_in_path + '/noise/laplacian'))/len(os.listdir(dir_in_path))))
            print(dir_in_path, "\t\tcount canny: {:.2f}".format (len(os.listdir(dir_in_path + '/noise/canny'))/len(os.listdir(dir_in_path))))
            print(dir_in_path, "\t\tcount sobelx: {:.2f}".format (len(os.listdir(dir_in_path + '/noise/sobelx'))/len(os.listdir(dir_in_path))))
            print(dir_in_path, "\t\tcount sobely: {:.2f}".format (len(os.listdir(dir_in_path + '/noise/sobely'))/len(os.listdir(dir_in_path))))
        except:
            continue
        ############# COPY FOLDER #############################
from distutils.dir_util import copy_tree
if key == '3':
    input_folder = input('Nhap folder muon copy: ')
    for dir_in in os.listdir('Dataset/align_noresize'):
        if os.path.isdir('Dataset/align_noresize/' + dir_in):
        # dir_in_path = 'Dataset/align_noresize/' + dir_in + '/top_laplacian_2'
            dir_in_path = 'noise/' + dir_in + "/" + input_folder
            dir_coming = 'image/' + dir_in + "/" + input_folder
            try: 
                if not os.path.exists(dir_coming):
                    os.makedirs(dir_coming) 
                copy_tree(dir_in_path, dir_coming)
            except:
                continue
        