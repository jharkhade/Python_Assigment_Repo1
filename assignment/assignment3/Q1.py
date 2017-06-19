class Enemey:
	life = 3
	
	def attack(self):
		print ("ocuh!")
		self.life -=1
	
	def checklife(self):
		if self.life <= 0:
			print ('i am dead')
		else:
			print (str(self.life) + " life left")
			
enemy1 = Enemey()
enemy2 = Enemey()

enemy1.attack()
enemy1.attack()
enemy1.attack()
enemy1.checklife()
enemy2.checklife()
enemy2.checklife()


