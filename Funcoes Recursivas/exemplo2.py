from collections import namedtuple
from typing import List

Box = namedtuple('Box', 'have_key')

def find_key(boxes: List[Box], index: int = 0) -> Box:
    # Caso base
    if len(boxes) <= index:
        return Box(False)
    
    box = boxes[index]

    # Caso Base
    if box.have_key:
        return box
    
    # Caso Recursivo
    index += 1
    return find_key(boxes, index) 


if __name__ == "__main__":
    boxes: List[Box] = [
        Box(False), Box(False), Box(False),
        Box(False), Box(False), Box(False),
        Box(False), Box(True), Box(False),
    ]

    print(boxes)