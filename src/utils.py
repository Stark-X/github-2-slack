import hashlib
import hmac
from typing import Union


def get_signature(secret: Union[str, bytes], payload: Union[str, bytes]) -> bytes:
    key = bytes(secret, "utf-8") if type(secret) == str else secret
    msg = bytes(payload, "utf-8") if type(payload) == str else payload
    digester = hmac.new(key=key, msg=msg, digestmod=hashlib.sha256)
    signature = digester.hexdigest()
    return bytes(signature, "utf-8")


def verify_signature(src: Union[str, bytes], dest: Union[str, bytes]) -> bool:
    return hmac.compare_digest(bytes(src, "utf-8") if type(src) is str else src,
                               bytes(dest, "utf-8") if type(dest) is str else dest)
