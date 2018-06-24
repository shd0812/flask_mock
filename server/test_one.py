import requests
from server.base_Api import ApiServer_Unittest,run_unnitest

class TestServer(ApiServer_Unittest):
    def setUp(self):
        super(TestServer,self).setUp()
        self.host='http://127.0.0.1:5000'
        self.api_client=requests.session()

    def tearDown(self):
        super(TestServer, self).tearDown()
    def test_create_user_not_existed(self):
        url = "%s/api/users/%d" % (self.host, 25)
        print(url)
        resp = self.api_client.get(url)
        print(resp.content)
if __name__ =='__main__':
    run_unnitest()