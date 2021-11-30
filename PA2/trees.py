# Programming Assignment 2 - CS315
# Erin Maines - 912273694
# 27 October, 2021
import csv
import sys
import pdb

class TreeNode:
    def __init__(self, x):
        self.key = x
        self.left = None
        self.right = None

    def preOrder(self,node):
        if not node:
            return
        print(node.key)
        self.preOrder(node.left)
        self.preOrder(node.right)

    def postOrder(self,node):
        if not node:
            return
        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node.key)

    def inOrder(self,node):
        if not node:
            return
        self.inOrder(node.left)
        print(node.key)
        self.inOrder(node.right)
        
    # Function to insert a new node in BST
    def insert(self,node, key):
  
        # 1. If the tree is empty, return a new,     
        # single node
        if not node:
            return TreeNode(key)
  
        # 2. Otherwise, recur down the tree
        if key < node.key:
            node.left = self.insert(node.left, key)
        if key > node.key:
            node.right = self.insert(node.right, key)
      
        # return the (unchanged) node
        return node

    def search(self,root, key):
        if not root:
            return False
        elif root.key == key:
            return True
        elif root.key > key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)
        return (-1)

    def min(self,node):
        curr = node
        while (curr.left):
            curr = curr.left
        return curr.key

    def max(self,node):
        curr = node
        while (curr.right):
            curr = curr.right
        return curr.key


class Heap:
    def swap(array, a, b):
        array[a], array[b] = array[b], array[a]

    def create_max_heap(self, a):
        heap_size = len(a)
        start = heap_size //2 - 1
        for i in range(start, -1, 1):
            self.max_heapify(a, i, heap_size)
        return

    def max_heapify(self, heap, i, length):
        largest = i
        l = i*2+1
        r = i*2+2
        if l <= length and heap[l] > heap[largest]:
            largest = l
        if r <= length and heap[r] > heap[largest]:
            largest = r
        if largest != i:
            self.swap(heap, i, largest)
            self.max_heapify(heap, i, length)
        return

def array_to_bst(a):
    if a != None:
        if len(a) != 0:
            mid = len(a)//2
            node = TreeNode(a[mid])
            for i in a:
                node.insert(node, i)
           # node.left = array_to_bst(a[:mid])
           # node.right = array_to_bst(a[mid+1:])
            return node

def open_csv(file_name):
    master_list = []
    with open(file_name, newline='') as csv_file:
            unsorted_list = csv.reader(csv_file, delimiter=',', quotechar='|')
            for row in unsorted_list:
                master_list.append(int(row[0]))
    return master_list

def main():
    if sys.argv[1]:
        file_name = sys.argv[1]
        array = open_csv(file_name)
        bst = array_to_bst(array)
        
        print("Max Value", bst.max(bst))

        print("Min Value", bst.min(bst))

        print("In Order Traversal")
        bst.inOrder(bst)
        
        print("Pre Order Traversal")
        bst.preOrder(bst)

        print("Post Order Traversal")
        bst.postOrder(bst)

        option = input("Enter a search value: (-1 to quit): ")
        while int(option) != (-1):
            print(bst.search(bst, int(option)))
            option = input("Enter a search value: (-1 to quit): ")

if __name__ == "__main__":
    main()
