
from PIL import Image
from argparse import ArgumentParser
from glob import glob
import os

parser = ArgumentParser(description="Convert colored images to black and white")
parser.add_argument("--input", help="File with photos", required=True)
parser.add_argument("--output", help="File with photos black and white", required=True)

args = parser.parse_args()

search_path =args.input + "/*"
photos_list = glob(search_path)

for photo in photos_list:
    print("Processing", photo)
    img = Image.open(photo)
    bw_img = img.convert("L")
    filename = os.path.basename(photo)
    save_path = args.output + "/" + filename
    bw_img.save(save_path)
