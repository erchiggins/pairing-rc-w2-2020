import unittest


def is_binary_search_tree(root):

    if root.left:
        largest_left = find_largest(root.left)
        if largest_left > root.value:
            return False

    if root.right:
        smallest_right = find_smallest(root.right)
        if smallest_right < root.value:
            print(smallest_right)
            return False

    return True


def find_largest(root):
    largest = root.value

    if root.right:
        largest_right = find_largest(root.right)
        if largest_right > largest:
            largest = largest_right

    if root.left:
        largest_left = find_largest(root.left)
        if largest_left > largest:
            largest = largest_left

    return largest


def find_smallest(root):

    print(root.value)
    smallest = root.value

    if root.right:
            smallest_right = find_smallest(root.right)
            if smallest_right < smallest:
                smallest = smallest_right

    if root.left:
        smallest_left = find_smallest(root.left)
        if smallest_left < smallest:
            smallest = smallest_left

    return smallest


# Tests

class Test(unittest.TestCase):

    class BinaryTreeNode(object):

        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def insert_left(self, value):
            self.left = Test.BinaryTreeNode(value)
            return self.left

        def insert_right(self, value):
            self.right = Test.BinaryTreeNode(value)
            return self.right

    def test_valid_full_tree(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(70)
        left.insert_left(10)
        left.insert_right(40)
        right.insert_left(60)
        right.insert_right(80)
        result = is_binary_search_tree(tree)
        self.assertTrue(result)

    def test_both_subtrees_valid(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(80)
        left.insert_left(20)
        left.insert_right(60)
        right.insert_left(70)
        right.insert_right(90)
        result = is_binary_search_tree(tree)
        self.assertFalse(result)

    def test_descending_linked_list(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(40)
        left_left = left.insert_left(30)
        left_left_left = left_left.insert_left(20)
        left_left_left.insert_left(10)
        result = is_binary_search_tree(tree)
        self.assertTrue(result)

    def test_out_of_order_linked_list(self):
        tree = Test.BinaryTreeNode(50)
        right = tree.insert_right(70)
        right_right = right.insert_right(60)
        right_right.insert_right(80)
        result = is_binary_search_tree(tree)
        self.assertFalse(result)

    def test_one_node_tree(self):
        tree = Test.BinaryTreeNode(50)
        result = is_binary_search_tree(tree)
        self.assertTrue(result)


unittest.main(verbosity=2)
