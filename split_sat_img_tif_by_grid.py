
import os

import rasterio
from rasterio.windows import Window

from matplotlib import pyplot as plt
from rasterio.windows import Window


def get_allFilenames_in_folder(path_to_folder):
    list_ = []
    with os.scandir(path_to_folder) as entries:
        for entry in entries:
            if entry.is_file():
                list_.append(entry.name)
    return list_


def save_tiff_img(data,sat_image,save_path,new_width,new_height,num_bands):
    # print('-----start save image----')
    if len(data.dtypes)>1:
        dtype = data.dtypes[0]
    else:
        dtype = data.dtypes
    with rasterio.open(
        f'{save_path}.tif', 'w',
        driver='GTiff', width=new_width, height=new_height, count=num_bands,
        dtype=dtype) as dst:
        dst.write(sat_image)
    # print('----completely save image----')
    
    
def create_folder(folder_path):
    if os.path.exists(folder_path):
        # print(f"The folder '{folder_path}' exists.")
        print()
    else:
        # print(f"The folder '{folder_path}' does not exist. create it!!")
        os.makedirs(folder_path)
        # print(f"The folder '{folder_path}' is created, completelly.")
        
        
def split_tiff_image(data,num_rows,num_cols,img_name,save_path):
    img_width = data.width
    img_height = data.height
    num_band = data.count
    
    new_img_width = img_width//num_rows # size of new width
    new_img_height = img_height//num_cols # size of new height
    
    create_folder(save_path)
    
 
    for row in range(num_rows):
        for col in range(num_cols):
            folder_name = f'{save_path}{row}_{col}'
            create_folder(folder_name)
            image_name = folder_name+f'/{img_name}_{row}_{col}'
           
            new_img = data.read(window=Window(col,row,new_img_width,new_img_height))
            
            save_tiff_img(data,
                          new_img,
                          image_name,
                         new_img_width,
                         new_img_height,
                         num_band)
    # print('Completely, run split image')
    