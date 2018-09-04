

class GameObject:
	def __init__(self, parent, name):
		self.name = name
		self.parent = parent
		self.children = []

	def add_child(self, child):
		self.children.append(child)

	def remove_child(self, child):
		self.children.remove(child)

	def __setattr__(self, key, value):
		if(key == "parent"):
			if(not hasattr(self.parent, 'add_child')):
				raise Exception(f'{value} is not a GameObject!')
			if(not hasattr(self.parent, 'remove_child')):
				raise Exception('You are not allowed to change the parent of this object!')
			self.parent.remove_child(self)
			value.add_child(self)
		super().__setattr__(key, value)

