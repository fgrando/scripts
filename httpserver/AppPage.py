import subprocess
from WebPage import *

class AppPage(WebPage):

    def title(self):
        return "<title>Ping</title>"

    def body(self):
        entries = self.getAppResult()

        body = "<p>"
        for entry in entries:
            body = body + "\n" + entry + "<br>"
        body = body + "</p>"

        return "\n<body>" + body + "\n</body>"

    def runAppCommand(self):
        result = subprocess.run(['C:/Windows/System32/ping', 'google.com'], stdout=subprocess.PIPE)
        text = result.stdout.decode("utf-8", errors="ignore")
        return text

    def getAppResult(self):
        raw = self.runAppCommand()
        entries = raw.strip().split("\r\n")
        print(entries)
        return entries

