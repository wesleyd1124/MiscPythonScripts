import world
import terrain_generator


config = {"terrain_width":10, "terrain_height":10}
my_world = world.World("Test World", config)

for y in my_world.terrain.tiles:
	row = ""
	for tile in y:
		if(tile["terrain"] == terrain_generator.TerrainType.WATER):
			row+="≈"
	print(row)