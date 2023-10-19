from PIL import Image

for num in range(256):
    im = Image.new(mode="L", size=(10,10), color=num)
    im.save(f'../images/pixels/{num}.png')
    im.close()
