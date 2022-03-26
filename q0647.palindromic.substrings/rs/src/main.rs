fn main() {
   let s = String::from("asdf");
   count_substrings(s);
}


pub fn count_substrings(s: String) -> i32 {
    let mut ans = 0;
    let bytes = s.as_bytes();

    for i in 0..bytes.len() as i32{
        ans += count_from_center(bytes, i, i);
        ans += count_from_center(bytes, i, i + 1);
    }
    ans
}

pub fn count_from_center(s: &[u8], mut i:i32, mut j:i32) -> i32 {
    let mut ans = 0;
    while i >= 0 && j < s.len() as i32{
        if s[i as usize] == s[j as usize] {
            ans += 1;
        } else {
            break;
        }
        i -= 1;
        j += 1;
    }
    ans
}


#[cfg(test)]
mod count_substrings_tests{
    use super::*;

    #[test]
    fn test_1(){
        let s = String::from("abc");
        let ans = 3;

        assert_eq!(count_substrings(s), ans);
    }
}

#[test]
fn test_2(){
    let s = String::from("aaa");
    let ans = 6;

    assert_eq!(count_substrings(s), ans);
}



