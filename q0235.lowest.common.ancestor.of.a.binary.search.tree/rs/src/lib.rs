use leetcode_prelude::TreeNode;

struct Solution {}

use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn lowest_common_ancestor(
        root: Option<Rc<RefCell<TreeNode>>>, 
        p: Option<Rc<RefCell<TreeNode>>>, 
        q: Option<Rc<RefCell<TreeNode>>>
    ) -> Option<Rc<RefCell<TreeNode>>> {
        let p_val = p.unwrap().borrow().val;
        let q_val = q.unwrap().borrow().val;
        let mut root = root;
        let mut res = None;

        while let Some(node) = root {
            let mut n = node.borrow_mut();
            res = Some(Rc::new(RefCell::new(TreeNode::new(n.val))));
            if n.val > p_val && n.val > q_val {
                root = n.left.take();
                continue;
            }
            if n.val < p_val && n.val < q_val {
                root = n.right.take();
                continue;
            }
            break;
        }
        res
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use leetcode_prelude::btree;

    #[test]
    fn test_1() {
        let root = btree![6,2,8,0,4,7,9,null,null,3,5];
        let p = btree![2];
        let q = btree![8];
        let result = Solution::lowest_common_ancestor(root, p, q);
        assert_eq!(result, btree![6]);
    }

    #[test]
    fn test_2() {
        let root = btree![6,2,8,0,4,7,9,null,null,3,5];
        let p = btree![2];
        let q = btree![4];
        let result = Solution::lowest_common_ancestor(root, p, q);
        assert_eq!(result, btree![2]);
    }

    #[test]
    fn test_3() {
        let root = btree![2,1];
        let p = btree![2];
        let q = btree![1];
        let result = Solution::lowest_common_ancestor(root, p, q);
        assert_eq!(result, btree![2]);
    }
}
