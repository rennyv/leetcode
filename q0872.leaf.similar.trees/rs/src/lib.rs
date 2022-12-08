use leetcode_prelude::TreeNode;

struct Solution {}

use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn leaf_similar(root1: Option<Rc<RefCell<TreeNode>>>, root2: Option<Rc<RefCell<TreeNode>>>) -> bool {
        fn collect_leaves(n: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
            match n {
                None => vec![],
                Some(n) => {
                    if n.borrow().left.is_none() && n.borrow().right.is_none() {
                        return vec![n.borrow().val];
                    }
                    let mut list = collect_leaves(n.borrow().left.clone());
                    list.extend(collect_leaves(n.borrow().right.clone()));
                    list
                }
            }
        }
        collect_leaves(root1) == collect_leaves(root2)
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use leetcode_prelude::btree;

    #[test]
    fn test_ex1() {
        let root1 = btree![3,5,1,6,2,9,8,null,null,7,4];
        let root2 = btree![3,5,1,6,7,4,2,null,null,null,null,null,null,9,8];
        
        let result = Solution::leaf_similar(root1, root2);
        assert_eq!(result, true);
    }

    #[test]
    fn test_ex2() {
        let root1 = btree![1,2,3];
        let root2 = btree![1,3,2];
        
        let result = Solution::leaf_similar(root1, root2);
        assert_eq!(result, false);
    }
}
