#!/usr/bin/python3


from CS4412Graph import *
import time
import BinaryHeapPQ
import UnsortedArrayPQ


class NetworkRoutingSolver:
    def __init__(self):
        pass

    def initializeNetwork(self, network):
        assert (type(network) == CS4412Graph)
        self.network = network

    # O(n) where n is the number of list items
    def getShortestPath(self, destIndex):
        node = self.network.nodes[destIndex]
        path_edges = []
        total_length = node.distance

        # If the total length is infinity, there is no path to the destination.
        if total_length == float('inf'):
            return {'cost': total_length, 'path': path_edges}

        # Backtrack from destination to source while there is a predecessor.
        while node.predecessor is not None:
            edge = node.predecessor
            # Add the path to the path_edges list
            path_edges.append((edge.src.loc, edge.dest.loc, '{:.0f}'.format(edge.length)))
            node = edge.src
        # Reverses the path_edges list to get the path in the right order.
        path_edges.reverse()

        return {'cost': total_length, 'path': path_edges}

    # O(nlogn)?
    def computeShortestPaths(self, source, use_heap=False):
        self.source = source
        t1 = time.time()

        # Set the distance to infinity and all nodes to no predecessors.
        for node in self.network.nodes:
            node.distance = float('inf')
            node.predecessor = None

        # Set the source node distance
        self.network.nodes[self.source].distance = 0

        # If the variable 'use_heap' is true, use binaryheap. Else, array.
        if use_heap:
            pq = BinaryHeapPQ.BinaryHeapPQ()
        else:
            pq = UnsortedArrayPQ.UnsortedArrayPQ()

        pq.insert(self.network.nodes[self.source].distance, self.network.nodes[self.source])

        # Dijkstra's algorithm
        queue_empty = False
        while not queue_empty:
            # Delete the nod with the min distance from PQ
            node = pq.delete_min()

            # Iterates over the neighbor nodes
            for edge in node.neighbors:
                neighbor = edge.dest
                # Calculates new distance to the neighbor node.
                new_distance = node.distance + edge.length

                # If the new distance is smaller, use that one.
                if new_distance < neighbor.distance:
                    neighbor.distance = new_distance
                    neighbor.predecessor = edge

                    # Adds the node to the PQ if it is not there.
                    if neighbor not in pq.queue:
                        pq.insert(neighbor.distance, neighbor)

            # Check is the PQ is empty
            queue_empty = pq.is_empty()

        # Returns the time taken
        t2 = time.time()
        return t2 - t1
