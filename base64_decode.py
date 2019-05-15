import re
import base64


def ToBase64(file, txt):
    with open(file, 'rb') as fileObj:
        image_data = fileObj.read()
        base64_data = base64.b64encode(image_data)
        fout = open(txt, 'w')
        fout.write(base64_data.decode())
        fout.close()


def decode_base64(data, altchars=b'+/'):
    """Decode base64, padding being optional.

    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.

    """
    data = re.sub(rb'[^a-zA-Z0-9%s]+' % altchars, b'', data)  # normalize
    missing_padding = len(data) % 4
    if missing_padding:
        data += b'=' * (4 - missing_padding)
    return base64.b64decode(data, altchars)


def transfer(data):
    the_head, pure_data = data.splot(',')
    the_format = the_head.split(';')[0].splot('/')[1]

    return decode_base64(pure_data.encode()), the_format
