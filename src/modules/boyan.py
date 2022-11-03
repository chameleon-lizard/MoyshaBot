from lzma import CHECK_ID_MAX
from tabnanny import check
from typing import List

from pathlib import Path
from PIL import Image

import imagehash

class Boyan:
    def __init__(self, path: str) -> None:
        '''
        Path is path to hash db.
        '''
        self._hashpath = path
        try:
            self._hashes = Path(path).read_text().split()
        except:
            self._hashes = []
            Path(path).write_text("")

    def add_image(self, path: str) -> None:
        hash = imagehash.average_hash(Image.open(path))
        self._hashes.append(str(hash))
        Path(self._hashpath).write_text(" ".join(self._hashes))

    def check_image(self, path: str) -> bool:
        return self._hashes.count(str(imagehash.average_hash(Image.open(path))))

    def check_image_by_hash(self, hash: imagehash.ImageHash) -> bool:
        if str(hash) in self._hashes:
            return False
        else:
            return True