struct Solution {}

impl Solution {
    fn colorcoded(index: i32, group_id: i32, adjmap: &mut Vec<Vec<i32>>, dispatch_group: &mut Vec<i32>) -> bool {
        if dispatch_group[index as usize] == -1 {
            dispatch_group[index as usize] = group_id;
        }

        let dislike_list = adjmap[index as usize].clone();
        for dislike_index in dislike_list.iter() {
            if dispatch_group[*dislike_index as usize] == -1 {
                Solution::colorcoded(*dislike_index, 1 - group_id, adjmap, dispatch_group);
            }
            else if dispatch_group[*dislike_index as usize] == dispatch_group[index as usize] {
                return false;
            }
        }
        
        true
    }

    pub fn possible_bipartition(n: i32, dislikes: Vec<Vec<i32>>) -> bool {
        let mut dispatch_group = vec![-1; (n + 1) as usize];
        let mut dislike_adjmap = vec![vec![]; (n + 1) as usize];

        for dislike_pair in dislikes.iter(){
            dislike_adjmap[dislike_pair[0] as usize].push(dislike_pair[1]);
            dislike_adjmap[dislike_pair[1] as usize].push(dislike_pair[0]);
        }

        for i in 0..n {
            if dispatch_group[i as usize] == -1 {
                if !Solution::colorcoded(i, 0, &mut dislike_adjmap, &mut dispatch_group) { 
                    return false;
                }
            }
        }

        true
    }
}

#[cfg(test)]
mod tests {
    use std::vec;

    use super::*;

    #[test]
    fn test_ex1() {
        let n = 4;
        let dislikes = vec![
            vec![1,2],
            vec![1,3],
            vec![2,4]
        ];
        
        let ans = true;
        assert_eq!(Solution::possible_bipartition(n, dislikes), ans);
    }

    #[test]
    fn test_ex2() {
        let n = 3;
        let dislikes = vec![
            vec![1,2],
            vec![1,3],
            vec![2,3]
        ];
        
        let ans = false;
        assert_eq!(Solution::possible_bipartition(n, dislikes), ans);
    }

    #[test]
    fn test_ex3() {
        let n = 5;
        let dislikes = vec![
            vec![1,2],
            vec![2,3],
            vec![3,4],
            vec![4,5],
            vec![1,5]
        ];
        
        let ans = false;
        assert_eq!(Solution::possible_bipartition(n, dislikes), ans);
    }
}
