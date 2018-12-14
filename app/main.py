import json
import falcon
import qrcode
from io import BytesIO

def create_qr():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=7,
        border=1,
    )
    return qr

class QRCode:
    def on_get(self, req, res):
        if req.get_param('data'):
            qr = create_qr()
            qr.add_data(req.get_param('data'))
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")

            io = BytesIO()
            img.save(io, "PNG")
            io.seek(0)

            res.content_type = "image/png"
            res.stream = io
        else:
            res.media = {"error": "data field missing" }

app = falcon.API()
app.add_route('/', QRCode())
