// Node class for our binary tree
class TreeNode {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

// Binary Search Tree class with insert and traversal methods
class BinarySearchTree {
  constructor() {
    this.root = null;
  }

  insert(value) {
    const newNode = new TreeNode(value);
    if (this.root === null) {
      this.root = newNode;
      return;
    }
    let current = this.root;
    while (true) {
      if (value < current.value) {
        if (current.left === null) {
          current.left = newNode;
          return;
        }
        current = current.left;
      } else {
        if (current.right === null) {
          current.right = newNode;
          return;
        }
        current = current.right;
      }
    }
  }

  // Breadth-First Search
  bfs() {
    const data = [];
    const queue = [];
    let node = this.root;
    if (!node) return data;

    queue.push(node);

    while (queue.length) {
      node = queue.shift();
      data.push(node.value);

      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }
    return data;
  }

  // Depth-First Search: Preorder (root → left → right)
  dfsPreorder() {
    const data = [];
    function traverse(node) {
      if (!node) return;
      data.push(node.value);
      traverse(node.left);
      traverse(node.right);
    }
    traverse(this.root);
    return data;
  }

  // Depth-First Search: Inorder (left → root → right)
  dfsInorder() {
    const data = [];
    function traverse(node) {
      if (!node) return;
      traverse(node.left);
      data.push(node.value);
      traverse(node.right);
    }
    traverse(this.root);
    return data;
  }

  // Depth-First Search: Postorder (left → right → root)
  dfsPostorder() {
    const data = [];
    function traverse(node) {
      if (!node) return;
      traverse(node.left);
      traverse(node.right);
      data.push(node.value);
    }
    traverse(this.root);
    return data;
  }
}

// Example: Build a tree and traverse it
const bst = new BinarySearchTree();
[10, 6, 15, 3, 8, 20].forEach(num => bst.insert(num));

console.log('BFS:', bst.bfs());               // e.g., [10, 6, 15, 3, 8, 20]
console.log('DFS Preorder:', bst.dfsPreorder());   // e.g., [10, 6, 3, 8, 15, 20]
console.log('DFS Inorder:', bst.dfsInorder());     // e.g., [3, 6, 8, 10, 15, 20]
console.log('DFS Postorder:', bst.dfsPostorder()); // e.g., [3, 8, 6, 20, 15, 10]
