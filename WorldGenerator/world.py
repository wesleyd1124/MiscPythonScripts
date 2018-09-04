import typing
import terrain_generator

class World:
	def __init__(self, name : str, config : typing.Dict):
		self.name : str = name
		self.config : typing.Dict = config

		self._t_generator = terrain_generator.TerrainGenerator(config)
		self.terrain : terrain_generator.Terrain = self._t_generator.generate()