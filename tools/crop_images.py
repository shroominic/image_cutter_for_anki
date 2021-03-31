from PIL import Image
import os, numpy as np

def get_images(image_folder_path):
    image_path_list = os.listdir(image_folder_path)
    image_path_list.sort()
    image_list = []

    for path in image_path_list:
        if '.jpg' in path:
            image_list.append(Image.open(f'./{image_folder_path}/{path}'))

    return image_list

def crop_index_up(image):
    image_array = np.array(image)
    index = 0
    for width, i in zip(image_array, range(0, image_array.size-1)):
        if index != 0:
            break
        for pixel in width:
            if pixel.mean() < 250:
                if i > 15:
                    i -= 15
                index = i
                break
    return index

def crop_index_down(image):
    image_array = np.array(image)
    index = 0
    for width, i in zip(reversed(image_array), range(0, image_array.size-1)):
        if index != 0:
            break
        for pixel in width:
            if pixel.mean() < 250:
                if i > 15:
                    i -= 15
                index = image_array.shape[0] - i
                break
    return index

def crop_index_left(image):
    image_array = np.array(image).swapaxes(1, 0)
    index = 0
    for width, i in zip(image_array, range(0, image_array[0].size-1)):
        if index != 0:
            break
        for pixel in width:
            if pixel.mean() < 250:
                if i > 15:
                    i -= 15
                index = i
                break
    return index

def crop_index_right(image):
    image_array = np.array(image).swapaxes(0, 1)
    index = 0
    for width, i in zip(reversed(image_array), range(0, image_array[0].size-1)):
        if index != 0:
            break
        for pixel in width:
            if pixel.mean() < 250:
                if i > 15:
                    i -= 15
                index = image_array.shape[0] - i
                break
    return index

def crop(image):
    image_path = image.filename
    index_up = crop_index_up(image)
    index_down = crop_index_down(image)
    index_left = crop_index_left(image)
    index_right = crop_index_right(image)
    image_array = np.array(image)[index_up:index_down, index_left:index_right, :]
    try:
        output_image = Image.fromarray(image_array)
    except:
        output_image = image
        print(f'Error: {image.filename}')
    output_image.save(image_path)
    print(f'{index_up}_{index_down}_{index_left}_{index_right}_{image.size}')

def crop_images(path):
    image_list = get_images(path)
    for image in image_list:
        crop(image)


path = 'result'
crop_images(path)