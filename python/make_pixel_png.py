from PIL import Image

for num in range(256):
    im = Image.new(mode="L", size=(10,10), color=num)
    im.save(f'../data/pixels/{num:03d}.png')
    im.close()
