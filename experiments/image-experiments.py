from PIL import Image

#def combine_rows(ima, imb, imc):
#    

def double_dist(ab_tup):
    a = ab_tup[0]
    b = ab_tup[1]
    dist = a - b
    dist = int(dist / 2)
    a = a + dist
    b = b - dist
    return (a,b)

def rgba_arith_mean(a, b):
    return (
            (a[0] + b[0]) / 2,
            (a[1] + b[1]) / 2,
            (a[2] + b[2]) / 2,
            (a[3] + b[3]) / 2
            )

def rgba_max(a,b):
    return (
            max(a[0],b[0]),
            max(a[1],b[1]),
            max(a[2],b[2]),
            max(a[3],b[3])
            )

def rgba_min(a,b):
    return (
            min(a[0],b[0]),
            min(a[1],b[1]),
            min(a[2],b[2]),
            min(a[3],b[3])
            )

def rgb_arith_mean(a, b):
    ret = (
            int((a[0] + b[0]) / 2),
            int((a[1] + b[1]) / 2),
            int((a[2] + b[2]) / 2),
            )
    gray = int((ret[0] + ret[1] + ret[2]) / 3)
    ret = (
        double_dist((ret[0], gray))[0],
        double_dist((ret[1], gray))[0],
        double_dist((ret[2], gray))[0],
    )
    return ret

def rgb_max(a,b):
    return (
            max(a[0],b[0]),
            max(a[1],b[1]),
            max(a[2],b[2]),
            )

def rgb_min(a,b):
    return (
            min(a[0],b[0]),
            min(a[1],b[1]),
            min(a[2],b[2]),
            )




def combine_images(ima, imb, xform_func):
    width = max(ima.width, imb.width)
    height = max(ima.height, imb.height)
    imc = Image.new('RGBA',(width,height))
    ima = ima.resize((width, height))
    imb = imb.resize((width,height))
    for y in range(height):
        for x in range(width):
            imc.putpixel((x,y), xform_func(
                ima.getpixel((x,y)),
                imb.getpixel((x,y))
                ))
    imc.save('out.png')

def shrink_num(n, factor):
    return (n // factor) * factor

def shrink_pixel(pixel, factor):
    return (
            shrink_num(pixel[0], factor),
            shrink_num(pixel[1], factor),
            shrink_num(pixel[2], factor),
            )

def reduce_color_space(im, factor):
    imc = Image.new('RGBA', (im.width,im.height))
    for y in range(im.height):
        for x in range(im.width):
            imc.putpixel((x,y),
                shrink_pixel(im.getpixel((x,y)), factor)
            )
    imc.save('reduced.png')

#def transform_image_a(im):
#    #for y in range()

def main():
    ima = Image.open('pica.jpg')
    #imb = Image.open('picb.jpg')
    reduce_color_space(ima, 64)
    #combine_images(ima,imb, rgb_arith_mean)
    






main()
