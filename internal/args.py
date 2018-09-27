import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str, default=None, \
                        help="Name of input image with extension.")
    parser.add_argument("-o", "--output", type=str, default="output.jpg", \
                        help="Name of output file (Add extension).")
    parser.add_argument("-s", "--size", type=str, default="all", \
                        help="Size to image. Avalible options 700 and 1500.")

    args = parser.parse_args()

    return args
