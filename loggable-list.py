import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, elem):
        super().append(elem)
        return self.log(elem)


lgl = LoggableList()
lgl.append('Hello')
