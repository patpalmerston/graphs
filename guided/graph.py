
    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Check if the node has been visited
        # If not...
            # Mark it as visited
            # Call dft_recursive on each neighbor

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a queue
        # Enqueue A PATH TO the starting vertex
        # Create a set to store visited vertices
        # While the queue is not empty...
            # Dequeue the first PATH
            # GRAB THE VERTEX FROM THE END OF THE PATH
            # Check if it's been visited
            # If it hasn't been visited...
                # Mark it as visited
                # CHECK IF IT'S THE TARGET
                    # IF SO, RETURN THE PATH
                # Enqueue A PATH TO all it's neighbors
                    # MAKE A COPY OF THE PATH
                    # ENQUEUE THE COPY


