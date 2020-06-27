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

		self.grid_size = 38
		self.grid = []

		self.start_node = None
		self.end_node = None
		#self.obstacles = []

		self.grid_generator()
		self.button_mapping()

		sys.exit(self.app.exec_())

	def grid_generator(self):
		x = 0
		y = 0
	
		# Generates nodes in the grid array
		for i in range(0, self.grid_size):
			self.grid.append([])
			y = 0

			for j in range(0, self.grid_size):

				self.grid[i].append(Node(i, j))
	
				self.window.ui.button = QtWidgets.QPushButton(self.window.ui.centralwidget)
				self.window.ui.button.setGeometry(QtCore.QRect(x, y, 20, 20))
				self.window.ui.button.setText("{x},{y}".format(x=i,y=j))
				self.window.ui.button.setObjectName("{x},{y}".format(x=i,y=j))
				self.window.ui.button.show()
	
				y += 20
	
			x += 20

	def button_mapping(self):

		for child in self.window.ui.centralwidget.children():
			try:
				child.clicked.connect(self.set_key_nodes)
			except AttributeError:
				pass

		message_window_title = "Setting Key Nodes"
		message_text = "Please set start node, end node, and obstacles. Press 'Begin' when you're ready."

		self.window.ui.readyButton.clicked.connect(self.begin_pathfinding)

		self.show_message(message_window_title, message_text)

	def set_key_nodes(self):
		sender = self.window.ui.centralwidget.sender()
		x, y = self.get_tile_coordinates(sender.objectName())

		if self.start_node is None:
			print("Starting node: ", x, y)
			self.grid[x][y].is_start = True
			self.start_node = self.grid[x][y]
			sender.setStyleSheet("QPushButton {background-color: #F06E69;}")
		elif self.start_node is not None and self.end_node is None:
			print("End node: ", x, y)
			self.grid[x][y].is_end = True
			self.end_node = self.grid[x][y]
			sender.setStyleSheet("QPushButton {background-color: #B2C515;}")
		elif self.start_node is not None and self.end_node is not None and self.node_available(x, y):
			print("Obsctale node: ", x, y)
			self.grid[x][y].is_obstacle = True
			sender.setStyleSheet("QPushButton {background-color: #41424A;}")


	def get_tile_coordinates(self, tile_name):
		coordinates = tile_name.split(",")
		return int(coordinates[0]), int(coordinates[1])

	def node_available(self, x_coordinate, y_coordinate):
		if self.grid[x_coordinate][y_coordinate].is_start or self.grid[x_coordinate][y_coordinate].is_end or self.grid[x_coordinate][y_coordinate].is_obstacle:
			return False
		else:
			return True


	def begin_pathfinding(self):
		print("Works")

	def show_message(self, window_title, message_text):

		message = QtWidgets.QMessageBox()
		message.setWindowTitle(window_title)
		message.setText(message_text)
		message.setStandardButtons(QtWidgets.QMessageBox.Ok)
		message.exec_()

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


#/* Color Theme Swatches in Hex */
# #41424A Light Gray
# #39373B Dark Gray
#.Colorful-2-hex { color: #FFBF00; } Yellow
#.Colorful-3-hex { color: #0099C7; } Blue
#.Colorful-4-hex { color: #F06E69; } Pinkish
#.Colorful-5-hex { color: #B2C515; } Green
