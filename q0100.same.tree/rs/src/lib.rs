use std::rc::Rc;
use std::cell::RefCell;
use leetcode_prelude::TreeNode;

struct Solution {}

impl Solution {
    pub fn is_same_tree(p: Option<Rc<RefCell<TreeNode>>>, q: Option<Rc<RefCell<TreeNode>>>) -> bool {
        match (p, q) {
            (None, None) => true,
            (Some(p), Some(q)) => {
                let p = p.borrow();
                let q = q.borrow();
                p.val == q.val
                    && Self::is_same_tree(p.left.clone(), q.left.clone())
                    && Self::is_same_tree(p.right.clone(), q.right.clone())
            }
            _ => false,
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use leetcode_prelude::btree;

    #[test]
    fn test_ex1() {
        let p = btree![1,2,3];
        let q = btree![1,2,3];

        let result = Solution::is_same_tree(p, q);
        let ans = true;

        assert_eq!(ans, result);
    }

    #[test]
    fn test_ex2() {
        let p = btree![1,2];
        let q = btree![1,None,2];

        let result = Solution::is_same_tree(p, q);
        let ans = false;

        assert_eq!(ans, result);
    }

    #[test]
    fn test_ex3() {
        let p = btree![1,2,1];
        let q = btree![1,1,2];

        let result = Solution::is_same_tree(p, q);
        let ans = false;

        assert_eq!(ans, result);
    }
}
