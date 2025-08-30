from datapackpy.datapack import DataPack
from datapackpy.internal.game_version import GameVersion
import datapackpy.internal.utils as utils

print(utils.convertFromResourceLocation('minecraft/villager'))

print(utils.formatWithNamespace('minecraft', 'test'))
print(utils.formatWithNamespace('Minecraft', 'test'))
print(utils.getPackFormatRange(80))
print(GameVersion.fromTuple((1, 19)))

print(utils.getPackFormatId(GameVersion.fromTuple((1, 21, 9))))

dataPack = DataPack((1, 21, 1), 'cartermods', 'cst')
print(dataPack)

print(dataPack.meta.toJson())
dataPack.save()