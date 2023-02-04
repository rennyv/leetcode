struct Solution {}

impl Solution {
    pub fn check_inclusion(s1: String, s2: String) -> bool {
        let (l1, l2) = (s1.len(), s2.len());

        if l1 > l2 {
            return false;
        }

        let (mut c1, mut c2) = ([0; 26], [0; 26]);
        let s2: Vec<usize> = s2.bytes().map(|b| (b - b'a') as usize).collect();
        s1.bytes()
            .map(|b| (b - b'a') as usize)
            .for_each(|i| c1[i] += 1);
        s2.iter().take(l1).for_each(|i| c2[*i] += 1);
        c1 == c2 || (0..l2 - l1).any(|i| {
            c2[s2[i]] -= 1;
            c2[s2[i + l1]] += 1;
            c1 == c2
        })
    }
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_ex1() {
        let s1 = String::from("ab");
        let s2 = String::from("eidbaooo");
        let ans = true;

        let result = Solution::check_inclusion(s1, s2);
        assert_eq!(result, ans);
    }

    #[test]
    fn test_ex2() {
        let s1 = String::from("ab");
        let s2 = String::from("eidboaooo");
        let ans = false;

        let result = Solution::check_inclusion(s1, s2);
        assert_eq!(result, ans);
    }

    
    #[test]
    fn test_ex3() {
        let s1 = String::from("ab234");
        let s2 = String::from("23");
        let ans = false;

        let result = Solution::check_inclusion(s1, s2);
        assert_eq!(result, ans);
    }
}
