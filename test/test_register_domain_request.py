# coding: utf-8

"""
    MONEI API v1

    <p>The MONEI API is organized around <a href=\"https://en.wikipedia.org/wiki/Representational_State_Transfer\">REST</a>. Our API has predictable resource-oriented URLs, accepts JSON-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.</p> <h4 id=\"base-url\">Base URL:</h4> <p><a href=\"https://api.monei.com/v1\">https://api.monei.com/v1</a></p> <h4 id=\"client-libraries\">Client libraries:</h4> <ul> <li><a href=\"https://github.com/MONEI/monei-php-sdk\">PHP SDK</a></li> <li><a href=\"https://github.com/MONEI/monei-python-sdk\">Python SDK</a></li> <li><a href=\"https://github.com/MONEI/monei-node-sdk\">Node.js SDK</a></li> <li><a href=\"https://postman.monei.com/\">Postman Collection</a></li> </ul>   # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import Monei
from Monei.models.register_domain_request import RegisterDomainRequest  # noqa: E501
from Monei.rest import ApiException

class TestRegisterDomainRequest(unittest.TestCase):
    """RegisterDomainRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RegisterDomainRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = Monei.models.register_domain_request.RegisterDomainRequest()  # noqa: E501
        if include_optional :
            return RegisterDomainRequest(
                domain_name = 'example.com'
            )
        else :
            return RegisterDomainRequest(
                domain_name = 'example.com',
        )

    def testRegisterDomainRequest(self):
        """Test RegisterDomainRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
