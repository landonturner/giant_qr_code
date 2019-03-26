#!/usr/bin/env python3

import qrcode
import image_slicer

from fpdf import FPDF

if __name__ == '__main__':
    url = 'https://leaveanote.io/oldtownbrown'

    # Create qr code instance
    qr = qrcode.QRCode(
            box_size = 200,
            border = 0,
    )

    # Add data
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image()

    img.save('full.png')

    image_slicer.slice('full.png', 9)

    image_names = [
        './full_01_01.png',
        './full_01_02.png',
        './full_01_03.png',
        './full_02_01.png',
        './full_02_02.png',
        './full_02_03.png',
        './full_03_01.png',
        './full_03_02.png',
        './full_03_03.png',
    ]

    pdf = FPDF('P', 'in', 'Letter')
    # imagelist is the list with all image filenames
    for image in image_names:
        pdf.add_page()
        pdf.image(image, 0.75, 0.75, 7, 7)
        pdf.set_font('Arial', 'B', 16)
        pdf.text(x=0.75, y=9, txt=image)
    pdf.output("full.pdf", "F")

