import qr_generator

data = input("Enter the text or URL: ").strip()
filename = input("Enter the filename: ").strip()
qr = qr_generator.QRCode(box_size=10, border=5)
qr.add_data(data)
image = qr.make_image(fill_color='black', back_color='white')
image.save(filename)
print(f"QR code saved as {filename}")