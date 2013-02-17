###########################################
# Tower Array class
###########################################

class TowerArray(object):
	def __init__(self):
		self.towerList = []


###########################################
# Tower class
###########################################

class Tower(object):
	def __init__(self, row, col, board, cellDim):
		self.row = row
		self.col = col
		self.board = board
		self.cellDim = cellDim
		self.location = self.calculateLocation(
		self.row, self.col, cellDim)
		self.shotOnScreen = False
		self.radius = 70
		self.center = self.calculateCenter(self.location) 
		self.shots = []
		self.color = "black"
		self.shotSpeed = 1.4
		self.shotDamage = 0
		self.slowDown = False

	def __repr__(self):
		return "Tower(%r, %r, %r)" % (self.row, self.col, self.color)

	def calculateLocation(self, row, col, cellDim):	
		startx = col*cellDim
		starty = row*cellDim
		endx = startx + cellDim
		endy = starty + cellDim
		return [startx, starty, endx, endy]

	def calculateCenter(self, location): 
		centerX = (location[2] - location[0])/2.0 + location[0] 
		centerY = (location[3] - location[1])/2.0 + location[1]
		return [centerX, centerY]

	def fireShot(self, enemy):
		self.shotOnScreen = True
		shot = Shot(self, enemy, self.board, self.cellDim)
		self.shots.append(shot)   
			

###########################################
# Orange Tower class
###########################################

class OrangeTower(Tower):
	def __init__(self, row, col, board, cellDim):
		super(OrangeTower, self).__init__(row, col, board, cellDim)
		self.color = "orange"
		self.cost = 3
		self.shotDamage = 1
	
		
###########################################
# Red Tower class
###########################################

class RedTower(Tower):
	def __init__(self, row, col, board, cellDim):
		super(RedTower, self).__init__(row, col, board, cellDim)
		self.color = "red"
		self.cost = 10
		self.shotDamage = 2


###########################################
# Green Tower class
###########################################

class GreenTower(Tower):
	def __init__(self, row, col, board, cellDim):
		super(GreenTower, self).__init__(row, col, board, cellDim)
		self.color = "green"
		self.cost = 15
		self.shotSpeed = 1.6
		self.radius = 90
		self.shotDamage = 3


###########################################
# Purple Tower class
###########################################

class PurpleTower(Tower):
	def __init__(self, row, col, board, cellDim):
		super(PurpleTower, self).__init__(row, col, board, cellDim)
		self.color = "#8C489F"
		self.radius = 65 
		self.slowDown = True
		self.cost = 20


