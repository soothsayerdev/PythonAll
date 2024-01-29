from collections import namedtuple
from typing import List

Box = namedtuple('Box', 'have_key')

if __name__ == "__main__":
    boxes: List[Box] = [
        Box(False), Box(False), Box(False),
        Box(False), Box(False), Box(False),
        Box(False), Box(True), Box(False),
    ]

    print(boxes)