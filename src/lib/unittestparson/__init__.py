import document
import unittestgui

class unittest(unittestgui.unittest):
    def main(self):
        l = document.createElement('ul')
        self.resdiv.appendChild(l)
        self.resList = l

        for func in self.tlist:
            try:
                self.setup()
                func()
                self.tearDown()
            except Exception as e:
                self.appendErrorResult(e)
                self.numFailed += 1
                raise
        self.showSummary()

    def appendErrorResult(self, error):
        msg = '<div>Error in parsing/executing your program:</div><span class="error">' + str(error) + '</span>'
        self.appendFeedbackMessage(msg, "error")

    def appendResult(self,res,actual,expected,feedback):
        msg = '<div class="feedback">' + feedback + '</div>'
        if res:
            self.numPassed += 1
            status = "pass"
        else:
            msg += '<span class="expected">Expected %s %s</span>' % (str(actual),str(expected))
            self.numFailed += 1
            status = "fail"
        self.appendFeedbackMessage(msg, status)

    def appendFeedbackMessage(self, msg, status):
        pTag = document.createElement('li')
        pTag.setAttribute("class", "testcase " + status)
        pTag.innerHTML = msg
        self.resList.appendChild(pTag)

    def showSummary(self):
        pct = self.numPassed / (self.numPassed+self.numFailed) * 100
        pTag = document.createElement('p')
        pTag.setAttribute("class", "summary")
        pTag.innerHTML = "You passed: " + str(pct) + "% of the tests"
        self.resdiv.appendChild(pTag)
        if pct < 90:
            self.resdiv.setCSS('background-color','#de8e96')
        else:
            self.resdiv.setCSS('background-color','#83d382')



