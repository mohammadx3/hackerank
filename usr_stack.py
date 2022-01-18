class mStack:
    def __init__(self,size):
        self.size = size
        self.elements = []

    def pop(self):
        if len(self.elements) == 0:
            print('Stack is empty!!')
            return
        print(f'pop element: {self.elements[-1]}')
        del self.elements[-1]

        
    def push(self,element):
        if len(self.elements) >= self.size:
            print('Stack Overflow!!')
            return
        self.elements.append(element)
        
    def show(self):
        print(self.elements)
    
    def capacity(self):
        print(self.size)

    def seek(self):
        print(self.elements[-1])

if __name__ == '__main__':
    x = mStack(5)
    y = mStack(3)
    x.push(5)
    x.push(9)
    y.push(9)
    y.push(5)
    y.push(4)
    x.push(4)
    y.seek()
    x.push(2)
    x.push(1)
    x.show()
    y.show()
    x.seek()
    x.capacity()
   