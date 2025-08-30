import os
from pathlib import Path
import shutil
import pytest

from datapackpy.internal import utils
from datapackpy.datapack import DataPack
from datapackpy.internal.game_version import GameVersion
from datapackpy.internal.pack_meta import PackMeta

@pytest.fixture
def sample_datapack():
    return DataPack((1, 21, 8), 'cartermods', 'cst')

@pytest.fixture
def sample_meta(sample_datapack):
    return PackMeta(sample_datapack)

def test_meta_pack_set(sample_datapack, sample_meta):
    assert sample_meta.pack == sample_datapack

def test_meta_description_set(sample_meta):
    assert sample_meta.description == 'My First DataPack'

def test_meta_packFormat_set(sample_datapack, sample_meta):
    assert utils.getPackFormatId(sample_datapack.game_version) == sample_meta.pack_format

def test_meta_packFormat_set_invalid():
    # Expect ValueError when creating DataPack with invalid version
    with pytest.raises(ValueError) as exc_info:
        DataPack((0, 1, 0), 'cartermods', 'cst')

    assert "Invalid game version" in str(exc_info.value)

def test_meta_create_file(sample_meta):
    datapack = DataPack((1, 21, 8), 'cartermods', 'cst')
    tempPath = Path(os.path.expandvars('%TEMP%'))
    path = Path(tempPath / 'tests')
    path.mkdir(exist_ok=True)

    result = datapack.meta.createMetaFile(path)
    assert result.exists()
    assert result.is_file()

    shutil.rmtree(path, ignore_errors=True)