import numpy as np
from cbc_scanner.processing.focus_score import focus_score

def test_focus_score():
    img = np.random.randint(0, 255, (100, 100), dtype=np.uint8)
    score = focus_score(img)
    assert score > 0
