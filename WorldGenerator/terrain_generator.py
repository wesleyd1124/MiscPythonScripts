import typing
from enum import IntEnum

class TerrainGenerator:
	def __init__(self, config : typing.Dict):
		self.config : typing.Dict = config
		if("terrain_width" not in config):
			self.config["terrain_width"] = 500
		if("terrain_height" not in config):
			self.config["terrain_height"] = 500

	def generate(self):
		new_terrain = Terrain(self.config["terrain_width"], self.config["terrain_height"])
		return new_terrain

class TerrainType(IntEnum):
	WATER = 0
	ROCK = 1
	GRASS = 2
	DIRT = 3
	ROAD = 4
	PLANT = 5
	SAND = 6

class Elevation(IntEnum):
	WATER_LEVEL = 0
	DEEP_BELOW = -10
	HIGH_ABOVE = 10

class Terrain:
	def __init__(self, width, height):
		self.tiles = [[{}]*width]*height
		self._width = width
		self._height = height
		for y in range(height):
			for x in range(width):
				self.tiles[y][x] = {"terrain":TerrainType.WATER, "elevation":Elevation.WATER_LEVEL}

	def set_tile(self, terrain_type : int, elevation : int, x : int, y : int):
		assert elevation <= -10 or elevation >= 10, "ERROR: Elevation of tile is not between -10 and 10!"
		assert x <= self._width, "ERROR: X position is greater than width!"
		assert y <= self._height, "ERROR: Y position is greater than height!"
		self.tiles[y][x] = {"terrain":terrain_type, "elevation":elevation}

