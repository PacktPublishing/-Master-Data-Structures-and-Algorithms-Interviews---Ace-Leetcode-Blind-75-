
// Definition for a binary tree node.
function TreeNode(val) {
    this.val = val;
    this.left = this.right = null;
}

var Codec = function() {};

// Encodes a tree to a single string.
Codec.prototype.serialize = function(root) {
    if (!root) {
        return "";
    }
    let queue = [root];
    let result = [];
    while (queue.length > 0) {
        let node = queue.shift();
        if (node) {
            result.push(node.val);
            queue.push(node.left);
            queue.push(node.right);
        } else {
            result.push("N");
        }
    }
    return result.join(",");
};

// Decodes your encoded data to tree.
Codec.prototype.deserialize = function(data) {
    if (!data) {
        return null;
    }
    let values = data.split(",");
    let root = new TreeNode(parseInt(values[0]));
    let queue = [root];
    let i = 1;
    while (queue.length > 0) {
        let node = queue.shift();
        if (values[i] !== "N") {
            node.left = new TreeNode(parseInt(values[i]));
            queue.push(node.left);
        }
        i++;
        if (values[i] !== "N") {
            node.right = new TreeNode(parseInt(values[i]));
            queue.push(node.right);
        }
        i++;
    }
    return root;
};
