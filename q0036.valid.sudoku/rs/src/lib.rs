struct Solution {}

impl Solution {
    pub fn is_valid_sudoku(board: Vec<Vec<char>>) -> bool {
        let mut rows = vec![vec![false; 9]; 9];
        let mut cols = vec![vec![false; 9]; 9];
        let mut boxs = vec![vec![false; 9]; 9];

        for row in 0..9 {
            for col in 0..9{
                let b = (row/3)*3 + col/3;

                if board[row][col] != '.' {
                    let num = board[row][col].to_digit(10).unwrap() as usize - 1;
                    
                    if rows[row][num] || cols[col][num] || boxs[b][num]{
                        return false
                    }

                    rows[row][num] = true;
                    cols[col][num] = true;
                    boxs[b][num] = true;
                }

            }
        }
        
              
        
        
        return true
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_ex1() {
        let grid = vec![
            vec!['5','3','.','.','7','.','.','.','.'],
            vec!['6','.','.','1','9','5','.','.','.'],
            vec!['.','9','8','.','.','.','.','6','.'],
            vec!['8','.','.','.','6','.','.','.','3'],
            vec!['4','.','.','8','.','3','.','.','1'],
            vec!['7','.','.','.','2','.','.','.','6'],
            vec!['.','6','.','.','.','.','2','8','.'],
            vec!['.','.','.','4','1','9','.','.','5'],
            vec!['.','.','.','.','8','.','.','7','9'],
        ];

        let ans = true;

        assert_eq!(ans, Solution::is_valid_sudoku(grid));
    }

    #[test]
    fn test_ex2() {
        let grid = vec![
            vec!['8','3','.','.','7','.','.','.','.'],
            vec!['6','.','.','1','9','5','.','.','.'],
            vec!['.','9','8','.','.','.','.','6','.'],
            vec!['8','.','.','.','6','.','.','.','3'],
            vec!['4','.','.','8','.','3','.','.','1'],
            vec!['7','.','.','.','2','.','.','.','6'],
            vec!['.','6','.','.','.','.','2','8','.'],
            vec!['.','.','.','4','1','9','.','.','5'],
            vec!['.','.','.','.','8','.','.','7','9'],
        ];

        let ans = false;

        assert_eq!(ans, Solution::is_valid_sudoku(grid));
    }
}
