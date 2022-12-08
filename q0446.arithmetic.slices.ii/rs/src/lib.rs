struct Solution {}

use std::{collections::HashMap};

impl Solution {
    pub fn number_of_arithmetic_slices(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut ans = 0;
        let mut dp = vec!{};

        for _ in 0..n{
            dp.append(HashMap::new())
        }

        for i in 1..nums.len(){
            for j in 0..i {
                let diff = nums[i] - nums[j];
                let mut cnt = 0;
                if dp[j].contains(diff){
                    cnt = dp[j][diff]
                }
                dp[i][diff] += cnt +1;
                ans += cnt
            }
        }

        return ans
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_ex1() {
        let nums = vec![2,4,6,7,10];
        let ans = 7;
        
        let result = Solution::number_of_arithmetic_slices(nums);
        assert_eq!(result, ans);
    }

    #[test]
    fn test_ex2() {
        let nums = vec![7,7,7,7,7];
        let ans = 16;
        
        let result = Solution::number_of_arithmetic_slices(nums);
        assert_eq!(result, ans);
    }
}
