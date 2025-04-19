with open('file.wav', 'wb') as f:
    with open('file', 'rb') as ff:
        f.write(ff.read())
