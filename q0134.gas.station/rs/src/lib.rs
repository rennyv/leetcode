struct Solution {}

impl Solution {
    pub fn can_complete_circuit(gas: Vec<i32>, cost: Vec<i32>) -> i32 {
        let (mut fill, mut lack, mut spot, n) = (0, 0, 0, gas.len());
        for (i, (gas, cost)) in gas.into_iter().zip(cost.into_iter()).enumerate() {
            fill += gas - cost;
            if fill < 0 {
                lack += fill;
                fill = 0;
                spot = (i + 1) % n;
            }
        }
        if fill + lack >= 0 { spot as i32 } else { -1 }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_ex1() {
        let gas = vec![1,2,3,4,5];
        let cost = vec![3,4,5,1,2];
     
        let ans = 3;

        let result = Solution::can_complete_circuit(gas, cost);
        assert_eq!(result, ans);
    }

    #[test]
    fn test_ex2() {
        let gas = vec![2,3,4];
        let cost = vec![3,4,3];
     
        let ans = -1;

        let result = Solution::can_complete_circuit(gas, cost);
        assert_eq!(result, ans);
    }
}
