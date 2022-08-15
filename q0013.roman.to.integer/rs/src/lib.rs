struct Solution {}

impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        let mut prev = 0;
        let mut ans = 0;

        for c in s.chars().rev() {
            let current = Self::_convert(c);
            if current < prev {
                ans -= current;
            } else {
                ans += current;
            }
            prev = current;
        }
        ans
    }

    fn _convert(s: char) -> i32 {
        match s {
            'I' => 1,
            'V' => 5,
            'X' => 10,
            'L' => 50,
            'C' => 100,
            'D' => 500,
            'M' => 1000,
            _ => 0
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        let s = String::from("III");
        let result = 3; 
        assert_eq!(result, Solution::roman_to_int(s));
    }

    #[test]
    fn test_2() {
        let s = String::from("LVIII");
        let result = 58; 
        assert_eq!(result, Solution::roman_to_int(s));
    }

    #[test]
    fn test_3() {
        let s = String::from("MCMXCIV");
        let result = 1994; 
        assert_eq!(result, Solution::roman_to_int(s));
    }
}
