from PIL import Image

def x_image(a):
    try:
        x_image = Image.open(a)
    except:
        try:
            x_image = Image.open(a.replace("\\","/"))
        except:
            x_image = Image.open(a.replace("/","\\"))
    
    return x_image