from PIL import Image
import numpy as np
import json
import os

digit_dict = {}
for digit_dir in os.listdir('../images/mnist_png/'):
    if not os.path.isdir(f'../images/mnist_png/{digit_dir}/'):
        continue
    print(digit_dir)
    digit_dict[digit_dir] = []
    for img_path in os.listdir(f'../images/mnist_png/{digit_dir}/'):
        img_num = int(img_path.strip('.png'))
        digit_dict[digit_dir].append(img_num)
        img = Image.open(f'../images/mnist_png/{digit_dir}/{img_path}')
        pixels = np.array(img).flatten().tolist()
        img.close()
        with open(f'../js/mnist/{img_num}.js', 'w') as f:
            f.write(f'var pixel_data = {pixels};')
    print(len(digit_dict[digit_dir]))
with open(f'../js/file_map.js', 'w') as f:
    f.write(f'const map = {json.dumps(digit_dict)};');
    
        
        
