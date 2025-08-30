import os
from pathlib import Path
import shutil
import pytest

from modules.datapack import DataPack
from modules.game_version import GameVersion

def test_datapack_supports_tuple():
    datapack = DataPack((1, 21, 8), 'cartermods', 'cst')
    assert datapack.game_version == (1, 21, 8)

def test_datapack_supports_GameVersion():
    datapack = DataPack(GameVersion(1, 21, 8), 'cartermods', 'cst')
    assert datapack.game_version == GameVersion(1, 21, 8)

def test_datapack_str():
    datapack = DataPack((1, 21, 8), 'cartermods', 'cst')
    datapackStr = str(datapack)
    assert datapackStr == 'DataPack[cst | v1.21.8 | format=81]'

def test_datapack_save():
    datapack = DataPack((1, 21, 8), 'cartermods', 'cst')
    tempPath = Path(os.path.expandvars('%TEMP%'))
    path = Path(tempPath / 'tests')

    result = datapack.save(str(path))
    assert result.exists()
    assert result.is_dir()

    shutil.rmtree(path, ignore_errors=True)