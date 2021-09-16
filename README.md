# C19Verifier
This program allows you to verify the data inside the green pass for covid 19.  The QR-Code was used as an example to test the program.  

Source QR-Code: https://io.italia.it/certificato-verde-green-pass-covid/

The program in PYTHON 3 requires the following libraries:
  
  sys
  zlib
  pprint
  PIL.image
  PIL                 (Image, UnidentifiedImageError)
  pyzbar.pyzbar
  base45
  cbor2
  qrcode
  json
  datetime            (datetime)



Usage: 
  python3 C19Verifier.py img.x
  
  Sono ammesse tutte le estensioni supportate da PIL
