import pygame
import numpy as np
import math
import sounddevice as sd


pygame.init()

window = pygame.display.set_mode((1000, 600))
running = True

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
GREEN = (60, 200, 60)
YELLOW = (200, 200, 40)

class Button:
	def __init__(self, x, y, width, height, color, text, text_color):
		self.rect = pygame.Rect(x, y, width, height)
		self.color = color
		self.text = text
		self.text_color = text_color

	def draw(self, surface):
		pygame.draw.rect(surface, self.color, self.rect)
		font = pygame.font.Font(None, 40)
		text_surface = font.render(self.text, True, self.text_color)
		text_rect = text_surface.get_rect(center=self.rect.center)
		surface.blit(text_surface, text_rect)

	def is_clicked(self, pos):
		return self.rect.collidepoint(pos)

class Graph:
	def __init__(self, x, y, width, height, color, graph_color, graph):
		self.rect = pygame.Rect(x, y, width, height)
		self.hheight = (self.rect.height - 15) / 2
		self.color = color
		self.graph_color = graph_color
		self.graph = graph
		self.default_size = 3000
		self.scale_y = [self.hheight / np.max(self.graph), self.hheight / np.min(self.graph)]
		self.scale_x = width / self.default_size

	def draw(self, surface):
		pygame.draw.rect(surface, self.color, self.rect, 2)

		x = 0
		lines = []
		for i in range(1, self.default_size, int(1 / self.scale_x)):
			x_pos = x + self.rect.x
			if x_pos >= self.rect.x + self.rect.width:
				break
			y_pos = int(self.graph[i] * self.scale_y[0]) + self.rect.y + int(self.rect.height / 2)
			lines.append([x_pos, y_pos])
			x += 1

		pygame.draw.lines(window, self.graph_color, False, lines)

	def add_freq(self, freq):
		self.graph += np.sin(2 * np.pi * freq * t / sample_rate) * volume
		self.scale_y = [self.hheight / np.max(self.graph), self.hheight / np.min(self.graph)]




sample_rate = 44100
duration = 3
volume = 0.03


t = np.arange(int(sample_rate * duration))
raw_data = np.sin(2 * np.pi * 261.63 * t / sample_rate) * volume



play_sound = Button(20, 20, 100, 50, GRAY, "Play", BLACK)
add_E = Button(140, 20, 180, 50, GRAY, "Add E Note", BLACK)
add_G = Button(340, 20, 180, 50, GRAY, "Add G Note", BLACK)
sound_graph = Graph(20, 100, 800, 300, GRAY, YELLOW, raw_data)
print(sound_graph.graph[0])


while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			if play_sound.is_clicked(event.pos):
				sd.play(raw_data, sample_rate)
				sd.wait()
			if add_E.is_clicked(event.pos):
				sound_graph.add_freq(329.63)
			if add_G.is_clicked(event.pos):
				sound_graph.add_freq(391.99)

	window.fill(BLACK)

	play_sound.draw(window)
	add_E.draw(window)
	add_G.draw(window)
	sound_graph.draw(window)

	pygame.display.flip()