import json
import falcon
import qrcode
from io import BytesIO

def create_qr(data=""):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=7,
        border=1,
    )

    qr.add_data(data)
    qr.make(fit=True)
    return qr.make_image(fill_color="black", back_color="white")

class QRCode:
    def on_get(self, req, res):
        if req.get_param('data'):
            img = create_qr(req.get_param('data'))

            io = BytesIO()
            img.save(io, "PNG")
            io.seek(0)

            res.content_type = "image/png"
            res.stream = io
        else:
            res.media = {"error": "data field missing" }

app = falcon.API()
app.add_route('/', QRCode())
