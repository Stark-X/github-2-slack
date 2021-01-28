import hashlib
import hmac
from typing import Union


def get_signature(secret: str, payload: str) -> bytes:
    key = bytes(secret, 'utf-8')
    msg = bytes(payload, "utf-8")
    digester = hmac.new(key=key, msg=msg, digestmod=hashlib.sha256)
    signature = digester.hexdigest()
    return bytes(signature, "utf-8")


def verify_signature(src: Union[str, bytes], dest: Union[str, bytes]) -> bool:
    return hmac.compare_digest(bytes(src, "utf-8") if type(src) is str else src,
                               bytes(dest, "utf-8") if type(dest) is str else dest)
