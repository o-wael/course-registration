from University import University
import pytest  # type: ignore


def test_singleton():

    University.reset()
    university = University.getUniversity()
    university2 = University.getUniversity()
    assert university == university2
    assert university is university2
    university.__str__()

    with pytest.raises(Exception):
        University()
