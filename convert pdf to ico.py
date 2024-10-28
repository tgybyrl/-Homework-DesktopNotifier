from PIL import Image
filename = 'home.png'
img = Image.open(filename)
img.save('home.ico')