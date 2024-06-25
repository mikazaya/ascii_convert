import PIL.Image


# chars = ["@", "J", "D", "%", "*", "P", "+", "Y", "$", ",", "."]
chars='$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,"^`\'.'

def _convert(im:PIL.Image)->str:

     
    im=im.convert('L')
    width,height=im.size
    aspect_ratio=height/width
    new_width=120
    new_height=aspect_ratio*new_width*0.55
    im=im.resize((new_width,int(new_height)))
    
     
    pixels=im.getdata()
    new_pixels=[chars[px//25] for px in pixels]
    new_pixels=''.join(new_pixels)
    new_pixels_count=len(new_pixels)
    ascii_image=[new_pixels[index:index+new_width] for index in range(0,new_pixels_count,new_width)]
    ascii_image="\n".join(ascii_image)
    with open("ascii_image.txt","w") as f:
        f.write(ascii_image)     
     
    return ascii_image

def convert(path:str)->str:
    im=None
    try:
        im = PIL.Image.open(path)
    except Exception as e :
        print("Unable to open image",path,e)
    if im:
        return _convert(im)
     

res=convert("images/mn.webp")