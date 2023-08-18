from PIL import Image
import os

def remove_exif(image_path, output_path):
    try:
        img = Image.open(image_path)
        data = list(img.getdata())
        img_without_exif = Image.new(img.mode, img.size)
        img_without_exif.putdata(data)
        img_without_exif.save(output_path)
        print(f"EXIF data removed from {image_path} successfully.")
    except Exception as e:
        print(f"An error occurred while processing {image_path}: {e}")

if __name__ == "__main__":
    input_folder = input("Enter the path of the folder containing the input images: ")
    output_folder = input("Enter the path of the output folder: ")

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            input_image_path = os.path.join(input_folder, filename)
            output_image_path = os.path.join(output_folder, filename)
            remove_exif(input_image_path, output_image_path)