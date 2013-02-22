###########################################
# Shot class
###########################################

class Shot(object):
	def __init__(self, tower, enemy, board, cellDim):
		self.targetEnemy = enemy
		self.originTower = tower
		self.rows = len(board)
		self.cols = len(board[0])
		self.cellDim = cellDim
		self.speed = 15
		self.color = self.whichColor(self.originTower)
		self.location = self.calculateLocation(self.originTower)
		self.angle = self.calculateAngle(self.originTower, 
		self.targetEnemy)
		self.dx = -1*math.cos(self.angle)*self.speed
		self.dy = -1*math.sin(self.angle)*self.speed
		self.center = self.calculateCenter(self.location)

	def __repr__(self):
		return "Shot(%r, %r, %r)" % (self.location, self.dx, self.dy)
		
	def whichColor(self, tower):
		if isinstance(tower, OrangeTower):
			return "orange"
		elif isinstance(tower, RedTower):
			return "red"
		elif isinstance(tower, GreenTower):
			return "green"
		elif isinstance(tower, PurpleTower):
			return "#8C489F" 

	def calculateLocation(self, tower):
		startx = tower.center[0]-5
		starty = tower.center[1]-5
		endx = startx+10
		endy = starty+10
		location = [startx, starty, endx, endy]
		return location

	def calculateAngle(self, tower, enemy):
		xDistance = tower.center[0] - enemy.center[0]
		yDistance = tower.center[1] - enemy.center[1]
		angle = math.atan2(yDistance, xDistance)
		return angle

	def calculateCenter(self, location):
		centerX = (location[2] - location[0])/2.0 + location[0]	
		centerY = (location[3] - location[1])/2.0 + location[1]
		return [centerX, centerY]

	def moveShot(self):
		self.location[0] += self.dx * self.originTower.shotSpeed
		self.location[1] += self.dy * self.originTower.shotSpeed
		self.location[2] += self.dx * self.originTower.shotSpeed
		self.location[3] += self.dy * self.originTower.shotSpeed
		self.center = self.calculateCenter(self.location)

	def isOffScreen(self):
		if (self.location[0] < 0 or 
		self.location[1] < 0 or 
		self.location[2] > (self.cols+1)*self.cellDim or 
		self.location[3] > (self.rows+1)*self.cellDim):
			return True
		return False


###########################################
# Button class
###########################################

class TowerButton(object):
	def __init__(self, buttonNum, canvas, towerName, boardDim):
		self.buttonNum = buttonNum
		self.canvas = canvas
		self.towerName = towerName
		self.statsBarWidth = 200
		self.towerBarTopPad = 60
		self.iconColor = towerName[:len(towerName)-6]
		startx, endx = boardDim+10, (boardDim+
		self.statsBarWidth-10)
		starty = (self.towerBarTopPad+10+
		(buttonNum*60+10)+self.buttonNum*10) 
		endy = starty + 60
		self.location = [startx, starty, endx, endy]

	def __repr__(self):
		return "Button(%r, %r)" % (self.location, self.iconColor)

	def drawButton(self, pressed):
		if pressed == False:
			self.canvas.create_rectangle(self.location[0],
			self.location[1], self.location[2], self.location[3],
			fill="#333333", outline="white")
		elif pressed == True:
			self.canvas.create_rectangle(self.location[0],
			self.location[1], self.location[2], self.location[3],
			fill="#333333", outline=self.iconColor)	
		self.canvas.create_text(self.location[0] + 120, 
		self.location[1]+(self.location[3]-self.location[1])/2, 
		text=self.towerName, fill="white")
		self.drawTowerIcon()
		
	def drawTowerIcon(self):
		startx = self.location[0] + 20
		starty = self.location[1] + ((self.location[3]-
		self.location[1])-40)/2
		endx = startx + 40
		endy = starty + 40
		self.iconLocation = [startx, starty, endx, endy]
		self.canvas.create_oval(startx, starty, 
		endx, endy, fill=self.iconColor)	
