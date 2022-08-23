#This is an abstract class for manager

class AbstractManager():

    def __init__(self):
        pass
    
    @abstractmethod
    def run(self):
        '''run a task under certain condition'''
        pass

    @abstractmethod
    def stop(self):
        '''stop a task under certain condition'''
        pass

    @abstractmethod
    def check_alive(self):
        '''regularly check if certain tasks are alive'''
        pass

    @abstractmethod
    def detect_failure(self):
        '''detect the failure of certain tasks'''
        pass

    @abstractmethod
    def roll_back(self):
        '''after a failure occurs, determine how to roll back and act roll-back'''
        pass