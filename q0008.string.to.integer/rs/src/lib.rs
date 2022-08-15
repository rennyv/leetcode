use std::string;

struct Solution;

impl Solution {
    pub fn my_atoi(s: String) -> i32 {
        let mut chrs = s.chars().skip_while(|c| c == &' ').peekable();
        
        let sign = if chrs.peek().map_or(false, |s| s == & '-') {
            chrs.next();
            -1i32
        } else {
            if chrs.peek().map_or(false, |s| s == &'+') {
                chrs.next();
            }
            1i32
        };

        chrs
            .into_iter()
            .take_while(|n| n.is_numeric())
            .try_fold(0i32, |acc, n| acc.checked_mul(10).and_then(|acc| acc.checked_add(n.to_digit(10).unwrap() as i32)))
            .map(|n| n * sign)
            .unwrap_or(if sign > 0 { i32::MAX} else { i32::MIN})
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        let s = String::from("42");
        let result = 42;
        assert_eq!(result, Solution::my_atoi(s));
    }

    #[test]
    fn test_2() {
        let s = String::from("        -42");
        let result = -42;
        assert_eq!(result, Solution::my_atoi(s));
    }

    #[test]
    fn test_3() {
        let s = String::from("4193 with words");
        let result = 4193;
        assert_eq!(result, Solution::my_atoi(s));
    }
}
