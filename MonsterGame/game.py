import sys

from character import character
from monster import Dragon
from monster import Goblin
from monster import Troll

class Game:
    def setup(self):
        self.player = Character()
        self.monster = [ Goblin(), Troll(), Dragon()]
        self.monster = self.get_next_monster()
		
	def get_new_monster(self):
		try:
			return self.monster.pop(0)
		except IndexError:
			return None
			
	def monster_turn(self):
		
		# Check to see if the monster attacks
		if self.monster.attack():
			# If so, tell the player
			print ('{} is attacking.'.format(self.monster))
			
			# Check if the player wants to dodge
			if input('Dodge? Y/N: ').lower() == 'y':
				if self.player.dodge():
					# If dodged, print that
					print ('You dodged successfuly')
				# If it is not, remove one player hit point
				else:
					print ('You got hit anyway')
					self.player.hit_points -= 1
			else:
				print ('{} hit you for one point!'.format(self.monster))
				self.player.hit_points -= 1
			
		# If the monster is not attacking, tell that to the player too.
		else:
			print ('{} is not attacking this turn. It is your turn now'.format(self.monster))
		
	def player_turn(self):
		# Let the player attack, rest or quit
		action_chioce = input('Your action ([A]ttack, [R]est, [Q]uit): ').lower()
		# If they attack:
			# See if the attack is successful
			if action choice == 'a':
				print ("You are attacking {}!".format(self.monster))
				if self.player.attack():
					if self.monster.dodge():
						print ('{} dodged your attack.'.format(self.monster))
					else:
						if self.player.leveled_up():
							self.monster_hit_points -= 2
						else:
							self.monster_hit_points -= 1
					print ("You hit {} with your {}".format(self.monster, self.player.weapon))
					
				else:
					print ("You missed!")
			
			# If not a good attack, tell the player
				   
			
			# If they rest:
			# Call the player.rest() method
			elif action choice == 'r'
				return self.player.rest()
			# If they quit, exit the game
			elif action choice == 'q':
				sys.exit()
			# If they pick anything else, re-run this method
			else:
				return self.player_turn()
		
		
			
	def cleanup(self):
		# If the monster has no more hit points:
		if self.monster.hit_points <= 0:
			# up ther player's experience
			self.player.experience += self.monster.experience
			# print message
			print ('You killed {}!'format(self.monster))
			# Get a new monster
			self.monster = self.get_next_monster()
			
			
	def __init__(self):
		self.setup()
		
		while self.player.hit_points and (self.monster or self.monsters)
		print ('\n' + '='*20)
		print (self,player)
		self.monster_turn()
		print ('\n' + '-'*20)
		self.player_turn()
		self.cleanup()
		print ('\n' + '='*20)
		
	if self.player_hit_points:
		print ('You win!')
	elif self.monsters or self.monster:
	sys.exit()
		print ('You lose!')
		
Game()
