class mQueue:
    
    def __init__(self,size = None) -> None:
        if size != None:
            self.size = size
            self.elements = []

    def push(self,elem):
        if(len(self.elements)>=self.size):
            print('Queue is Full!!')
        else: self.elements.append(elem)
    
    def pop(self):
        del self.elements[0]
    
    def seek(self):
        if(len(self.elements)>0):
            print('Current Element: ',self.elements[0])
        else: print('Empty Queue!!')
    
    def show(self):
        print('Queue : ',self.elements)
    
    def capacity(self):
        print(self.size)

if __name__ == '__main__':
    x = mQueue(5)
    x.push(1)
    x.push(5)
    x.seek()
    x.show()
    x.push(20)
    x.push(4)
    x.show()
    x.pop()
    x.show()