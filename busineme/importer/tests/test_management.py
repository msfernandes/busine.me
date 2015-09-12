from configuration.tests import ManagementTest
from importer.management.commands.import_data import Command




class TestManagement(ManagementTest):

	"""docstring for API_Views"""

	def test_command(self):
		command = Command()
		self.assertIsNone(command.handle())
