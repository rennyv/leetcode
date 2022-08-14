struct Solution {}

impl Solution {
    pub fn reverse(x: i32) -> i32 {
        match x < 0 {
            true => {
                -1 * {
                    x.to_string()
                        .chars()
                        .skip(1)
                        .collect::<String>()
                        .chars()
                        .rev()
                        .collect::<String>()
                        .parse::<i32>()
                        .unwrap_or_default()
                }
            }
            false => {
                x.to_string()
                .chars()
                .rev()
                .collect::<String>()
                .parse::<i32>()
                .unwrap_or_default()
            }
        }
    }
}

#[cfg(test)]
mod tests {
    use crate::Solution;

    #[test]
    fn test_1() {
        let x = 123;
        let result = 321;
        assert_eq!(result, Solution::reverse(x));
    }

    #[test]
    fn test_2() {
        let x = -123;
        let result = -321;
        assert_eq!(result, Solution::reverse(x));
    }

    #[test]
    fn test_3() {
        let x = 120;
        let result = 21;
        assert_eq!(result, Solution::reverse(x));
    }
}
