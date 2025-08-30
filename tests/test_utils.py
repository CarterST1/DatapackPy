import pytest
from modules.utils import LEGAL_CHARS, PACK_VERSIONS, convertFromResourceLocation, getPackFormatRange, isLegalChar, isValidToConvert, formatWithNamespace

def test_isLegalChar():
    for char in LEGAL_CHARS:
        assert isLegalChar(char)

    assert isLegalChar('A') == False

def test_isValidToConvert():
    location = 'minecraft:empty'
    assert isValidToConvert(location)
    assert isValidToConvert(location.upper()) == False

def test_formatWithNamespace():
    namespace = 'minecraft'
    path = 'diamond'
    assert formatWithNamespace(namespace, path)
    assert formatWithNamespace(namespace.upper(), path) == (False, '')
    assert formatWithNamespace(namespace, path.upper()) == (False, '')

def test_convertFromResourceLocation():
    assert convertFromResourceLocation('minecraft:empty') == (True, 'minecraft', 'empty')
    assert convertFromResourceLocation(':empty') == (True, 'minecraft', 'empty')
    assert convertFromResourceLocation('minecraft::empty') == (False, '', '')

def test_getPackFormatRange():
    assert getPackFormatRange(85) == ((1, 21, 9), (1, 21, 9))
    assert getPackFormatRange(99) == None