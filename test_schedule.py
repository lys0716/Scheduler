from schedule_persist import Schedule
import os

class TestClass:

	s = None
	names = []
	descriptions = []
	prioritys = []
	due_hours = []

	def test_init(self):
		self.names.append('eason')
		self.descriptions.append('awesome')
		self.prioritys.append(1)
		self.due_hours.append('2h')
		self.s = Schedule()
		assert not os.path.isfile(self.s.filepath)

	def test_get(self):
		self.s = Schedule()
		assert self.s.get_task(self.names[0]) == ''

	def test_add(self):
		self.s = Schedule()
		for i in range(len(self.names)):
			self.s.add_task(self.names[i], self.descriptions[i], self.prioritys[i], self.due_hours[i])
			assert self.s.get_task(self.names[i]) == '%-10s %-5s %-5s %-50s' % (self.names[i], self.prioritys[i], self.due_hours[i], self.descriptions[i])
		assert os.path.isfile(self.s.filepath)
		assert len(self.s.task.keys()) == len(self.names)

	def test_delete(self):
		self.s = Schedule()
		self.s.delete_task(self.names[0])
		assert len(self.s.task.keys()) == len(self.names) - 1
