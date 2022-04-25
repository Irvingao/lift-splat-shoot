import cv2
import os 
from tqdm import tqdm

    
viz_path = "lidar_dir"
# viz_path = "viz_dir"
save_dir = "./"

def sort(viz_path):
    folder_dir = viz_path.split("/")[-1]
    folder_name = folder_dir.split("_")[0]
    viz_list = os.listdir(viz_path)
    
    sort_list = [None for i in range(len(viz_list))]
    # sort rank
    for name_dir in viz_list:
        print(name_dir)
        name = name_dir.split('.')[0]
        name = name.split(folder_name)[-1]
        img_id = int(name.split("_")[0])
        sort_list[img_id] = name_dir

    return sort_list
    

if __name__ == '__main__':
    is_init = False
    viz_list = sort(viz_path)
    for img_dir in tqdm(viz_list):
        img = cv2.imread(os.path.join(viz_path, img_dir))
        if not is_init:
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            out = cv2.VideoWriter(os.path.join(save_dir, 'output2.avi'),fourcc, 3.0, (img.shape[1],img.shape[0]))
            is_init = True
        out.write(img)
    out.release()