import os 

from_labelStudio_dir = 'yolo_json'
to_dataset_dir = 'custom2'


os.makedirs(f'datasets/{to_dataset_dir}/images/train', exist_ok=True)
os.makedirs(f'datasets/{to_dataset_dir}/images/val', exist_ok=True)

os.makedirs(f'datasets/{to_dataset_dir}/labels/train', exist_ok=True)
os.makedirs(f'datasets/{to_dataset_dir}/labels/val', exist_ok=True)


# first logic
images_list = os.listdir(f'{from_labelStudio_dir}/images')
images_list_len = len(images_list)


train = images_list[:round(images_list_len * 0.8)]
val = images_list[len(train):]

for img in train:
    os.rename(f'{from_labelStudio_dir}/images/{img}', f'datasets/{to_dataset_dir}/images/train/{img}')
    name = img.split('.')[0]
    os.rename(f'{from_labelStudio_dir}/labels/{name}.txt', f'datasets/{to_dataset_dir}/labels/train/{name}.txt')

for img in val:
    os.rename(f'{from_labelStudio_dir}/images/{img}', f'datasets/{to_dataset_dir}/images/val/{img}')
    name = img.split('.')[0]
    os.rename(f'{from_labelStudio_dir}/labels/{name}.txt', f'datasets/{to_dataset_dir}/labels/val/{name}.txt')



