struct Solution {}

use std::collections::HashMap;

impl Solution {
    pub fn is_possible(nums: Vec<i32>) -> bool {
        let mut freq = HashMap::<i32,i32>::new();
        let mut append_freq = HashMap::<i32,i32>::new();

        for &i in &nums{
            *freq.entry(i).or_default() += 1;
        }

        for &i in &nums {
            if *freq.get(&i).unwrap() == 0 {
                continue;
            } else if *append_freq.get(&i).or(Some(&0)).unwrap() > 0 {
                *append_freq.entry(i).or_default() -= 1;
                *append_freq.entry(i + 1).or_default() += 1;
            } else if *freq.get(&(i + 1)).or(Some(&0)).unwrap() > 0
                && *freq.get(&(i + 2)).or(Some(&0)).unwrap() > 0
            {
                *freq.entry(i + 1).or_default() -= 1;
                *freq.entry(i + 2).or_default() -= 1;
                *append_freq.entry(i + 3).or_default() += 1;
            } else {
                return false;
            }
            *freq.entry(i).or_default() -= 1;
        }
        true

    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        let nums = vec![1,2,3,3,4,5];

        assert_eq!(Solution::is_possible(nums), true);
    }

    
    #[test]
    fn test_2() {
        assert_eq!(Solution::is_possible(vec![1, 2, 3, 3, 4, 4, 5, 5]), true)
    }

    #[test]
    fn test_3() {
        assert_eq!(Solution::is_possible(vec![1, 2, 3, 4, 4, 5]), false)
    }
}
