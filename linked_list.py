# ecoding=utf-8
# Author: Sven_Weng
# Email : sven_weng@wengyb.com
# Web   : http://www.wengyb.com


class Node(object):
	def __init__(self, value=None, next=None):
		self.value = value
		self.next = next

	def get_value(self):
		return self.value

	def get_next(self):
		return self.next

	def set_next(self, next):
		self.next = next

	def set_value(self, value):
		self.value = value


class LinkedList(object):
	"""单向链表"""

	def __init__(self):
		self.head = Node()
		self.tail = None
		self.length = 0

	def is_empty(self):
		"""判断链表是否为空"""
		return self.head is None

	def add2head(self, value):
		"""向链表头部新增数据"""
		node = Node(value)
		if self.head.get_value() is None:
			self.head = node
		else:
			node.set_next(self.head)
			self.head = node
		self.length += 1

	def append(self, value):
		"""向链表尾部新增数据"""
		p = self.head
		tail_node = Node(value)
		if self.length != 0:
			for i in range(self.length):
				if p.get_next() is None:
					p.set_next(tail_node)
					self.length += 1
					break
				p = p.get_next()
		else:
			self.add2head(value)

	def insert(self, value, index):
		"""
		向链表中插入一个元素
		:param value: 插入的元素
		:param index: 对应的序列
		:return: None
		"""
		index = int(index)
		if index > self.length or index < 0:
			raise OverflowError(
				"index is out of range , linked list length is {0}, you give is {1}".format(self.length, index))
		if index == self.length:
			self.append(value)
			return
		if index == 0:
			self.add2head(value)
			return
		i_node = Node(value)
		p = self.head
		for i in range(self.length):
			if i == index - 1:
				n_p = p.get_next()
				p.set_next(i_node)
				i_node.set_next(n_p)
				self.length += 1
				break
			p = p.get_next()

	def remove(self, value, step=0):
		"""
		链表中移除一个元素, 如果链表中存在多个值相同的元素，step值指定删除第几个相同的
		:param value:
		:param step:
		:return:
		"""
		p = self.head
		_step_count = 0
		f_p = None
		for i in range(self.length):
			if p.get_value() == value:
				if _step_count != step:
					_step_count += 1
				else:
					if not f_p:
						self.head = p.get_next()
					else:
						f_p.set_next(p.get_next())
					break
			f_p = p
			p = p.get_next()
		self.length -= 1

	def index(self, value, step=0):
		"""
		获取某个值的序号， 如果存在元素重复，可以通过step来指定返回第几个
		:param value: 值
		:param step: 步进值
		:return:
		"""
		p = self.head
		_step = 0
		for i in range(self.length):
			if p.get_value() == value:
				if _step == step:
					return i
			p = p.get_next()
		else:
			raise OverflowError("The value is no in LinkedList")

	def __str__(self):
		v = []
		p = self.head
		for i in range(self.length):
			v.append(p.get_value())
			p = p.get_next()
		return "->".join(v)

	def __len__(self):
		return self.length

	def __getitem__(self, item):
		if item > self.length or item < 0:
			raise OverflowError(
				"index is out of range , linked list length is {0}, you give is {1}".format(self.length, item))
		p = self.head
		for i in range(self.length):
			if item == i:
				return p.get_value()
			p = p.get_next()


if __name__ == '__main__':
	ll = LinkedList()
	ll.add2head("a")
	ll.append("b")
	ll.append("c")
	ll.append("d")
	ll.remove("d")
	ll.insert("test", 2)
	# print(ll.index("b"))
	print ll
	print len(ll)
	print ll[3]
