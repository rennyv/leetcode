struct Solution {}

impl Solution {
    pub fn num_islands(grid: Vec<Vec<char>>) -> i32 {
        let mut visited = grid.clone();
        let mut result = 0;
        if grid.len() == 0 || grid[0].len() == 0 {
            return 0 as i32;
        }
        
        let height = grid.len();
        let width = grid[0].len();

        for row in &mut visited{
            for c in row{
                *c = 0 as char;
            }
        }

        fn dfs(grid: &Vec<Vec<char>>, visited: &mut Vec<Vec<char>>, i:usize, j:usize, height:usize, width:usize) {
            visited[i][j] =1 as char;
            if i>0 && visited[i-1][j] == 0 as char  && grid[i-1][j] == '1' { dfs(grid,visited,i-1,j,height,width); }
            if j>0 && visited[i][j-1] == 0 as char && grid[i][j-1] == '1' { dfs(grid,visited,i,j-1,height,width); }
            if i<height-1 && visited[i+1][j] == 0 as char && grid[i+1][j] == '1' { dfs(grid,visited,i+1,j,height,width); }
            if j<width-1 && visited[i][j+1] == 0 as char && grid[i][j+1] == '1' { dfs(grid,visited,i,j+1,height,width); }
        }

        for (i, row) in grid.iter().enumerate(){
            for (j,c) in row.iter().enumerate() {
                if *c == '1' && visited[i][j] == 0 as char {
                    result += 1;
                    dfs(&grid, &mut visited, i,j, height, width)
                }
            }
        }


        result
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_01() {
        let grid = vec![
            vec!['1','1','1','1','0'],
            vec!['1','1','0','1','0'],
            vec!['1','1','0','0','0'],
            vec!['0','0','0','0','0']
        ];

        let ans = 1;

        assert_eq!(ans, Solution::num_islands(grid))
    }

    #[test]
    fn test_02() {
        let grid = vec![
            vec!['1','1','0','0','0'],
            vec!['1','1','0','0','0'],
            vec!['0','0','1','0','0'],
            vec!['0','0','0','1','1']
        ];

        let ans = 3;

        assert_eq!(ans, Solution::num_islands(grid))
    }
}
