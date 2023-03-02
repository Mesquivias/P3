class UnsortedArrayPQ:
    def __init__(self):
        self.queue = []
        self.empty = True

    # O(1) because you are appending an element to the end of a list
    def insert(self, priority, node):
        # Adds tuple with priority and node to the PQ
        self.queue.append((priority, node))
        # It is now not empty
        self.empty = False

    # O(n) because you are iterating over a list and worst case
    # it has to iterate over the entire thing.
    def decrease_key(self, new_priority, node):
        # Iterates over list and updates priority
        for i, (priority, n) in enumerate(self.queue):
            if n == node:
                self.queue[i] = (new_priority, n)

    # O(n) because you are iterating over a list and worst case
    # it has to iterate over the entire thing.
    def delete_min(self):
        # Initializes the min node and priority
        min_node = None
        min_priority = float('inf')
        # Finds the node with the lowest priority and updates
        for i, (priority, node) in enumerate(self.queue):
            if priority < min_priority:
                min_priority = priority
                min_node = node
        if min_node is not None:
            # Removes the node with the min priority
            self.queue.remove((min_priority, min_node))
            if not self.queue:
                self.empty = True
        return min_node

    # O(1) since it only returns the boolean flag.
    def is_empty(self):
        # Flag to see if list is empty.
        return self.empty

    # Total space complexity would be O(n) according to my review.
    # n is the number of elements in the queue
