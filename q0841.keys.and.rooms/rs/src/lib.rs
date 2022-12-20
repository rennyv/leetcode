struct Solution {}

impl Solution {
    pub fn can_visit_all_rooms(rooms: Vec<Vec<i32>>) -> bool {
        // create a hash set to store if you visited
        let mut visited = vec![false; rooms.len()];
        visited[0] = true;

        //create a queue to visit the rooms
        //init it to room 0
        let mut stack = vec![0];

        while let Some(next) = stack.pop() {
            for &i in &rooms[next as usize] {
                if !visited[i as usize] {
                    visited[i as usize] = true;
                    stack.push(i)
                }
            }
        }
        
        //if you visited all the rooms return true
        visited.iter().all(|&b| b)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_ex1() {
        let rooms = vec![
            vec![1],
            vec![2],
            vec![3],
            vec![]
        ];
        let ans = true;
        assert_eq!(ans, Solution::can_visit_all_rooms(rooms));
    }

    #[test]
    fn test_ex2() {
        let rooms = vec![
            vec![1,3],
            vec![3,0,1],
            vec![2],
            vec![0]
        ];

        let ans = false;
        assert_eq!(ans, Solution::can_visit_all_rooms(rooms));
    }
}
