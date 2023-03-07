struct Solution {}

impl Solution {
    pub fn minimum_time(time: Vec<i32>, total_trips: i32) -> i64 {
        let min_time = *time.iter().min().unwrap();
        let (mut left, mut right) = (0,  total_trips as i64 * min_time as i64 + 1);

        while left < right {
            let mid = (left + right) / 2;
            let trip_count = time.iter().map(|&t| mid / t as i64).sum::<i64>();
            if trip_count < total_trips as i64 {
                left = mid + 1;
            }
            else {
                right = mid;
            }
        }
        left
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_ex1() {
        let time = vec![1,2,3];
        let total_trips = 5;
        let ans =  3;

        let result = Solution::minimum_time(time, total_trips);
        assert_eq!(result, ans);
    }

    #[test]
    fn test_ex2() {
        let time = vec![2];
        let total_trips = 1;
        let ans =  2;
        
        let result = Solution::minimum_time(time, total_trips);
        assert_eq!(result, ans);
    }
}
