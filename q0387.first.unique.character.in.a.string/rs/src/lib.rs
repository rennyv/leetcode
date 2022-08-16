struct Solution {}

use std::collections::HashMap;

impl Solution {
    pub fn first_uniq_char(s: String) -> i32 {
        let mut h_m:HashMap<char,i32> = HashMap::new();

        for i in s.chars() {
            *h_m.entry(i).or_insert(0) += 1;
        }

        for (i,v) in s.chars().enumerate(){
            if h_m.get(&v).unwrap() == &1{
                return i as i32
            }
        }

        -1
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        let s = String::from("leetcode");

        let result = 0;
        assert_eq!(result, Solution::first_uniq_char(s));
    }

    #[test]
    fn test_2() {
        let s = String::from("loveleetcode");

        let result = 2;
        assert_eq!(result, Solution::first_uniq_char(s));
    }

    #[test]
    fn test_3() {
        let s = String::from("aabb");

        let result = -1;
        assert_eq!(result, Solution::first_uniq_char(s));
    }
}
