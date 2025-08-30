LEGAL_CHARS = '0123456789abcdefghijklmnopqrstuvwxyz_.'

def isLegalChar(char: str):
    if len(char) != 1:
        return False
    
    if char in list(LEGAL_CHARS):
        return True
    
    return False

def isValidToConvert(location: str) -> bool:
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
    for char in namespace + path:
        if not isLegalChar(char):
            return False, ''
    return True, namespace + ':' + path

def convertFromResourceLocation(location: str):
    if not isValidToConvert(location):
        return False, '', ''
    
    splitLocation = location.split(':')
    resolvedNamespace = splitLocation[0]
    if not resolvedNamespace:
        resolvedNamespace = 'minecraft'

    resovedPath = splitLocation[1]

    return True, resolvedNamespace, resovedPath