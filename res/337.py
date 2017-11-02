from PIL import Image

def is_red(pixel):
    return (pixel[0] == 255) and \
            (pixel[1] == 0) and \
            (pixel[2] == 0)

def rotate_row(im, y):
    x_coord = 0
    row_end = 0
    row = []
    while not is_red(im.getpixel((x_coord,y))):
        x_coord = (x_coord + 1) % im.width
    while is_red(im.getpixel((x_coord,y))):
        row_end = x_coord
        x_coord = (x_coord + 1) % im.width
    while x_coord != row_end:
        row.append(im.getpixel((x_coord,y)))
        x_coord = (x_coord + 1) % im.width
    row.append(im.getpixel((x_coord,y)))
    x_coord = 0
    for i in row:
        im.putpixel((x_coord,y), i)
        x_coord += 1
    return row

def unscramble_image(im):
    for i in range(im.width):
        rotate_row(im, i)
    im.save(im.filename.split('.')[0] + "-unscrambled" + '.' + im.format)

def main():
    filename = input('File to unscramble: ')
    im = Image.open(filename)
    unscramble_image(im)

main()

