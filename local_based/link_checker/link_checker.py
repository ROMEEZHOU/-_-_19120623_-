from urllib.robotparser import RobotFileParser

'''check whether a link can be fetched, if so, add it to the queue to wait to be fetch'''
class Link_checker():
    def __init__(self,link):
        self.link=link
        global lock, url_q

    def check_robots(self):
        '''returns a boolean value of whether self.link is allowd by robots agreement'''
        robotparser=RobotFileParser()
        robotparser.set_url(self.link+"/robots.txt")
        robotparser.read()
        return robotparser.can_fetch("*", self.link)

    def check_visited(self):
        '''returns a boolean value of whether self.link has been visited'''
        pass

    def check(self):
        if self.check_robots() and self.check_visited():
            return True
        else:
            return False

    def add_link(self):
        global lock, url_q
        if self.check():
            lock.acquire()
            url_q.put(self.link)
            lock.release()