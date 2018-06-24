from multiprocessing import  Process
import time
import unittest
from server import mock
import requests

def run_flask():
    mock.app.run(debug=True)
def run_unnitest():
    unittest.main()
class ApiServer_Unittest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api_server_processs = Process(
            target=run_flask
        )
        cls.api_server_processs.start()
        time.sleep(0.1)

    @classmethod
    def tearDownClass(cls):
        cls.api_server_processs.terminate()


if __name__ =='__main__':
    print(111)
    #unittest.main()