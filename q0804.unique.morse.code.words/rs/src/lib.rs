struct Solution {}

use std::collections::HashSet;
impl Solution {
    pub fn unique_morse_representations(words: Vec<String>) -> i32 {
        
        let codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."];

       words.iter()
            .map(|w| w.chars().map(|c| codes[c as usize - 'a' as usize]).collect::<String>())
            .collect::<HashSet<_>>()
            .len() as i32
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    
    macro_rules! vec_of_str {
        ($($x:expr),*) => (vec![$($x.to_string()),*]);
    }
    
    #[test]
    fn test_1() {
        let words = vec_of_str!["gin","zen","gig","msg"];

        let result = 2;

        assert_eq!(result, Solution::unique_morse_representations(words));
    }

    #[test]
    fn test_2() {
        let words = vec_of_str!["a"];

        let result = 1;

        assert_eq!(result, Solution::unique_morse_representations(words));
    }
}
