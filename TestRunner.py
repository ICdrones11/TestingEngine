#!/usr/bin/python
from TestCaseParser import TestCaseParser


class TestRunner:
    def __init__(self, folderName):
        self.testCaseParser = TestCaseParser(folderName)
        self.testCases = self.testCases.loadAll()

    def runOne(self):
        test = self.testCases.pop()
        return test.run()

    # TODO: make sure we can tell which tests fail. (log out in green or red).
    def runAll(self):
        testCases = self.testCaseParser.loadAll()
        for testCase in testCases:
            success = testCase.run()
            # print ..



def main():
    print 'Initializing test runner.'
    runner = TestRunner("droneData")
    runner.runAll()

if __name__ == "__main__":
    main()



