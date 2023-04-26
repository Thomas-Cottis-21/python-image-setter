import os

# Get the current directory
current_dir = os.getcwd()

# Set the root folder to Product_images
root_folder = "Product_images"

# Loop through each folder in the Product_images folder
for folder in os.listdir(os.path.join(current_dir, root_folder)):
    folder_path = os.path.join(current_dir, root_folder, folder)
    if os.path.isdir(folder_path):
        # Loop through each file in the folder
        file_count = 1
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            new_filename = str(file_count) + os.path.splitext(filename)[1]
            new_file_path = os.path.join(folder_path, new_filename)
            os.rename(file_path, new_file_path)
            file_count += 1
