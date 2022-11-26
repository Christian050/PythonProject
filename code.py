# import pandas as pd
# import pyqrcode
# import pandas
#
#
# def createQRCode():
#     df = pd.read_csv('studentdata.csv')
#     for index, values in df.iterrows():
#         name = values['Name']
#         age = values['ID']
#         course = values['Course']
#         data = f'''Name:{name}\n
#                     ID:{age}\n
#                         Course:{course}'''
#         image = pyqrcode.create(data)
#         image.svg(f"{name}_{age}.svg", scale='5')
#
#
# createQRCode()


# Qrcode to add data(weblink)
# import qrcode
#
# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
# )
# qr.add_data('www.openlabsghana.com')
# qr.make(fit=True)
# img = qr.make_image(fill_color='black', back_color='white')
# img.save("openlabs.png")

# Add Image
# QRCODE( Modules used qrcode and pillow)
# immport Modules
import qrcode
from PIL import Image
# Importing your desired image
"""logo_link = image name here


logo = Image.open(logo_link)
# taking base width
basewidth = 100

# Adjusting image size
wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])* float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
QRCode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)

# Generating QR cpde
QRCode.make()

# Applying your desired color
QRcolor = 'Blue'

# Adding color to QR Code
QRimg = QRCode.make_image(fill_color=QRcolor, back_color='White').convert('RGB')

# Set the size off the QR Code
pos = ((QRimg.size[0] - logo.size[0])) // 2, ((QRimg.size[1] - logo.size[1] // 2)
QRimg.save('Code_QR.png')

print('QR code generated!')"""