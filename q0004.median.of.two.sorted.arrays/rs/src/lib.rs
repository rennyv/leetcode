struct Solution {}

impl Solution {
    pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
        let mut nums1 = nums1;
        let mut nums2 = nums2;
        if nums1.len() > nums2.len() {
            let tmp = nums1;
            nums1 = nums2;
            nums2 = tmp;
        }
        let m = nums1.len();
        let n = nums2.len();
        let mut l = 0;
        let mut r = m;

        while l <= r {
            let i = (l + r) / 2;
            let j = (m + n) / 2 - i;

            if i < m && nums1[i] < nums2[j - 1] {
                l = i + 1;
            } else if i > 0 && nums1[i - 1] > nums2[j] {
                r = i - 1;
            } else {
                let r_min = if i == m {
                    nums2[j]
                } else if j == n {
                    nums1[i]
                } else {
                    nums1[i].min(nums2[j])
                };

                if (m + n) % 2 == 1 {
                    return r_min as f64;
                }

                let l_max = if i == 0 {
                    nums2[j - 1]
                } else if j == 0 {
                    nums1[i - 1]
                } else {
                    nums1[i - 1].max(nums2[j - 1])
                };

                return (l_max + r_min) as f64 / 2.;
            }
        }

        0.
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        let nums1 = vec![1,3];
        let nums2 = vec![2];

        let result = 2.0;
        assert_eq!(result, Solution::find_median_sorted_arrays(nums1, nums2));
    }

    #[test]
    fn test_2() {
        let nums1 = vec![1,2];
        let nums2 = vec![3,4];

        let result = 2.5;
        assert_eq!(result, Solution::find_median_sorted_arrays(nums1, nums2));
    }
}
