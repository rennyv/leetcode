struct Solution {}

use std::cmp;

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut do_nothing= 0;
        let mut holding = i32::MIN;
        let mut sold = 0;

        for price in prices.iter() {
            let prev_do_nothing = do_nothing;
            do_nothing = cmp::max(do_nothing, sold);
            sold = holding + price;
            holding = cmp::max(holding, prev_do_nothing-price)
        }

        return cmp::max(sold, do_nothing)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn text_ex1() {
        let prices = vec![1,2,3,0,2];
        let ans = 3;

        let result = Solution::max_profit(prices);
        assert_eq!(result, ans);
    }

    #[test]
    fn text_ex2() {
        let prices = vec![1];
        let ans = 0;
        
        let result = Solution::max_profit(prices);
        assert_eq!(result, ans);
    }
}
