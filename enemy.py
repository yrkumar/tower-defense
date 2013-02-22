###########################################
# Enemy Wave class
###########################################

class EnemyWave(object):
	def __init__(self, numEnemies, rows, cols, cellDim, startLocation, board):
		self.wave = []
  	

###########################################
# Enemy class
###########################################

class Enemy(object):
	def __init__(self, boardRows, boardCols, cellDim, startLocation, 
	board, enemyHealth, color):
		(self.rows, self.cols, self.cellDim) = (boardRows, 
		boardCols, cellDim)
		(self.startLocation, self.board) = (startLocation, board)
		self.location = self.calculateLocation(startLocation, cellDim)	
		self.center = self.calculateCenter(self.location)
		self.color = color
		self.direction = [1, 0]
		self.health = enemyHealth
		self.speedFactor = 1
		self.setSpeedFactor()
		self.counter = 0

	def __repr__(self):
		return "Enemy(%r)" % (self.location)

	def calculateLocation(self, startLocation, cellDim):
		startx = startLocation[1]*cellDim
		starty = (startLocation[0]+1)*cellDim
		endx = startx + cellDim
		endy = starty + cellDim
		return [startx, starty, endx, endy]

	def calculateCenter(self, location):	
		centerX = (location[2] - location[0])/2.0 + location[0]
		centerY = (location[3] - location[1])/2.0 + location[1]
		return [centerX, centerY]

	def setSpeedFactor(self):
		if self.color == "pink" or self.color == "yellow":
			self.speedFactor = 8.0/5
		elif self.color == "cyan" or self.color == "maroon":
			self.speedFactor = 2.0
 
	def moveEnemy(self):
		(row, col) = self.getRowCol()	
		(dRow, dCol) = (self.direction[0], self.direction[1])
		if self.speedFactor == 0.2 and self.isAtEdge():
			self.counter += 1
			if self.counter % 2 == 0:
				self.setSpeedFactor()
		if (row, col) == (self.startLocation[0]+1, 
		self.startLocation[1]):
			pass
		elif self.isAtTurningRTC(row, col):
			self.moveEnemyRow(row, col)
			self.moveEnemyCol(row, col)
			(dRow, dCol) = (self.direction[0], self.direction[1])
		elif self.isAtTurningCTR(row, col):
			self.moveEnemyRow(row, col)
			self.moveEnemyCol(row, col)
			(dRow, dCol) = (self.direction[0], self.direction[1])
		self.location[0] += int(self.cellDim/8 * dCol * self.speedFactor)  
		self.location[2] += int(self.cellDim/8 * dCol * self.speedFactor)
		self.location[1] += int(self.cellDim/8 * dRow * self.speedFactor)
		self.location[3] += int(self.cellDim/8 * dRow * self.speedFactor)
		self.center = self.calculateCenter(self.location)
		 
	def getRowCol(self):
		row = self.location[1]/self.cellDim
		col = self.location[0]/self.cellDim
		return (row, col)

	def isAtEdge(self):
		if self.direction == [1, 0] or self.direction == [-1, 0]:
			if (self.location[1] % self.cellDim == 0 or 
			self.location[3] % self.cellDim == 0):
				return True
			return False
		elif self.direction == [0, 1] or self.direction == [0, -1]:
			if (self.location[0] % self.cellDim == 0 or 
			self.location[2] % self.cellDim == 0):
				return True
			return False
		return False
	
	def isAtTurningRTC(self, row, col):
		if (self.direction[1] == 1 or 
		self.direction[1] == -1):
			if self.location[2] % self.cellDim == 0:
				if row+1>=self.rows:
					return self.board[row-1][col] == 1
				elif row-1<0:
					return self.board[row+1][col] == 1
				else:
					return (self.board[row+1][col] == 1 or 
					self.board[row-1][col] == 1)
		return False
	
	def isAtTurningCTR(self, row, col):
		if (self.direction[0] == 1 or 
		self.direction[0] == -1):
			if self.location[3] % self.cellDim == 0:
				if col+1>=self.cols:
					return self.board[row][col-1] == 1
				elif col-1<0:
					return self.board[row][col+1] == 1
				else:
					return (self.board[row][col+1] == 1 or 
					self.board[row][col-1] == 1)
		return False
	
	def moveEnemyRow(self, row, col):
		if self.direction[0] == 1:
			if row+1<self.rows and self.board[row+1][col] != 1:
				self.direction[0] = 0
			elif row+1>=self.rows:
				self.direction[0] = 0
		elif self.direction[0] == -1:
			if row-1>0 and self.board[row-1][col] != 1:
				self.direction[0] = 0
			elif row-1<=0:
				self.direction[0] = 0
		elif self.direction[0] == 0:
			if row+1<self.rows and self.board[row+1][col] == 1:
				self.direction[0] = 1
			elif row-1>0 and self.board[row-1][col] == 1:
				self.direction[0] = -1

	def moveEnemyCol(self, row, col):
		if self.direction[1] == 1:
			if col+1<self.cols and self.board[row][col+1] != 1:
				self.direction[1] = 0
			elif col+1>=self.cols:
				self.direction[1] = 0
		elif self.direction[1] == -1:
			if col-1>0 and self.board[row][col-1] != 1:
				self.direction[1] = 0
			elif col-1<=0:
				self.direction[1] = 0
		elif self.direction[1] == 0:
			if col+1<self.cols and self.board[row][col+1] == 1:
				self.direction[1] = 1
			elif col-1>0 and self.board[row][col-1] == 1:
				self.direction[1] = -1

	def slowSpeed(self):
		self.speedFactor = 0.2

