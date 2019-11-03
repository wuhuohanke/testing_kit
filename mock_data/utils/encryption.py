import hashlib


# md5转码
def md5(before_convert):
    converted_data = hashlib.md5(before_convert.encode(encoding='utf-8')).hexdigest()
    return converted_data
