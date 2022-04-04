from concurrent.futures import thread
from multiprocessing.connection import wait
import global_values
import time
import threading


class camera:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        self.__moveTargetX = x
        self.__moveTargetY = y
        self.__moveTime = 0
    
    def smoothMoveAndWait(self,x=0,y=0):
        self.__moveTargetX = x
        self.__moveTargetY = y
        initialX = self.x
        initialY = self.y
        t = time.time()
        self.__moveTime = t
        while self.__moveTime == t and ((self.__moveTargetX-self.x)**2 + (self.__moveTargetY-self.y)**2) > 0.0005 and initialX == self.x and initialY == self.y:
            initialX = (self.__moveTargetX - self.x)*0.04 + self.x
            initialY = (self.__moveTargetY - self.y)*0.04 + self.y
            self.x = initialX
            self.y = initialY
            time.sleep(0.01)


        if self.__moveTime == t and initialX == self.x and initialY == self.y:
            self.x = self.__moveTargetX
            self.y = self.__moveTargetY

    def smoothMove(self,x=0,y=0):
        threading.Thread(target=self.smoothMoveAndWait,args=(x,y)).start()
        



