"""Module providing Fucnction zip image file"""
from PIL import Image


def zippic(pic: str, targetfile: str, quality: int):
    """Function zip image file simply"""
    img = Image.open(pic)
    img = img.convert("RGB")
    img.save(targetfile, quality=quality)
