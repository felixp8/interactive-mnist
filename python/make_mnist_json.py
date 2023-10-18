from PIL import Image
import numpy as np
import json
import os

digit_dict = {}
for digit_dir in os.listdir('../data/mnist_png/'):
    if not os.path.isdir(f'../data/mnist_png/{digit_dir}/'):
        continue
    print(digit_dir)
    digit_dict[digit_dir] = []
    for img_path in os.listdir(f'../data/mnist_png/{digit_dir}/'):
        img_num = int(img_path.strip('.png'))
        digit_dict[digit_dir].append(img_num)
        img = Image.open(f'../data/mnist_png/{digit_dir}/{img_path}')
        pixels = np.array(img).flatten().tolist()
        img.close()
        with open(f'../data/mnist_json/{img_num}.json', 'w') as f:
            json.dump(pixels, f)
    print(len(digit_dict[digit_dir]))
with open(f'../data/file_map.json', 'w') as f:
    json.dump(digit_dict, f)
    
        
        
