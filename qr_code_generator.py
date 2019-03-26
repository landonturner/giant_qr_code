#!/usr/bin/env python3

from fpdf import FPDF
from glob import glob
import image_slicer
import qrcode
import sys
import argparse
import os

def parse_args():
    parser = argparse.ArgumentParser(
        description='Create a poster sized QR Code printable on 8.5x11 paper')

    parser.add_argument('-w', '--width', type=int, action='store', nargs='?', default=3,
                        help='width in pieces of 8.5x11 paper (.75in margins)')
    parser.add_argument('-c', '--clean', action='store_true',
                        help='delete intermediate images. only keep pdf')
    parser.add_argument('text', type=str, help='text to be encoded in qr code')

    return parser.parse_args()

def create_qr_code(text, filename):
    """ Create qr code instance that encodes the text and saves it to filename """
    qr = qrcode.QRCode(
            box_size = 200,
            border = 0,
    )

    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image()
    img.save(filename)

if __name__ == '__main__':
    args = parse_args()

    create_qr_code(args.text, 'full.png')

    # slices image and pulls filenames
    image_slicer.slice('full.png', args.width * args.width)
    image_names = glob('full_*.png')
    image_names.sort()

    if len(image_names) > args.width * args.width:
        print('ERROR - unknown files detected')
        print(image_names)
        sys.exit(1)

    # create the pdf and insert each images as a new page
    pdf = FPDF('P', 'in', 'Letter')
    for file in image_names:
        pdf.add_page()
        pdf.image(file, 0.75, 0.75, 7, 7)
        pdf.set_font('Arial', 'B', 16)
        pdf.text(x=0.75, y=9, txt=file)
    pdf.output("full.pdf", "F")

    # deletes intermediate images
    if args.clean:
        os.remove('full.png')
        for file in image_names:
            os.remove(file)

