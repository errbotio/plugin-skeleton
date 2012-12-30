# This is a skeleton for Err plugins, use this to get started quickly.

from errbot import BotPlugin, botcmd
from errbot.builtins.webserver import webhook

class Skeleton(BotPlugin):
	"""An Err plugin skeleton"""
	min_err_version = '1.6.0' # Optional, but recommended
	max_err_version = '1.7.1' # Optional, but recommended

	def activate(self):
		"""Triggers on plugin activation
		
		In this case, starts a poller that triggers each second
		"""
		super(Skeleton, self).activate()

		# Make sure our shelf has a counter. Putting this check here saves
		# an if statement being executed once every second (in the poller)
		if 'counter' not in self.shelf.keys():
			self.shelf['counter'] = 0
		self.start_poller(1, self.poll)

	def get_configuration_template(self):
		"""Defines the configuration structure this plugin supports"""
		return {'EXAMPLE_KEY_1': "Example value",
		        'EXAMPLE_KEY_2': ["Example", "Value"]
		       }

	def poll(self):
		"""An example poller which increments a simple counter"""
		self.shelf['counter'] += 1

	# Passing split_args_with=None will cause arguments to be split on any kind
	# of whitespace, just like Python's split() does
	@botcmd(split_args_with=None)
	def counter_show(self, mess, args):
		"""Return the number of counter ticks since reset"""
		return "My counter has ticked {0} times since being reset".format(self.shelf['counter'])

	@botcmd(split_args_with=None)
	def counter_reset(self, mess, args):
		"""Reset the counter"""
		self.shelf['counter'] = 0
		return "Counter reset"

	@webhook
	def counter(self, incoming_request):
		return "My counter has ticked {0} times since being reset\n".format(self.shelf['counter'])
