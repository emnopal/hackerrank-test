class BinaryTreeNode {
	constructor(data) {
		this.data = data;
		this.left = null;
		this.right = null;
	}

	insert(data) {
		if (this.data === data) {
			return;
		}
		if (data < this.data) {
			if (this.left) {
				this.left.insert(data);
			} else {
				this.left = new BinaryTreeNode(data);
			}
		} else {
			if (this.right) {
				this.right.insert(data);
			} else {
				this.right = new BinaryTreeNode(data);
			}
		}
	}

	find(data) {
		if (this.data === data) {
			return true;
		}
		if (data < this.data) {
			if (this.left) {
				return this.left.find(data);
			}
			return false;
		}
		if (this.right) {
			return this.right.find(data);
		}
		return false;
	}

	show(position) {
		if (this) {
			switch (position) {
				case "pre":
					console.log(this.data, " ");
					if (this.left) {
						this.left.show(position);
					}
					if (this.right) {
						this.right.show(position);
					}
					return;
				case "in":
					if (this.left) {
						this.left.show(position);
					}
					console.log(this.data, " ");
					if (this.right) {
						this.right.show(position);
					}
					return;
				case "post":
					if (this.left) {
						this.left.show(position);
					}
					if (this.right) {
						this.right.show(position);
					}
					console.log(this.data, " ");
					return;
				default:
					console.log(this.data, " ");
					if (this.left) {
						this.left.show(position);
					}
					if (this.right) {
						this.right.show(position);
					}
					return;
			}
		}
	}
}

class Tree {
	constructor() {
		this.root = null;
	}

	insert(data) {
		if (this.root) {
			this.root.insert(data);
		} else {
			this.root = new BinaryTreeNode(data);
		}
		return this;
	}

	find(data) {
		if (this.root) {
			return this.root.find(data);
		}
		return false;
	}

	show(position) {
		console.log(position, ": ");
		if (this.root) {
			this.root.show(position);
		}
		console.log();
	}
}

const main = () => {
	const arr = [10, 12, 5, 4, 20, 8, 7, 15, 13];
	const tree = new Tree();

	arr.forEach((i) => {
		tree.insert(i);
	});

	console.log(tree.find(1));
	console.log(tree.find(12));
	tree.show("pre");
	tree.show("in");
	tree.show("post");
}

main();
