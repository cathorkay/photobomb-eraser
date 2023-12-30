#!/usr/bin/env python3

"""
Stanford CS106A Ghost Project
"""

import os
import sys

# This line imports SimpleImage for use here
# This depends on the Pillow package
from simpleimage import SimpleImage


def pix_dist2(pix1, pix2):
    """
    From two pix tuples,
    this function returns the squares of each color's distance between
    the respective other in the other tuple and outputs it as a list
    to be used in the function best_pix.
    >>> pix_dist2((23, 23, 23), (1,1,1))
    [484, 484, 484]
    >>> pix_dist2((255, 155, 55), (5,10,15))
    [62500, 21025, 1600]
    """
    diff = (abs(pix2[0] - pix1[0]), abs(pix2[1] - pix1[1]), abs(pix2[2] - pix1[2]))
    return list(map(lambda elem: elem * elem, diff))

def mean(pix):
    """
    Computes the average of all the numbers in a pix tuple.
    """
    result = 0.0
    if len(pix) >= 0:
        for num in pix:
            result += num
        result = result / len(pix)
    return result


def best_pix(pixs):
    """
    Given a list of 3 or more pix, returns the best pix.
    >>> best_pix([(1, 1, 1), (1, 1, 1), (28, 28, 28)])
    (1, 1, 1)
    >>> best_pix([(1, 2, 3), (4, 5, 6), (27, 28, 29)])
    (4, 5, 6)
    """
    ave_red = mean(list(map(lambda num: num[0], pixs)))
    ave_green = mean(list(map(lambda num: num[1], pixs)))
    ave_blue = mean(list(map(lambda num: num[2], pixs)))
    average = (ave_red, ave_green, ave_blue)
    # return average
    best = min(pixs, key=lambda pix: pix_dist2(pix, average))
    return best


def solve(images):
    """
    Given a list of image objects, compute and show
    a Ghost solution image based on these images.
    There will be at least 3 images and they will all be
    the same size.
    """

    d = {}
    for image in images:
        for y in range(image.height):
            for x in range(image.width):
                pix = image.get_pix(x, y)
                key = x,y
                if key not in d:
                    d[key] = []
                d[key].append(pix)
    for x,y in d:
        pixs = d[x,y]
        best = best_pix(pixs)
        d[x,y] = best
    output = SimpleImage.blank(image.width, image.height)
    for y in range(output.height):
        for x in range(output.width):
            pixel = output.get_pixel(x, y)
            ghost_red = d[x,y][0]
            ghost_green = d[x,y][1]
            ghost_blue = d[x,y][2]
            pixel.red = ghost_red
            pixel.green = ghost_green
            pixel.blue = ghost_blue
    return output.show()


def jpgs_in_dir(dir):
    """
    (provided)
    Given the name of a directory
    returns a list of the .jpg filenames within it.
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided)
    Given a directory name, reads all the .jpg files
    within it into memory and returns them in a list.
    Prints the filenames out as it goes.
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print(filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    if len(args) == 1:
        images = load_images(args[0])
        solve(images)


if __name__ == '__main__':
    main()
