fn main() {
    let v = vec![1,2,3,4];

    println!("{}", search(v, 2));
}

pub fn search(nums: Vec<i32>, target: i32) -> i32 {
    use std::cmp::Ordering;
    let (mut left, mut right) = (0, nums.len());

    while left < right {
        let mid = left + (right - left) / 2;
        match nums[mid].cmp(&target) {
            Ordering::Equal => return mid as i32,
            Ordering::Less => left = mid + 1,
            Ordering::Greater => right = mid,
        }
    }
    -1
}


#[cfg(test)]
mod add_digits_tests {    
    use super::*;
    
    #[test]
    fn test_1() {
        let nums = vec![-1,0,3,5,9,12];
        let target = 9;
        let ans = 4;
        assert_eq!(search(nums, target), ans);
    }

    #[test]
    fn test_2() {
        let nums = vec![-1,0,3,5,9,12];
        let target = 2;
        let ans = -1;
        assert_eq!(search(nums, target), ans);
    }
}
