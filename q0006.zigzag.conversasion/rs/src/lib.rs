struct Solution {}

impl Solution {
    pub fn convert(s: String, num_rows: i32) -> String {
        if num_rows == 1 || num_rows as usize > s.len(){
            return s
        }

        let chars: Vec<_> = s.chars().collect();
        let mut arrs = vec![String::new(); num_rows as usize];

        let n = num_rows - 1;
        let matrix_size = 2 * n;

        for i in 0..s.len(){
            let arr_selected = ( ((i as i32+n) % matrix_size) - n).abs();
            arrs[arr_selected as usize].push(chars[i])
        }

       arrs.join("").to_string()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_ex1() {
        let s = String::from("PAYPALISHIRING");
        let num_rows = 3;
        let ans = String::from("PAHNAPLSIIGYIR");

        let result = Solution::convert(s, num_rows);
        assert_eq!(result, ans);
    }

    #[test]
    fn test_ex2() {
        let s = String::from("PAYPALISHIRING");
        let num_rows = 4;
        let ans = String::from("PINALSIGYAHRPI");

        let result = Solution::convert(s, num_rows);
        assert_eq!(result, ans);
    }

    #[test]
    fn test_ex3() {
        let s = String::from("A");
        let num_rows = 1;
        let ans = String::from("A");

        let result = Solution::convert(s, num_rows);
        assert_eq!(result, ans);
    }
}
