from PIL import Image

def x_image(windows,mac):
    try:
        x_image = Image.open(windows)
    except:
        x_image = Image.open(mac)
    return x_image