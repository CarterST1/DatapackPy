import pytest

from datapackpy.internal.game_version import GameVersion

def test_default_construction():
    version = GameVersion()
    assert (version.major, version.minor, version.patch) == (1, 21, 8)

def test_from_tuple_full():
    v = GameVersion.fromTuple((1, 19, 1))
    assert (v.major, v.minor, v.patch) == (1, 19, 1)

def test_from_tuple_missing_patch():
    v = GameVersion.fromTuple((1, 19))
    assert (v.major, v.minor, v.patch) == (1, 19, 0)

def test_equality_with_gameversion():
    v1 = GameVersion.fromTuple((1, 19, 2))
    v2 = GameVersion.fromTuple((1, 19, 2))
    assert v1 == v2
    assert not (v1 != v2)

def test_equality_with_tuple():
    v = GameVersion.fromTuple((1, 19, 2))
    assert v == (1, 19, 2)
    assert (1, 19, 2) == v
    assert not (v != (1, 19, 2))

def test_inequality_with_tuple_missing_patch():
    v = GameVersion.fromTuple((1, 19, 2))
    assert v != (1, 19)   # (1, 19, 0)
    assert (1, 19) != v

def test_ordering_with_gameversion():
    v1 = GameVersion.fromTuple((1, 19, 2))
    v2 = GameVersion.fromTuple((1, 20, 0))
    assert v1 < v2
    assert v2 > v1
    assert not (v1 > v2)
    assert not (v2 < v1)

def test_ordering_with_tuple():
    v = GameVersion.fromTuple((1, 19, 2))
    assert v < (1, 21, 0)
    assert (1, 21) > v
    assert (1, 19, 1) < v

def test_comparison_with_invalid_type():
    v = GameVersion.fromTuple((1, 19, 2))
    assert v != int()  # equality should return False
    with pytest.raises(TypeError):
        _ = v < "1.19.2"  # ordering against bad type

def test_str_and_repr():
    v = GameVersion.fromTuple((1, 19, 2))
    assert str(v) == "v1.19.2"
    assert repr(v) == "v1.19.2"
