__author__ = 'vkaravir'

class unittest():
    """
    A simple unittest class to be used with the js-parsons
    exercise framework: https://github.com/vkaravir/js-parsons/
    """
    def __init__(self):
        self.tlist = []
        testNames = {}
        for name in dir(self):
            if name[:4] == 'test' and name not in testNames:
                self.tlist.append(getattr(self,name))
                testNames[name]=True

    def setup(self):
        pass

    def tearDown(self):
        pass

    def main(self):
        self.result = []
        for func in self.tlist:
            try:
                self.setup()
                func()
                self.tearDown()
            except Exception as e:
                self.appendErrorResult(e)

        # join the result array to return a JSON string
        return '[' + ', '.join(self.result) + ']';

    def assertEqual(self, actual, expected, feedback=""):
        res = actual==expected and type(actual)==type(expected)
        self.appendResult(res, actual, ' to be equal to ',expected, feedback)

    def assertNotEqual(self, actual, expected, feedback=""):
        res = actual != expected
        self.appendResult(res, actual, ' to not equal ',expected,feedback)

    def assertTrue(self,x, feedback=""):
        res = x
        self.appendResult(res, x, ' to be ',True,feedback)

    def assertFalse(self,x, feedback=""):
        res = not x
        self.appendResult(res, x, ' to be ',False,feedback)

    def assertIs(self,a,b, feedback=""):
        res = a is b
        self.appendResult(res, a, ' to be the same object as ',b,feedback)

    def assertIsNot(self,a,b, feedback=""):
        res = a is not b
        self.appendResult(res, a, ' to not be the same object as ',b,feedback)

    def assertIsNone(self,x, feedback=""):
        res = x is None
        self.appendResult(res, x, ' to be', None,feedback)

    def assertIsNotNone(self,x, feedback=""):
        res = x is not None
        self.appendResult(res, x, ' to not be ',None,feedback)

    def assertIn(self,a,b, feedback=""):
        res = a in b
        self.appendResult(res, a, ' to be in ',b,feedback)

    def assertNotIn(self,a,b, feedback=""):
        res = a not in b
        self.appendResult(res, a, ' to not be in ',b,feedback)

    def assertIsInstance(self,a,b, feedback=""):
        res = isinstance(a,b)
        self.appendResult(res, a, ' to be an instance of ',b,feedback)

    def assertNotIsInstance(self,a,b, feedback=""):
        res = not isinstance(a,b)
        self.appendResult(res, a, ' to not be an instance of ',b,feedback)

    def assertAlmostEqual(self,a,b, feedback=""):
        res = round(a-b,7) == 0
        self.appendResult(res, a, ' to equal ',b,feedback)

    def assertNotAlmostEqual(self,a,b, feedback=""):
        res = round(a-b,7) != 0
        self.appendResult(res, a, ' to not equal ',b,feedback)

    def assertGreater(self,a,b, feedback=""):
        res = a > b
        self.appendResult(res, a, ' to be greater than ',b,feedback)

    def assertGreaterEqual(self,a,b, feedback=""):
        res = a >= b
        self.appendResult(res, a, ' to be greater than or equal to ',b,feedback)

    def assertLess(self,a,b, feedback=""):
        res = a < b
        self.appendResult(res, a, ' to be less than ',b,feedback)

    def assertLessEqual(self,a,b, feedback=""):
        res = a <= b
        self.appendResult(res, a, ' to be less than or equal to ',b,feedback)

    def appendErrorResult(self, error):
        # generate a JSON string for this error
        self.result.append('{"status":"error", "_error":"%s"}'%str(error))

    def appendResult(self,res,actual,comp, expected,feedback):
        if res:
            status = "pass"
        else:
            status = "fail"
        # generate a JSON string for this result
        jsonstr = '{"status": "%s", "expected": "%s", "actual": "%s", "test":"%s", "feedback":"%s"}' \
                            %(status, str(expected), str(actual), comp, feedback)
        self.result.append(jsonstr)
