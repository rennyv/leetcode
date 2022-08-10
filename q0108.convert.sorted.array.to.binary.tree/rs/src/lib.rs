use leetcode_prelude::TreeNode;

use std::rc::Rc;
use std::cell::RefCell;

struct Solution {}

impl Solution {
    pub fn sorted_array_to_bst(nums: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        match nums.len() {
            0 => None,
            _ => Solution::create_bst(nums.as_slice())
        }
    }

    fn create_bst(nums: &[i32]) -> Option<Rc<RefCell<TreeNode>>> {
        let length = nums.len();
        let mid = length / 2;
        let mut node = TreeNode::new(nums[mid]);
        if mid > 0 {
            node.left = Solution::create_bst(&nums[0..mid]);
        }
        if mid +1 < length {
            node.right = Solution::create_bst(&nums[(mid+1..)]);
        }

        Some(Rc::new(RefCell::new(node)))
    }
}

#[cfg(test)]
mod tests {
    use leetcode_prelude::btree;

    use super::*;

    #[test]
    fn test_1() {
        let nums = vec![-10,-3,0,5,9];
        let ans = Solution::sorted_array_to_bst(nums);

        assert_eq!(ans, btree![0,-3,9,-10,null,5]);
    }

    #[test]
    fn test_2() {
        let nums = vec![1,3];
        let ans = Solution::sorted_array_to_bst(nums);

        assert_eq!(ans, btree![3,1]);
    }
}
