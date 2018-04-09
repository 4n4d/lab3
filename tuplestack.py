class Stack:
    def __init__(self):
        self.destructive_mode = False
        self.iter_index = []
        self.stack_tuple = ()
        self.stack_height = 0

    def pop(self):
        if not self.is_empty():
            t = self.stack_tuple[0]
            self.stack_tuple = self.stack_tuple[1]
            self.stack_height = self.stack_height - 1
            return t
        
    def push(self,x):
        self.stack_tuple = (x, self.stack_tuple)
        self.stack_height = self.stack_height + 1
        
    def is_empty(self):
        if self.stack_height == 0:
            return True
        return False
        
    def __iter__(self):
        if self.destructive_mode == False:
            self.iter_index.append([0, True])
        else:
            self.destructive_mode = False
        return (self)

    def next(self):
        if (self.iter_index[-1][0] == self.stack_height and self.iter_index[-1][1] == True) or self.is_empty():
            self.iter_index.pop()
            raise StopIteration()
        self.iter_index[-1][0] = self.iter_index[-1][0] +  1

        if self.iter_index[-1][1] == False:
            return self.pop()

        t = self.stack_tuple
        for x in range(0,self.iter_index[-1][0]-1):
            t = t[1]
        return t[0]

    def destructive_iterator(self):
        self.destructive_mode = True
        self.iter_index.append([0, False])
        return (self)
        
