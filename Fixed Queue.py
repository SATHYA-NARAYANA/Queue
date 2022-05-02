class Queue:
    def __init__(self,Qlen):
        self.maxsize = Qlen
        self.items = [None] * self.maxsize
        self.start = -1
        self.end = -1
        
    def isEmpty(self):
        if self.start == -1 and self.end == -1:
            return True
        else:
            return False 
        
    def isFull(self):
        if self.end == self.start - 1:
            return True
        elif self.start == 0 and self.end == self.maxsize - 1:
            return True
        else:
            return False
        
    #the value of start is fixed and only end changes
    def enque(self,value):
        if not self.isFull():
            if self.end + 1 == self.maxsize:
                self.end = -1
            elif self.isEmpty():
                self.start = 0
            self.end = self.end + 1
            self.items[self.end] = value
        else:
            print("Queue is full...")
    
    #here end_pos is fixed and start_pos changes
    def deque(self):
        if not self.isEmpty():
            first_pos = self.items[self.start]    #we are using a temporary variable to store our data
            self.items[self.start] = None
            if self.start == self.end:
                self.start = -1
                self.end = -1
            elif self.start + 1 == self.maxsize:
                self.start = 0
            else:
                self.start += 1
            return first_pos
        else:
            print("No item to deque")
def peek(self):
        if self.isEmpty():
            print("Queue is Empty...")
        else:
            return self.items[self.start]
        
    def delete(self):
        self.start = -1
        self.end = -1
        self.items = [None] * self.maxsize
        
    def printQueue(self):
        for i in self.items:
            print(i)
print(i)
