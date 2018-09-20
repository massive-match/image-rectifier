import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str, default=None, \
                        help="Name of input image with extension.")
    parser.add_argument("-o", "--output", type=str, default="output.jpg", \
                        help="Name of output file (Add extension).")

    args = parser.parse_args()

    return args
