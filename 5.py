class User:
	def __init__(self, balance):
		self.balance = balance
	
	def transfer(self, destination, money):
		if self.balance >= money:
			self.balance -= money
			destination.balance += money


f_line = [int(i) for i in input().split(' ')]
N, T = f_line
dataBase = dict({})

for _ in range(N):
	data = input().split(' ')
	dataBase[data[0]] = User(int(data[1]))

for _ in range(T):
	data = input().split(' ')
	dataBase[data[0]].transfer(dataBase[data[1]], int(data[2]))

t = []
for key, val in dataBase.items():
	t.append((key, val.balance))

t.sort(key=lambda x: x[0])

for thing in t:
	print(thing[0], thing[1])
