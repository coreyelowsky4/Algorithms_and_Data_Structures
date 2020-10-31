import math

class Heap:

	def __init__(self, data = None):

		self.heap = []

		if data != None:
			self.buildHeap(data)

	def getLevel(self):
		pass

	def numLevels(self):
		return int(math.log(len(self.heap),2)) + 1

	def parentIndex(self, i):
		return int((i - 1)/2)

	def leftChild(self, i):
		return 2*i + 1

	def rightChild(self,i):
		return 2*i + 2

	def buildHeap(self,data):
		
		# iterate through items
		for item in data:

			# append to end of heap
			self.heap.append(item)

			# heapify up
			self.heapifyUp(len(self.heap)-1)


	def heapifyUp(self, i):
		
		while self.parentIndex(i) >= 0 and self.heap[self.parentIndex(i)] > self.heap[i]:
			self.swap(i,self.parentIndex(i))
			i = self.parentIndex(i)


	def swap(self, i, j):
		tmp = self.heap[j]
		self.heap[j] = self.heap[i]
		self.heap[i] = tmp

	def display(self,orientation='vertical'):
		if orientation == 'vertical':
			self.displayVertical()
		elif orientation == 'horizontal':
			self.displayHorizontal(0,0)

	def displayVertical(self):
		for level in range()


	def displayHorizontal(self,i,depth):
		if i >= 0 and i < len(self.heap):
			self.displayHelper(self.rightChild(i), depth+1)
			print('\t'*depth + str(self.heap[i]))
			self.displayHelper(self.leftChild(i),depth+1)




if __name__ == '__main__':

	print('\n#####')
	print('Heap')
	print('#####\n')

	heap = Heap([5,2,3,5,6,8,9,10,-1])
	print(heap.numLevels())



