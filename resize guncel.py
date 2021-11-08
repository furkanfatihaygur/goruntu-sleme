import os
from PIL import Image
import numpy as np


def convertImage():
    img = Image.open(img_path)
    img = img.convert("RGBA")
  
    datas = img.getdata()
  
    newData = []
  
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
  
    img.putdata(newData)
    img.save(img_path_new, "PNG")
    print("Successful")

img_folder = 'MDM_Urun_Fotolari'
folders = os.listdir(img_folder)
for folder in folders:
    path = img_folder+'/'+folder
    files = os.listdir(path)
    if '.resizefile' in files or files == []:
        continue
    print(files)
    for file in files:
        if "High" in file:
            continue
        img_path = path+'/'+file
        img_path_new = img_path.replace('.jpeg','.png')
        img = Image.open(img_path)
        img_arr = np.asarray(img)
        
        convertImage()

        img = np.array(Image.open(img_path_new))
        idx = np.where(img[:, :, 3] > 0)
        x0, y0, x1, y1 = idx[1].min(), idx[0].min(), idx[1].max(), idx[0].max()
        out = Image.fromarray(img[y0:y1+1, x0:x1+1, :])

        out.save(img_path_new)
        
    f = open(path+"/.resizefile", "x")
    f.close()