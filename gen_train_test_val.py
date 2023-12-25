import os
import shutil
from random import shuffle

def split_data(input_folder, output_folder, train_ratio=0.7, val_ratio=0.15, test_ratio=0.15):
    # Ensure the output folders exist, if not, create them
    train_folder = os.path.join(output_folder, 'train', 'images')
    val_folder = os.path.join(output_folder, 'val', 'images')
    test_folder = os.path.join(output_folder, 'test', 'images')

    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(val_folder, exist_ok=True)
    os.makedirs(test_folder, exist_ok=True)

    # Get a list of all image files in the input folder
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp','.json'))]
    shuffle(image_files)

    # Calculate the number of images for each split
    total_images = len(image_files)
    num_train = int(total_images * train_ratio)
    num_val = int(total_images * val_ratio)

    # Copy images to the train folder
    for image_file in image_files[:num_train]:
        source_path = os.path.join(input_folder, image_file)
        dest_path = os.path.join(train_folder, image_file)
        shutil.copyfile(source_path, dest_path)

    # Copy images to the val folder
    for image_file in image_files[num_train:num_train + num_val]:
        source_path = os.path.join(input_folder, image_file)
        dest_path = os.path.join(val_folder, image_file)
        shutil.copyfile(source_path, dest_path)

    # Copy images to the test folder
    for image_file in image_files[num_train + num_val:]:
        source_path = os.path.join(input_folder, image_file)
        dest_path = os.path.join(test_folder, image_file)
        shutil.copyfile(source_path, dest_path)

if __name__ == "__main__":
    input_folder = "images"  # Replace with the actual path to Folder A
    output_folder = "data/"  # Replace with the desired output path

    # Specify the ratio for train, validation, and test
    train_ratio = 0.7
    val_ratio = 0.1
    test_ratio = 0.2

    split_data(input_folder, output_folder, train_ratio, val_ratio, test_ratio)
