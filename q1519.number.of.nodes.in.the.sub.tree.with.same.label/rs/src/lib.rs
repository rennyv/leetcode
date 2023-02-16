struct Solution {}

impl Solution {
    pub fn count_sub_trees(n: i32, edges: Vec<Vec<i32>>, labels: String) -> Vec<i32> {
        //fill graph
        let mut graph = vec![Vec::new(); n as usize];
        for edge in edges.iter() {
            let (edge0, edge1) = (edge[0] as usize, edge[1] as usize);
            graph[edge0].push(edge1);
            graph[edge1].push(edge0);
        }

        vec![-1]
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_ex1(){
        let n = 7;
        let edges = vec![vec![0,1],vec![0,2],vec![1,4],vec![1,5],vec![2,3],vec![2,6]];
        let labels = String::from("abaedcd");
        
        let ans = vec![2,1,1,1,1,1,1];
        
        let result = Solution::count_sub_trees(n, edges, labels);
    
        assert_eq!(ans, result)
    }

    #[test]
    fn test_ex2(){
        let n = 4;
        let edges = vec![vec![0,1],vec![1,2],vec![0,3]];
        let labels = String::from("bbbb");
        
        let ans = vec![4,2,1,1];
        
        let result = Solution::count_sub_trees(n, edges, labels);
    
        assert_eq!(ans, result)
    }

    #[test]
    fn test_ex3(){
        let n = 5;
        let edges = vec![vec![0,1],vec![0,2],vec![1,3],vec![0,4]];
        let labels = String::from("aabab");

        let ans = vec![3,2,1,1,1];
        
        let result = Solution::count_sub_trees(n, edges, labels);
    
        assert_eq!(ans, result)
    }
}
