"""heap data structure from scratch"""

class heap:
    def __init__(self):
        self.heap = []
        self.el_count = 0
    def find_children(self, parent):
        child1 = (parent+1)*2-1
        child2 = (parent+1)*2
        return (child1, child2)
        
    def find_parent(self, child):
        return (child-1)//2
    def swap_el(ind1, ind2):
        self.heap[ind1], self.heap[ind2] = self.heap[ind2], self.heap[ind1]
    def heap_pop():
        self.swap_el(0,len(self.heap]-1)
        return_val = self.heap.pop()
        self.el_count -= 1
        #perlocate items down from the top of the heap
        parent = 0
        while parent< self.el_count:
            left_c, right_c = self.find_children(parent)
            if right_c < self.el_count - 1 and self.heap[parent]> self.heap[right_c]:
                swapper = right_c
            else if left_c <self.el_count -1 and self.heap[parent] > self.heap[left_c]:
                swapper = left_c
            else:
                swapper = self.el_count-1
            self.swap_el(parent, swapper)
            parent = swapper

        return return val
    def heap_add(val):
        self.heap.push(val)
        self.el_count += 1
        #perlocate up until no larger values above
        child = self.heap.el_count
        parent = self.find_parent(child)
        while self.heap[child]< self.heap[parent]:
            self.swap(child, parent)
            child = parent
            parent = self.find_parent(child)
    



        
        
    def add_el(self, el):
        self.heap.push(el)
