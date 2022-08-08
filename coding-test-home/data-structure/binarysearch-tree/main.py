class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self, root):
        self.root = root
        
    def insert(self, value):
        self.current_node = self.root
        while True:
            if value < self.current_node.value:
                # 왼쪽
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.letf = Node(value=value)
                    break
            else:
                # 오른쪽
                if self.current_node.right != None:
                    # 현재 노드를 바꾸고 다시 비교해야하니 current node의 위치를 right로 바꿔줌
                    self.current_node = self.current_node.right 
                else:
                    self.current_node.right = Node(value=value)
                    break
    
    def search(self, value):
        self.current_node = self.root
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif self.current_node.value > value:
                # current node가 더 크기 때문에 찾고자 하는 value는 왼쪽으로
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False
    
    def delete(self, value):
        self.current_node = self.root
        self.parent_node = self.root
        
        # case 1 삭제하고자 하는 노드가 Leef Node 
        # case 2 삭제하고자 하는 노드의 자식 node 가 1개
        # case 2-1 삭제하고자 하는 노드의 자식 node가 1개인데 1개가 왼쪽에 있을 때
        # case 2-2 삭제하고자 하는 노드의 자식 node가 1개인데 1개가 오른쪽에 있을 때
        # case 3 삭제하고자 하는 노드의 자식 node가 2개일 떄