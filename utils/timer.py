import time

class Timer:
    def __init__(self,limit):
        self.limit=limit
        self.start_time=None
    def start(self):
        self.start_time=time.time()
    def time_left(self):
        if self.start_time is None:
            return self.limit
        elapsed=time.time()-self.start_time
        return max(0,int(self.limit-elapsed))
    def is_time_up(self):
        return self.time_left()<=0
    def time_elapsed(self):
        if self.start_time is None:
            return 0
        return int(time.time()-self.start_time)
    
        
        
        
        
        
        