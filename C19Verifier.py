import sys
import zlib
import pprint
import PIL.Image
import pyzbar.pyzbar
import base45
import cbor2
import qrcode
from PIL import Image, UnidentifiedImageError
import json
from datetime import datetime

try:
    data = pyzbar.pyzbar.decode(PIL.Image.open(sys.argv[1]))

    print("\n\nQR Code to scan: " + sys.argv[1])

    cert = data[0].data.decode()
    print("\nQR Text: \n\n" + str(cert))

    b45data = cert.replace("HC1:", "")
    print("\n\nBase 45 data: \n\n" + str(b45data))

    zlibdata = base45.b45decode(b45data)
    print("\n\nZlibdata: \n\n" + str(zlibdata))

    cbordata = zlib.decompress(zlibdata)
    print("\n\nCbordata: \n\n" + str(cbordata))

    decoded = cbor2.loads(cbordata)
    print("\n\n\n\n\n\nDecoded: \n\n" + str(decoded))

    dataN = cbor2.loads(decoded.value[2])

    print("\n\n\n\n\nScan result: \n\n\n\n" + json.dumps(dataN, indent=4))

    print("""\n\n\n Meaning of the result: \n
    
    QR Code Issuer : """ + str(dataN[1]) + """
    QR Code Expiry : """ + str(datetime.fromtimestamp(dataN[4])) + """
    QR Code Generated : """ + str(datetime.fromtimestamp(dataN[6])) + """
        Vaccination Group
            Dose Number : """ + str(dataN[-260][1]['v'][0]['dn']) + """
            Marketing Authorization Holder : """ + str(dataN[-260][1]['v'][0]['ma']) + """
            Vaccine or prophylaxis : """ + str(dataN[-260][1]['v'][0]['vp']) + """
            ISO8601 complete date: Date of Vaccination : """ + str(dataN[-260][1]['v'][0]['dt']) + """
            Country of Vaccination : """ + str(dataN[-260][1]['v'][0]['co']) + """
            Unique Certificate Identifier: UVCI : """ + str(dataN[-260][1]['v'][0]['ci']) + """
            Vaccine medicinal product : """ + str(dataN[-260][1]['v'][0]['mp']) + """
            Certificate Issuer : """ + str(dataN[-260][1]['v'][0]['is']) + """
            Total Series of Doses : """ + str(dataN[-260][1]['v'][0]['sd']) + """
            Disease or agent targeted : """ + str(dataN[-260][1]['v'][0]['tg']) + """
        Surname(s), forename(s)
            Standardised surname : """ + str(dataN[-260][1]['nam']['fnt']) + """
            Surname : """ + str(dataN[-260][1]['nam']['fn']) + """
            Standardised forename : """ + str(dataN[-260][1]['nam']['gnt']) + """
            Forename : """ + str(dataN[-260][1]['nam']['gn']) + """
        Schema version : """ + str(dataN[-260][1]['ver']) + """
        Date of birth : """ + str(dataN[-260][1]['dob']) + """
    
     """)

except IndexError:
    print("\n\n Use this syntax: python3 C19Verifier.py <QRimage.png/jpg..> \n")
except FileNotFoundError:
    print("\n\n Image not found \n")
except UnidentifiedImageError:
    print("\n\n It is not an image \n")