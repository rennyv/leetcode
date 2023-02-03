struct Solution {}

impl Solution {
    pub fn min_time(n: i32, edges: Vec<Vec<i32>>, has_apple: Vec<bool>) -> i32 {
        // Setup the graph (not a tree)
        let mut graph = vec![Vec::new(); n as usize];
        for edge in edges.iter() {
            let (edge0, edge1) = (edge[0] as usize, edge[1] as usize);
            graph[edge0].push(edge1);
            graph[edge1].push(edge0);
        }
        let mut visited = vec![false; n as usize];
        visited[0] = true;
        Self::dfs_solve(&graph, &mut visited, &has_apple, 0, 0)
    }

    fn dfs_solve(graph: &Vec<Vec<usize>>, visit: &mut Vec<bool>, has_apple: &Vec<bool>, root: usize, count: i32) -> i32 {
        let mut total_count = 0;
        let mut n_count_added = -1;
        for &adj in graph[root].iter() {
            if visit[adj] == true {
                continue;
            }
            visit[adj] = true;
            let rcount = Self::dfs_solve(graph, visit, has_apple, adj, count + 1);
            if rcount > 0 {
                total_count += rcount + 1;
                n_count_added += 1;
            }
        }

        if n_count_added >= 0 {
            total_count - count*n_count_added
        } else {
            if has_apple[root] {
                count
            } else {
                0
            }
        }
    }
}
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_ex1() {
        let n = 7;
        let edges = vec![vec![0,1],vec![0,2],vec![1,4],vec![1,5],vec![2,3],vec![2,6]];
        let has_apple = vec![false,false,true,false,true,true,false];
        let ans = 8;

        let result = Solution::min_time(n, edges, has_apple);

        assert_eq!(result, ans);
    }

    #[test]
    fn test_ex2() {
        let n = 7;
        let edges = vec![vec![0,1],vec![0,2],vec![1,4],vec![1,5],vec![2,3],vec![2,6]];
        let has_apple = vec![false,false,true,false,false,true,false];
        let ans = 6;

        let result = Solution::min_time(n, edges, has_apple);

        assert_eq!(result, ans);
    }

    #[test]
    fn test_ex3() {
        let n = 7;
        let edges = vec![vec![0,1],vec![0,2],vec![1,4],vec![1,5],vec![2,3],vec![2,6]];
        let has_apple = vec![false,false,false,false,false,false,false];
        let ans = 0;

        let result = Solution::min_time(n, edges, has_apple);

        assert_eq!(result, ans);
    }

}
