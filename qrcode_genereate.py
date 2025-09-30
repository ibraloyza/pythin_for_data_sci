import qrcode; 
import image;
qr = qrcode.QRCode(
    version=15,
    box_size=10,
    border=5,

)
data = "+252 618 363 523";
qr.add_data(data);
qr.make(fit=True);
image = qr.make_image(fill= "black", black_color="white");
image.save("phone.png");