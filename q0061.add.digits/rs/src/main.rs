fn main() {
    println!("{}", add_digits(38));
}

pub fn add_digits(num: i32) -> i32 {
    let mut n = num;
    while n >= 10 {
        let mut sum = 0;
        while n != 0 {
            let m = n % 10;
            sum += m;
            n /= 10;
        }
        n = sum;
    }
    n
}



#[cfg(test)]
mod add_digits_tests {    
    use super::*;
    
    #[test]
    fn test_1() {
        let num = 38;
        assert_eq!(add_digits(num), 2);
    }

    #[test]
    fn test_2() {
        let num = 0;
        assert_eq!(add_digits(num), 0);
    }
}
