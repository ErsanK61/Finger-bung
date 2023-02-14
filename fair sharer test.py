import numpy as np
from fairsharer import fair_sharer

def test_fair_sharer():
    assert np.allclose(fair_sharer([0, 1000, 800, 0], 1), [100, 800, 900, 0])
    assert np.allclose(fair_sharer([0, 1000, 800, 0], 2) ,[100, 890, 720, 90])
