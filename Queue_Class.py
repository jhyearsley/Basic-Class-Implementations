#Queue Class

class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self,val):
        return self.items.insert(0,val)

    def dequeue(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

def hot_potato(name_list,num):
    queue = Queue()
    [queue.enqueue(name) for name in name_list]

    while queue.size() > 1:
        for i in range(num):
            queue.enqueue(queue.dequeue())

        queue.dequeue()

    return queue.dequeue()
            
                
