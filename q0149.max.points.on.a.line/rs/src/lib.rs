/*
    Interesting problem.  You need to know a bit about geometry for this question.
    The way I solved this was with the idea of first figuring out the slope of 2 
    points.  Then adding the slope to a collection and incrementing it if by 1.

    - Rust has an issue with f32 as keys so I converted to bits and used that.  It 
    worked here, but could cause problems on other solutions.

    Time: O(n^2) for each pair of points we need to calculate slope and frequency
    Space: O(n) we store the data in a hashmap size O(n)
*/

use std::collections::HashMap;

struct Solution {}

impl Solution {
    pub fn max_points(points: Vec<Vec<i32>>) -> i32 {
        let mut max_len = 1;

        // we need to check all the points 0 and the second last point, 
        // since we will have all the data for that point already
        for p1 in 0..points.len() -1 {
            // the intersect point and the count at that point
            let mut intersect_point: HashMap<u32, i32> = HashMap::new();
            for p2 in (p1 + 1)..points.len() {
                let slope = (points[p2][1] - points[p1][1]) as f32 / (points[p2][0] - points[p1][0]) as f32;
                let slope = match slope {
                    -0.0 => 0.0,  // there are the same thing
                    f32::NEG_INFINITY => f32::INFINITY,
                    other => other,
                };

                // hashmap can't do index on f32, so we convert to bits, 
                let count = intersect_point.entry(slope.to_bits()).or_insert(1);
                if *count + 1 > max_len { max_len = *count + 1 }
                *count += 1;
            }
        }

        max_len
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_ex1() {
        let points = vec![vec![1,1],vec![2,2],vec![3,3]];
        let ans = 3;
        
        let result = Solution::max_points(points);
        assert_eq!(result, ans);
    }

    #[test]
    fn test_ex2() {
        let points = vec![vec![1,1],vec![3,2],vec![5,3],vec![4,1],vec![2,3],vec![1,4]];
        let ans = 4;
        
        let result = Solution::max_points(points);
        assert_eq!(result, ans);
    }

    #[test]
    fn test_ex3() {
        let points = vec![vec![0,0]];
        let ans = 1;
        
        let result = Solution::max_points(points);
        assert_eq!(result, ans);
    }
}
