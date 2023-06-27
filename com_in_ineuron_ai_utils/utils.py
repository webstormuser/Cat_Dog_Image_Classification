import base64

def decodeImage(uploaded_file, filename):
    imgdata = base64.b64decode(uploaded_file)
    with open(filename, 'wb') as f:
        f.write(imgdata)

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())