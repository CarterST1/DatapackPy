import datapackpy

print(datapackpy.internal.utils.convertFromResourceLocation('minecraft/villager'))

print(datapackpy.internal.utils.formatWithNamespace('minecraft', 'test'))
print(datapackpy.internal.utils.formatWithNamespace('Minecraft', 'test'))
print(datapackpy.internal.utils.getPackFormatRange(80))
print(datapackpy.internal.GameVersion.fromTuple((1, 19)))

print(datapackpy.internal.utils.getPackFormatId(datapackpy.internal.GameVersion.fromTuple((1, 21, 9))))

dataPack = datapackpy.DataPack((1, 21, 1), 'cartermods', 'cst')
print(dataPack)

print(dataPack.meta.toJson())
dataPack.save()