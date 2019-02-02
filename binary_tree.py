class Node:
    """ represents a node of a binary tree, which contain some sort of data, and left and right children"""
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def from_bt_to_ordered_string(root, tree_string=''):
    """expect a root of a binary tree, and returns the tree as an ascending order string"""
    if root.left:
        tree_string = from_bt_to_ordered_string(root.left, tree_string)
    if root.right:
        tree_string += root.data
        tree_string = from_bt_to_ordered_string(root.right, tree_string)
    else:
        tree_string += root.data
    return tree_string


def serialize(root, tree_string=''):
    """
    converts a binary tree into a string on which the children of the leaves are represented as '-1'. the order of the
    string is the order on which we visit each node through a traverse on which we always pick the left child first.
    """
    if root is None:
        return tree_string + '-1 '
    tree_string += root.data + ' '
    tree_string = serialize(root.left, tree_string)
    tree_string = serialize(root.right, tree_string)

    return tree_string


def deserialize(string, index=0):
    """
    converts a string of the kind serialize makes, into the same original tree. the function returns the root of this
    tree
    """
    data = ''
    for ind in range(index, len(string)):
        index += 1
        char = string[ind]
        if char == ' ':
            break
        data += char
    if data == '-1':
        return None, index

    node = Node(data)
    node.left, index = deserialize(string, index)
    node.right, index = deserialize(string, index)
    print(node.data, node.left, node.right)
    return node, index


def deserialize_better(string):
    """ the same as the above only slight better"""
    node_list = string.split(' ')
    index = [0]

    def deserialize_rec():
        data = node_list[index[0]]
        index[0] += 1
        if data == '-1':
            return None
        node = Node(data)
        node.left = deserialize_rec()
        node.right = deserialize_rec()
        return node

    return deserialize_rec()


def bt_into_list(root):
    """
    expects a complete binary tree, and return a list on which the root is list[0], and the left child of the node in
    list[i] is in list[2 * i + 1], and right child is in list[2 * (i+1)].
    if the tree is incomplete binary tree it returns the order of all the node, by levels (without the above index rule)
    """
    tree_list = []
    node_queue = [root]
    queue_index = 0

    while queue_index < len(node_queue):
        node = node_queue[queue_index]
        queue_index += 1
        tree_list.append(node.data)
        if node.left:
            node_queue.append(node.left)
        if node.right:
            node_queue.append(node.right)
    return tree_list


def bt_into_str(root):
    """
    expects a complete binary tree, and returns a string on which the root is list[0], and the left child of the node in
    list[i] is in list[2 * i + 1], and right child is in list[2 * (i+1)].
    if the tree is incomplete binary tree it returns the order of all the node, by levels (without the above index rule)
    """
    return ''.join(bt_into_list(root))



