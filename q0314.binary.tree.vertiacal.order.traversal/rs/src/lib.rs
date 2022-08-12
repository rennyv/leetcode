use leetcode_prelude::TreeNode;

struct Solution {}

use std::collections::hash_map::Entry::{Occupied, Vacant};
use std::collections::{VecDeque, HashMap};
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn vertical_order(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
        let mut min = 0;
        let mut max = 0;
        let mut q = VecDeque::new();
        let mut map: HashMap<i32, Vec<i32>> = HashMap::new();
        
        if let Some(cur) = root {
            q.push_back((cur.clone(), 0));
        }

        loop {
            if q.len() == 0 {
                break;
            } else {
                // get node and index
                let (cur, ind) = q.pop_front().unwrap();
                
                //update max and min indexes
                if ind < min {
                    min = ind;
                }
                if ind > max {
                    max = ind;
                }
                let x = cur.borrow();

                //add val to the hashmap
                match map.entry(ind) {
                    Vacant(e) => {
                        e.insert(vec![x.val]);
                    }
                    Occupied(mut e) => {
                        e.get_mut().push(x.val);
                    }
                }

                //append left/right node to queue
                if let Some(left) = &x.left {
                    q.push_back((left.clone(), ind - 1));
                }
                if let Some(right) = &x.right {
                    q.push_back((right.clone(), ind + 1));
                }
            }
        }

        //clean up ans
        let mut ans = vec![];
        let min_abs = min.abs();
        for i in 0..=(max+min_abs) {
            if let Some(vals) = map.get(&(i - min_abs)){
                ans.push(vals.to_owned());
            }
        }
        ans
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use leetcode_prelude::btree;

    #[test]
    fn test_1() {
        let root = btree![3,9,20,null,null,15,7];
        let ans = vec![vec![9], vec![3,15], vec![20], vec![7]];
        assert_eq!(ans, Solution::vertical_order(root));
    }

    #[test]
    fn test_2() {
        let root = btree![3,9,8,4,0,1,7];
        let ans = vec![vec![4], vec![9], vec![3,0,1], vec![8], vec![7]];
        assert_eq!(ans, Solution::vertical_order(root));
    }

    #[test]
    fn test_3() {
        let root = btree![3,9,8,4,0,1,7,null,null,null,2,5];
        let ans = vec![vec![4], vec![9,5], vec![3,0,1], vec![8,2], vec![7]];
        assert_eq!(ans, Solution::vertical_order(root));
    }
}
