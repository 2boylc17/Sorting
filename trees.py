class Queue:
    def __init__(self, capacity):
        self.internalArray = [None] * capacity
        self.front = 0
        self.back = 0
        self.capacity = capacity

    def add(self, item):
        if self.internalArray[self.back] is not None:
            print("Queue is full")
        else:
            self.internalArray[self.back] = item
            self.back = self.back + 1
            if self.back == self.capacity:
                self.back = 0
            print(f"Added {item} to queue")
        pass

    def remove(self):
        if self.internalArray[self.front] is not None:
            removed = self.internalArray[self.front]
            self.internalArray[self.front] = None
            self.front = self.front + 1
            if self.front == self.capacity:
                self.front = 0
            return removed
        pass

    def __str__(self):
        return self.internalArray.__str__()


class TreeNode:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None

    # insert() method of TreeNode
    def insert(self, new_value):

        if new_value < self.value:

            if self.left is None:
                self.left = TreeNode(new_value)
            else:  # not None
                self.left.insert(new_value)
        elif new_value > self.value:
            if self.right is None:
                self.right = TreeNode(new_value)
            else:  # not None
                self.right.insert(new_value)


class BinaryTree:
    def __init__(self):
        self.root = None

    # inserts a new node into the Tree
    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            # calling the insert() method of TreeNode
            self.root.insert(value)

    # initially, starting_node will be the root node.
    def print_tree(self, starting_node):
        if starting_node.left is not None:
            self.print_tree(starting_node.left)
        print(starting_node.value)
        if starting_node.right is not None:
            self.print_tree(starting_node.right)

    def depth_search(self, search_node, starting_node):
        if starting_node is None:
            print(f"Not found")
            return
        if starting_node.value == search_node:
            print(f"Found {search_node}")
            return
        elif starting_node.value > search_node:
            self.depth_search(search_node, starting_node.left)
        elif starting_node.value < search_node:
            self.depth_search(search_node, starting_node.right)

    def breadth_searchh(self, search_node, starting_node, queue):
        if starting_node.value is None:
            print(f"Not found")
            return
        if starting_node.value == search_node:
            print(f"Found {search_node}")
            return
        else:
            if starting_node.left.value is not None:
                queue.add(starting_node.left)
            if starting_node.right.value is not None:
                queue.add(starting_node.right)
            print(queue)
            self.breadth_search(search_node, queue.front, queue)

    def breadth_search(self, search_node, starting_node, queue):
        found = False
        queue.add(starting_node)
        while found is False:
            cur_value = queue.remove()
            if cur_value == search_node:
                print(f"Found {search_node}")
                found = True
                return
            else:
                if cur_value.left is not None:
                    queue.add(starting_node.left)
                if cur_value.right is not None:
                    queue.add(starting_node.right)
            print(queue)

    # Week 8 exercises: implement breadth-first and depth-first
    # searches on the tree. For depth-first, you can assume the tree is
    # sorted.


# Main program
tree = BinaryTree()
tree.insert(444)
tree.insert(222)
tree.insert(666)
tree.insert(111)
tree.insert(333)
tree.insert(777)
tree.insert(555)
tree.print_tree(tree.root)
new_queue = Queue(20)
tree.depth_search(444, tree.root)
tree.breadth_search(444, tree.root, new_queue)
