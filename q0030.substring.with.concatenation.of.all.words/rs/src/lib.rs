struct Solution {}

use std::collections::{HashMap, hash_map::Entry};
impl Solution {
    pub fn find_substring(s: String, words: Vec<String>) -> Vec<i32> {
        let mut start_indices = Vec::<i32>::new();
        
        //is the word array empty
        if words.is_empty() {
            return start_indices;
        }

        let word_size = words[0].len();
        let window_size = word_size * words.len();

        if let Some(last_split) = s.len().checked_sub(window_size) {
            let mut word_set = HashMap::with_capacity(words.len());
            words.iter().for_each(|w|{
                let counter = word_set.entry(&w[..]).or_insert(0);
                *counter += 1;
            });

            word_set.shrink_to_fit();
            let mut seen = word_set.keys().map(|k| (*k, 0)).collect::<HashMap<_,_>>();

            for i in 0..word_size.min(last_split + 1) {
                let mut j = i + window_size;
                while j <= s.len() {
                    let mut k = 1;
                    while k <= words.len() {
                        let current_pos = j - k * word_size;
                        let current = &s[current_pos..(current_pos + word_size)];

                        match seen.entry(current) {
                            Entry::Occupied(entry) => {
                                let res = entry.into_mut();
                                *res += 1;
                                if *res > *word_set.get(current).unwrap(){
                                    break;
                                } else {
                                    k += 1;
                                }
                            }
                            Entry::Vacant(_) =>{
                                break;
                            }
                        }
                    }

                    let start = j - window_size;
                    if k > words.len() {
                        start_indices.push(start as i32);
                        j += word_size;
                    } else {
                        j= window_size + (j - (k-1)* word_size);
                    }
                    seen.values_mut().for_each(|v| *v = 0);
                }
            }
        }
        start_indices
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
        let s = String::from("barfoothefoobarman");
        let words = vec_of_str!["foo","bar"];

        let result = vec![0,9];

        assert_eq!(result, Solution::find_substring(s, words));
    }

    #[test]
    fn test_2() {
        let s = String::from("wordgoodgoodgoodbestword");
        let words = vec_of_str!["word","good","best","word"];

        let result: Vec<i32> = vec![];

        assert_eq!(result, Solution::find_substring(s, words));
    }

    #[test]
    fn test_3() {
        let s = String::from("barfoofoobarthefoobarman");
        let words = vec_of_str!["bar","foo","the"];

        let result: Vec<i32> = vec![6,9,12];

        assert_eq!(result, Solution::find_substring(s, words));
    }
}
