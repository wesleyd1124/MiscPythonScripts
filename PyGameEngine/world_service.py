import game_objects


class World_Service(game_objects.GameObject):
	def __init__(self, parent, name):
		super().__init__(parent, name)

	def new_scene(self, scene_config):
		pass

	def add_child(self, child):
		if(isinstance(child, Scene)):
			super().add_child(child)


class Scene(game_objects.GameObject):
	def __init__(self, parent, name, scene_id):
		super().__init__(parent, name)
		self.scene_id = scene_id

