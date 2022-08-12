use leetcode_prelude::TreeNode;

struct Solution {}


use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn is_valid_bst(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        return Self::_validate(&root, i64::MIN, i64::MAX)
    }

    fn _validate(node: &Option<Rc<RefCell<TreeNode>>>, min: i64, max: i64) -> bool {
        if let Some(n) = node {
            let v = n.as_ref().borrow().val as i64;

            if v <= min || v >= max { return false; }

            Self::_validate(&n.as_ref().borrow().left, min, v) &&
                Self::_validate(&n.as_ref().borrow().right, v, max)
        } else {
            true
        }
    }
}


#[cfg(test)]
mod tests {
    use super::*;
    use leetcode_prelude::btree;

    #[test]
    fn test_1() {
        let root = btree![2,1,3];

        let result = Solution::is_valid_bst(root);
        assert_eq!(true, result);
    }

    #[test]
    fn test_2(){
        let root = btree![5,1,4,null,null,3,6];

        let result = Solution::is_valid_bst(root);
        assert_eq!(false, result);
    }
}
