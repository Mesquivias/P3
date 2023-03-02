class BinaryHeapPQ:
    def __init__(self):
        self.queue = [(float('inf'), None)]
        # Keeps track of node position
        self.node_positions = {}
        self.empty = True

    # Inserts node into PQ
    # O(logn) since we are dealing with a tree and bubble_up is called
    def insert(self, priority, node):
        # Appends node to end of queue and updates position
        self.queue.append((priority, node))
        self.node_positions[node] = len(self.queue) - 1
        # Bubbles the node up to correct position.
        self.bubble_up(len(self.queue) - 1)
        self.empty = False

    # O(logn) since we are dealing with a tree and bubble_up is called
    def decrease_key(self, new_priority, node):
        # Returns if there is no node
        if node not in self.node_positions:
            return
        # Gets position and old priority
        pos = self.node_positions[node]
        old_priority, _ = self.queue[pos]
        # Updates priority and bubbles up if it is less than the old priority.
        self.queue[pos] = (new_priority, node)
        if new_priority < old_priority:
            self.bubble_up(pos)
        else:
            self.sift_down(pos)
        self.empty = False

    # O(logn) since we are dealing with a tree
    def delete_min(self):
        # Returns none is queue is empty
        if self.empty:
            return None

        # Finds the min node and deletes it.
        min_node = self.queue[1][1]
        last_node = self.queue.pop()[1]
        del self.node_positions[min_node]
        # Updates first node position and replaces the min node with last node
        if len(self.queue) > 1:
            self.node_positions[self.queue[1][1]] = 1
            self.queue[1] = (self.queue[-1][0], last_node)
            self.sift_down(1)
        else:
            self.empty = True
        return min_node

    # Gets the position of the parent node and swaps if is has a higher priority
    # O(logn) since we are dealing with a tree
    def bubble_up(self, pos):
        parent_pos = pos // 2
        while pos > 1 and self.queue[parent_pos][0] > self.queue[pos][0]:
            self.node_positions[self.queue[pos][1]] = parent_pos
            self.node_positions[self.queue[parent_pos][1]] = pos
            self.queue[parent_pos], self.queue[pos] = self.queue[pos], self.queue[parent_pos]
            pos = parent_pos
            parent_pos = pos // 2

    # Moves node down heap by swapping it with child until it is in correct position
    # O(logn) since we are dealing with a tree, n is the size of heap.
    def sift_down(self, pos):
        while True:
            # Calculate where left and right child are
            left_child_pos = 2 * pos
            right_child_pos = 2 * pos + 1
            # Compare left and right child nodes to find smaller priority
            if right_child_pos < len(self.queue):
                if self.queue[left_child_pos][0] <= self.queue[right_child_pos][0]:
                    min_child_pos = left_child_pos
                else:
                    min_child_pos = right_child_pos
            # Chooses left child if there is no right one.
            elif left_child_pos < len(self.queue):
                min_child_pos = left_child_pos
            # Will break if there are no children nodes.
            else:
                break
            # If the priority of the min child < current position
            # Swap those two nodes and update their positions
            if self.queue[min_child_pos][0] < self.queue[pos][0]:
                self.node_positions[self.queue[pos][1]] = min_child_pos
                self.node_positions[self.queue[min_child_pos][1]] = pos
                self.queue[pos], self.queue[min_child_pos] = self.queue[min_child_pos], self.queue[pos]
                pos = min_child_pos
            # Otherwise, break.
            else:
                break
        # Will set empty to true if it contains only one node
        if len(self.queue) == 1:
            self.empty = True

    # O(1) since it only returns the boolean flag.
    def is_empty(self):
        return self.empty

    # Space complexity would be on O(n) since there are n items.
