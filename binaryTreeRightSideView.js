function TreeNode(val, left, right)  {
    this.val = (val === undefined ? 0 : val)
    this.left = (left === undefined ? null : left)
    this.right = (right === undefined ? null : right)
}

/**
 * @param { TreeNode } root
 * @return { number[]}
 */
const rightSideView = (root) => {
    let result = []
    rightView(root, result, 0)
    return result
}

const rightView = (root, result, depth) => {
    if (root === null) {
        return
    }
    if (depth === result.length) {
        result.push(root.val)
    }
    rightView(root.right, result, depth + 1)
    rightView(root.left, result, depth + 1)
}

root = [1,2,3,null,5,null,4]
console.log(rightSideView(root))
