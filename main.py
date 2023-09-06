from split_sat_img_tif_by_grid import *
import zipfile
import rasterio

# pip install -r requirements.txt <-------- run this first on terminal


# [todo]: change path to your data path
zipfile_path = '../data/Barcelona/Barcelona_MS/Barcelona_1M/'

# [todo]: define your grid by rows and cols
num_rows = 5
num_cols = 5

# [todo]: if you want to see progress of your program
progress_flag = True

# [todo]: change to your satisfy save folder
save_path = './results/'



all_zipfiles = get_allFilenames_in_folder(zipfile_path)


all_zipfiles = all_zipfiles[:5] # test with 5 files

for index, file in enumerate(all_zipfiles):
    if progress_flag:
        print(f'----- Start {index+1}/{len(all_zipfiles)} -----')
    zip_file_path = zipfile_path+file
    root_name = file.split('.')[0]

    # Open the ZIP file in read mode
    with zipfile.ZipFile(zip_file_path, 'r') as zip_file:

        # List all the files and folders inside the ZIP file
        file_list = zip_file.namelist()
        extract_path = './extracting_directory/'
        for file_name in file_list:
            if '.TIF' in file_name:
                zip_file.extract(file_name, extract_path)
    #             tif_img_path = zip_file_path+'/'+file_name
                data = rasterio.open(extract_path+file_name)
                img_name = root_name+'_'+file_name.replace('/','_').split('.')[0]

                # start split satellite image
                split_tiff_image(data=data,
                                 num_rows=num_rows,
                                 num_cols=num_cols,
                                 img_name=img_name,
                                save_path=save_path)
    if progress_flag:
        print(f'----- Complete {index+1}/{len(all_zipfiles)}-----')
        
    