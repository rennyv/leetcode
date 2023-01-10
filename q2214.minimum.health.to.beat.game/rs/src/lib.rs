struct Solution {}

use std::cmp;

impl Solution {
    pub fn minimum_health(damage: Vec<i32>, armor: i32) -> i64 {
        let mut health: i64 = 0;
        let mut max_hit = 0;

        for n in damage {
            health += n as i64;
            max_hit = cmp::max(max_hit, n);
        }

        let protected = cmp::min(armor, max_hit) as i64;
        return health - protected + 1;
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_ex1() {
        let damage = vec![2,7,4,3];
        let armor = 4;
        let ans = 13;
        let result = Solution::minimum_health(damage, armor);
        assert_eq!(result, ans);
    }

    #[test]
    fn test_ex2() {
        let damage = vec![2,5,3,4];
        let armor = 7;
        let ans = 10;
        let result = Solution::minimum_health(damage, armor);
        assert_eq!(result, ans);
    }

    #[test]
    fn test_ex3() {
        let damage = vec![3,3,3];
        let armor = 0;
        let ans = 10;
        let result = Solution::minimum_health(damage, armor);
        assert_eq!(result, ans);
    }
}
