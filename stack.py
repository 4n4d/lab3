class Stack:
    def __init__(self):
        self.destructive_mode = False
        self.iter_index = []
        self.stack_list = []
        self.s_iterator = []

    def pop(self):
        if (self.is_empty()==False):
            return self.stack_list.pop()
        
    def push(self,x):
        self.stack_list.append(x)
        
    def is_empty(self):
        if not self.stack_list:
            return True
        else:
            return False

    def __iter__(self):
        if self.destructive_mode == False:
            self.iter_index.append([len(self.stack_list), True])
        else:
            self.destructive_mode = False
        return (self)

    def next(self):
        if self.iter_index[-1][0] == 0 or self.is_empty():
            self.iter_index.pop()
            raise StopIteration()
        self.iter_index[-1][0] = self.iter_index[-1][0] - 1
        if self.iter_index[-1][1] == False:
            return self.pop()
        return self.stack_list[self.iter_index[-1][0]]

    def destructive_iterator(self):
        self.destructive_mode = True
        self.iter_index.append([len(self.stack_list), False])
        return (self)
        
