from mlproject.lib import hello_world
from mlproject.distance import haversine

def test_length_of_hello_world():
    assert len(hello_world()) != 0

def test_haversine():
    assert haversine(2.380009, 48.865070, 52.5069531,
                     13.3903589) == 6028.898130516999
