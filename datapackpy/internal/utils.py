"""Contains utilities used by the datapack system"""
from typing import TypeAlias
from datapackpy.internal.game_version import GameVersion

Version: TypeAlias = GameVersion | tuple[int, int, int] | tuple[int, int]

LEGAL_CHARS = '0123456789abcdefghijklmnopqrstuvwxyz_.'

def isLegalChar(char: str):
    """Confirms that a char can be used in RESOURCE LOCATIONS"""
    if len(char) != 1:
        return False
    
    if char in list(LEGAL_CHARS):
        return True
    
    return False

def isValidToConvert(location: str) -> bool:
    """Confirms that a RESOURCE LOCATION can be converted"""
    hasColon = False
    success = True
    for char in location:
        if char == ':':
            if hasColon:
                success = False
            hasColon = True
        elif not isLegalChar(char):
            success = False
    return success

def formatWithNamespace(namespace: str, path: str):
    """Formats `namespace` and `path` to be `namespace:path`"""
    for char in namespace + path:
        if not isLegalChar(char):
            return False, ''
    return True, namespace + ':' + path

def convertFromResourceLocation(location: str):
    """Converts a resource location to a resolved namespace and resolved path"""
    if not isValidToConvert(location):
        return False, '', ''
    
    splitLocation = location.split(':')
    resolvedNamespace = splitLocation[0]
    if not resolvedNamespace:
        resolvedNamespace = 'minecraft'

    resovedPath = splitLocation[1]

    return True, resolvedNamespace, resovedPath

PACK_VERSIONS = {
    '4': {'minimum': (1, 13, 0), 'maximum': (1, 14, 4)},
    '5': {'minimum': (1, 15, 0), 'maximum': (1, 16, 1)},
    '6': {'minimum': (1, 16, 2), 'maximum': (1, 16, 5)},
    '7': {'minimum': (1, 17, 0), 'maximum': (1, 17, 1)},
    '8': {'minimum': (1, 18, 0), 'maximum': (1, 18, 1)},
    '9': {'minimum': (1, 18, 2), 'maximum': (1, 18, 2)},
    '10': {'minimum': (1, 19, 0), 'maximum': (1, 19, 3)},
    '12': {'minimum': (1, 19, 4), 'maximum': (1, 19, 4)},
    '15': {'minimum': (1, 20, 0), 'maximum': (1, 20, 1)},
    '18': {'minimum': (1, 20, 2), 'maximum': (1, 20, 2)},
    '26': {'minimum': (1, 20, 3), 'maximum': (1, 20, 4)},
    '41': {'minimum': (1, 20, 5), 'maximum': (1, 20, 6)},
    '48': {'minimum': (1, 21, 0), 'maximum': (1, 21, 1)},
    '57': {'minimum': (1, 21, 2), 'maximum': (1, 21, 3)},
    '61': {'minimum': (1, 21, 4), 'maximum': (1, 21, 4)},
    '71': {'minimum': (1, 21, 5), 'maximum': (1, 21, 5)},
    '80': {'minimum': (1, 21, 6), 'maximum': (1, 21, 6)},
    '81': {'minimum': (1, 21, 7), 'maximum': (1, 21, 8)},
    '85': {'minimum': (1, 21, 9), 'maximum': (1, 21, 9)},
}

def getPackFormatRange(formatNumber: int):
    version = PACK_VERSIONS.get(str(formatNumber))
    if version:
        return version.get('minimum', (1, 21, 8)), version.get('minimum', (1, 21, 8))
    else:
        return None
    
def getPackFormatId(version: GameVersion):
    for id, formatRange in PACK_VERSIONS.items():
        minimum = GameVersion.fromTuple(formatRange['minimum'])
        maximum = GameVersion.fromTuple(formatRange['maximum'])

        if (version <= maximum) and (version >= minimum):
            return id
        
    return None
