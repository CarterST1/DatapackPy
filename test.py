import datapackpy

dataPack = datapackpy.DataPack((1, 21, 1), 'cartermods', 'cst')
print(dataPack)

print(dataPack.meta.toJson())
dataPack.save()