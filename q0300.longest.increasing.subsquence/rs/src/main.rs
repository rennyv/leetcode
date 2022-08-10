fn main() {
    let s = vec![1,2,3];
    let ans = length_of_lis(s);

    println!("length of Longest Increasing Subsequence is {}", ans);
}

pub fn length_of_lis(nums: Vec<i32>) -> i32 {
    let nums_length = nums.len();

    let mut dp: Vec<i32> = vec![1; nums_length];
    let mut longest: i32 = 1;

    for high in 1..nums_length{
        for low in 0..high{
            if nums[low] < nums[high]{
                dp[high] = std::cmp::max(dp[high], dp[low] +1)
            }
        }

        longest = std::cmp::max(longest, dp[high])
    }

    longest
}


#[cfg(test)]
mod length_of_lis_tests {    
    use super::*;

    #[test]
    fn test_1() {
        let nums = vec![10,9,2,5,3,7,101,18];
        let ans = 4;
        assert_eq!(length_of_lis(nums), ans);
    }
    
    #[test]
    fn test_2() {
        let nums = vec![0,1,0,3,2,3];
        let ans = 4;
        assert_eq!(length_of_lis(nums), ans);
    }

    #[test]
    fn test_3() {
        let nums = vec![7,7,7,7,7,7];
        let ans = 1;
        assert_eq!(length_of_lis(nums), ans);
    }
}