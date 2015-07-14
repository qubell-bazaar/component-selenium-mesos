import os
import requests

from qubell.api.testing import *

@environment({
    "default": {}
})
class SeleniumMesosDevTestCase(BaseComponentTestCase):
    name = "component-selenium-mesos"
    meta = os.path.realpath(os.path.join(os.path.dirname(__file__), '../meta.yml')) 
    apps = [
       {"name": name,
        "file": os.path.realpath(os.path.join(os.path.dirname(__file__), '../%s.yml' % name))
       }
    ]

    @classmethod
    def timeout(cls):
        return 30
   
    @instance(byApplication=name)
    def test_selenium_hub(self, instance):
        host = instance.returnValues['selenium.selenium-hub']
        resp = requests.get(host, verify=False)
        assert resp.status_code == 200
    
