from modules.game_version import GameVersion
import modules.utils as utils

print(utils.convertFromResourceLocation('minecraft/villager'))

print(utils.formatWithNamespace('minecraft', 'test'))
print(utils.formatWithNamespace('Minecraft', 'test'))
print(utils.getPackFormatRange(80))
print(GameVersion.fromTuple((1, 19)))