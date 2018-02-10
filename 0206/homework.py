#1.
def dy_aliqout(n, reservoir):
    for i in range(1,n+1):
        print("i =", i)
        if n % i == 0:
            reservoir[i] = i
            print(reservoir)
            
    return n, reservoir
 
reservoir = {}
dy_aliqout_20, reservoir = dy_aliqout(20, reservoir)           
print('aliqout 20 =', reservoir)



aliqout = []
n = 20
for i in range (1, n+1):
    if n % i == 0:
        aliqout.append(i)

print(aliqout)

def aliqout(n):
    lst = []
    for i in range (1, n+1):
        if n % i == 0:
            lst.append(i)
    
    return lst

print(aliqout(20))

#2번
class Stack:
  # Initializer
  def __init__(self):
    # Attributes
    self.stack = []
    self.num = 0
  
  # Functions
  def is_empty(self):
    # Return True if self.stack is empty
    # Return False if self.stack is not empty
    if len(self.stack) == 0:
        return True
    else:
        return False
    
  def push(self, item):
    # Insert item into self.stack
    self.stack.append(item)
    self.num += 1
    
  def pop(self):
    # Pick up the lastly inserted item
    last_item = self.stack[-1]
    
    # Remove last_item from self.stack
    del self.stack[-1]
    self.num += -1
    
    return last_item
    

eg = Stack()
eg.push("aa")
eg.push(4)
eg.push("go")
eg.push(1)
print(eg.num, eg.stack)
eg.pop()
print(eg.num, eg.stack)
eg.push("go")
eg.push(1)
print(eg.num, eg.stack)
eg.pop()
print(eg.num, eg.stack)


