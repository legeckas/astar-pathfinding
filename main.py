import sys
from PyQt5 import QtCore, QtWidgets
from astar_pathfinding_ui import Ui_MainWindow


class ApplicationWindow(QtWidgets.QMainWindow):

	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)


class ApplicationController:
	def __init__(self):
		self.app = QtWidgets.QApplication(sys.argv)
		self.window = ApplicationWindow()
		self.window.show()

		self.grid = []

		self.grid_generator()

		sys.exit(self.app.exec_())

	def grid_generator(self):
		x = 0
		y = 0
	
		# Generates nodes in the grid array
		for i in range(0, 15):
			self.grid.append([])
			for j in range(0, 15):
				self.grid[i].append(Node(i, j))
	
				self.window.ui.button = QtWidgets.QPushButton(self.window.ui.centralwidget)
				self.window.ui.button.setGeometry(QtCore.QRect(x, y, 20, 20))
				self.window.ui.button.setText("{x},{y}".format(x=i,y=j))
				self.window.ui.button.setObjectName("{x},{y}".format(x=i,y=j))
				self.window.ui.button.show()
	
				y += 20
	
			x += 20
			y = 0

class Node:
	def __init__ (self, x_coordinate, y_coordinate):
		self.x_coordinate = x_coordinate
		self.y_coordinate = y_coordinate
		self.name = "{x},{y}".format(x=self.x_coordinate,y=self.y_coordinate)

		self.is_start = False
		self.is_end = False
		self.is_obstacle = False

"""
/// Getting neighbors of a node /// 

Situation:			n - 2,2		x,y
  1   2   3			a - 1,1		x-1,y-1
1_a_|_b_|_c_		b - 2,1		x,y-1
2_d_|_n_|_e_		c - 3,1		x+1,y-1
3 f | g | h			d - 1,2		x-1,y
					e - 3,2		x+1,y
					f - 1,3		x-1,y+1
					g - 2,3		x,y+1
					h - 3,3		x+1,y+1
"""

if __name__ == "__main__":
	ApplicationController()