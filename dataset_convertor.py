import os 
import json
import yaml

from_labelStudio_dir = 'yolo_json' # path of exported yolo dataset from label-studio
to_dataset_name = 'custom2'        # only name of dataset (not path) program will create all things for you 

# creating yolo dataset formate
os.makedirs(f'datasets/{to_dataset_name}/images/train', exist_ok=True)
os.makedirs(f'datasets/{to_dataset_name}/images/val', exist_ok=True)

os.makedirs(f'datasets/{to_dataset_name}/labels/train', exist_ok=True)
os.makedirs(f'datasets/{to_dataset_name}/labels/val', exist_ok=True)


# transfer from label-studio yolo to real yolo dataset format
images_list = os.listdir(f'{from_labelStudio_dir}/images')
images_list_len = len(images_list)


train = images_list[:round(images_list_len * 0.8)]
val = images_list[len(train):]

for img in train:
    os.rename(f'{from_labelStudio_dir}/images/{img}', f'datasets/{to_dataset_name}/images/train/{img}')
    name = img.split('.')[0]
    os.rename(f'{from_labelStudio_dir}/labels/{name}.txt', f'datasets/{to_dataset_name}/labels/train/{name}.txt')

for img in val:
    os.rename(f'{from_labelStudio_dir}/images/{img}', f'datasets/{to_dataset_name}/images/val/{img}')
    name = img.split('.')[0]
    os.rename(f'{from_labelStudio_dir}/labels/{name}.txt', f'datasets/{to_dataset_name}/labels/val/{name}.txt')



# creation of dataset yaml file
with open(f'{from_labelStudio_dir}/notes.json', 'r') as f:
    data = json.load(f)
    class_id_names = {id_name['id']: id_name['name'] for id_name in data['categories']}

yaml_dict = {
    'path': f'./{to_dataset_name}',
    'train': 'images/train',
    'val': 'images/val',
    'names': class_id_names

}

with open('dtst.yml', 'w') as f:
    yaml.dump(yaml_dict, f)
