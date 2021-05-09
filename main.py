import pathlib
import os
import shutil

from sklearn.model_selection import train_test_split

# source_path = '../baza (jpg+csv) wyciete'
# destination_path = '../baza (jpg+csv) podzielone'
source_path = '../baza (jpg+csv) - bmalo wyciete'
destination_path = '../baza (jpg+csv) - bmalo podzielone'
# train = 0.80
valid = 0.10
test = 0.10


def copy_img(images_names, dest_path):
    for file_name in images_names:
        if 'T' in file_name:
            shutil.copyfile(f"{source_path}/{file_name}", f"{dest_path}/True/{file_name}")
        else:
            shutil.copyfile(f"{source_path}/{file_name}", f"{dest_path}/False/{file_name}")


def divide_data():
    destination_path_train = f"{destination_path}/train"
    pathlib.Path(f'{destination_path_train}/True').mkdir(parents=True, exist_ok=True)
    pathlib.Path(f'{destination_path_train}/False').mkdir(parents=True, exist_ok=True)
    if valid > 0:
        destination_path_valid = f"{destination_path}/valid"
        pathlib.Path(f'{destination_path_valid}/True').mkdir(parents=True, exist_ok=True)
        pathlib.Path(f'{destination_path_valid}/False').mkdir(parents=True, exist_ok=True)
    if test > 0:
        destination_path_test = f"{destination_path}/test"
        pathlib.Path(f'{destination_path_test}/True').mkdir(parents=True, exist_ok=True)
        pathlib.Path(f'{destination_path_test}/False').mkdir(parents=True, exist_ok=True)

    images = os.listdir(source_path)
    image_train_numbers = [x for x in range(len(images))]

    if test > 0:
        image_train_numbers, image_test_numbers, _, _ = train_test_split(image_train_numbers, image_train_numbers, test_size=test)
        image_list = [images[idx] for idx in image_test_numbers]
        copy_img(image_list, destination_path_test)

    if valid > 0:
        image_train_numbers, image_valid_numbers, _, _ = train_test_split(image_train_numbers, image_train_numbers, test_size=valid)
        image_list = [images[idx] for idx in image_valid_numbers]
        copy_img(image_list, destination_path_valid)

    image_list = [images[idx] for idx in image_train_numbers]
    copy_img(image_list, destination_path_train)


if __name__ == '__main__':
    divide_data()
