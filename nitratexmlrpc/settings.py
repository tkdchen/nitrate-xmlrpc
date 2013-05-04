# -*- coding: utf-8 -*-


XMLRPC_METHODS = {
    'nitrate_XMLRPC': (
        ('nitrate.xmlrpc.auth', 'Auth'),
        ('nitrate.xmlrpc.build', 'Build'),
        ('nitrate.xmlrpc.env', 'Env'),
        ('nitrate.xmlrpc.product', 'Product'),
        ('nitrate.xmlrpc.testcase', 'TestCase'),
        ('nitrate.xmlrpc.testcaserun', 'TestCaseRun'),
        ('nitrate.xmlrpc.testcaseplan', 'TestCasePlan'),
        ('nitrate.xmlrpc.testopia', 'Testopia'),
        ('nitrate.xmlrpc.testplan', 'TestPlan'),
        ('nitrate.xmlrpc.testrun', 'TestRun'),
        ('nitrate.xmlrpc.user', 'User'),
        ('nitrate.xmlrpc.version', 'Version'),
        ('nitrate.xmlrpc.tag', 'Tag'),
    ),
}

XMLRPC_TEMPLATE = 'xmlrpc.html'