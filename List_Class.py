#List Class

class Node(object):
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    
class UnorderedList(object):
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, data):
        temp = Node(data)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            current = current.get_next()
            count += 1

        return count

    def search(self, item):
        found = False
        current = self.head

        while not found and current is not None:
            if current.get_data() == item:
                found = True

            current = current.get_next()

        return found
            
    def remove(self, item):
        found = False
        current = self.head
        previous = None

        while not found:
            if current.get_data() == item:
                found = True

            else:
                current, previous = current.get_next(), current

        if previous is None:
            self.head = current.get_next()

        else:
            previous.set_next(current.get_next())

    def append(self, item):
        at_end = False
        current = self.head
        data = Node(item)

        while not at_end:
            if current.get_next() is None:
                at_end = True

            else:
                current = current.get_next()

        current.set_next(data)



    def __str__(self):
        string = '['
        current = self.head
        for i in range(self.size()-1):
            string = string + str(current.get_data()) + ','
            current = current.get_next()

        string += str(current.get_data()) + ']'

        return string

a = UnorderedList()
a.add(5)
a.add(4)
a.add(6)

        
