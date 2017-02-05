import yaml
import sys
import os
import ConfigParser

project_path = os.environ['PROJECT_FOLDER']
config = ConfigParser.RawConfigParser()
config.read(project_path + '/config/prd.cfg')
persist_file = config.get('file','persist_path')
FILEPATH = project_path + persist_file

class Schedule(object):

	task = None
	filepath = None

	def __init__(self):
		self.filepath = FILEPATH
		if os.path.isfile(self.filepath):
			with open(self.filepath, 'r+') as f:
				self.task = yaml.load(f)
		else:
			self.task = {}

	def _save_to_file(self):
		with open(self.filepath, 'w+') as f:
			yaml.dump(self.task, f)

	def add_task(self, name, description, priority, due_hour):
		if name in self.task.keys():
			print('Task with name %s already exists' % name)
		new_task = [name, description, priority, due_hour]
		self.task.update({name: new_task})
		self._save_to_file()

	def delete_task(self, name):
		if name not in self.task.keys():
			print('Cannot delete a non-existing task %s' % name)	
		self.task.pop(name, None)
		self._save_to_file()

	def display(self):
		if self.task:
			for v in self.task.values():
				print ('%-10s %-5s %-5s %-50s' % (v[0], v[2], v[3], v[1]))

	def get_task(self, name):
		if name not in self.task.keys():
			return ''
		else:
			return ('%-10s %-5s %-5s %-50s' % (self.task[name][0], self.task[name][2], self.task[name][3], self.task[name][1]))

if __name__=='__main__':
	schedule = Schedule()

	action = sys.argv[1]
	args = sys.argv[2:]

	def add(name, description, priority, due_hour):
		schedule.add_task(name, description, priority, due_hour)
		schedule.display()

	def delete(name):
		schedule.delete_task(name)
		schedule.display()

	def display():
		schedule.display()

	def get(name):
		print schedule.get_task(name)

	options = {
		'add': add,
		'delete' : delete,
		'display': display,
		'get': get
	}

	options[action](*args)