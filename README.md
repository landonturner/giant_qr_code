# Giant QR Code Generator

## Purpose

This code creates a qr code and split it up across many pages suitable for
printing. Running this will create a pdf containing each page of the qr code.
Optionally it will create each resulting image in as its own png image as well
as a png of the QR code as a whole.

## Setup

#### Using a python virtual environment

```
python3 -m virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Runing

```
usage: qr_code_generator.py [-h] [-w [WIDTH]] [-c] text

Create a poster sized QR Code

positional arguments:
  text                  text to be encoded in qr code

optional arguments:
  -h, --help            show this help message and exit
  -w [WIDTH], --width [WIDTH]
                        width in pieces of 8.5x11 paper (.75in margins)
  -c, --clean           delete intermediate images. only keep pdf
```

