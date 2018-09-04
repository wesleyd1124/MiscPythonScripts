import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *



if(__name__ == "__main__"):
	pygame.init()
	display = (800,600)
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

	while True:
		for event in pygame.event.get():
			if(event.type == pygame.QUIT):
				pygame.quit()
				quit()

		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

		pygame.display.flip()