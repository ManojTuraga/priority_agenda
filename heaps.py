class MaxHeap():
    def __init__(self):
        self._heap = []
        self._i = 0

    def add(self, value):
        self._heap.append(value)
        self._upheap(len(self._heap) - 1)

    def remove(self):
        if len(self._heap) != 0:
            value = self._heap[0]
            self._heap[0] = self._heap[-1]
            self._heap.pop(-1)
            self._downheap(0)

            return value

    def _upheap(self, index):
        if (index - 1)//2 >= 0 and self._heap[index] > self._heap[(index - 1) // 2]:
            temp = self._heap[(index - 1) // 2]
            self._heap[(index - 1) // 2] = self._heap[index]
            self._heap[index] = temp
            self._upheap((index - 1) // 2)

    def _downheap(self, index):
        left = (2 * index) + 1
        right = (2 * index) + 2

        try:
            child = left if self._heap[left] > self._heap[right] else right

        except:
            if (2 * index) + 2 < len(self._heap):
                child = (2 * index) + 2

            elif (2 * index) + 1 < len(self._heap):
                child = (2 * index) + 1

            else:
                child = None

        
        if child is not None and self._heap[index] < self._heap[child]:
            temp = self._heap[index]
            self._heap[index] = self._heap[child]
            self._heap[child] = temp

            self._downheap(child)

    def peek_root(self):
        try:
            return self._heap[0]

        except:
            raise RuntimeError("Heap is empty")

    def get_heap(self):
        return self._heap

    def set_heap(self, new_heap):
        self._heap = new_heap.get_heap()

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        if self._i < len(self._heap):
            cur, self._i = self._heap[self._i], self._i+1
            return cur

        self._i = 0
        raise StopIteration()
    def __str__(self):
        string = ''
        for item in self._heap:
            string += f";\t{item}"

        return string
            
