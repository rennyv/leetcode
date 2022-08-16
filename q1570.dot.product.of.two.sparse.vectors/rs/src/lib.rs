use std::collections::HashMap;

struct SparseVector {
    map: HashMap<usize, i32>	
}

/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl SparseVector {
    fn new(nums: Vec<i32>) -> Self {
        // create hashmap idx,value
        let mut map = HashMap::new();
        
        for (i, n) in nums.into_iter().enumerate(){
            if n != 0 {
                map.entry(i).or_insert(n);
            }
        }

        Self{ map }
    }
	
    // Return the dotProduct of two sparse vectors
    fn dot_product(&self, vec: SparseVector) -> i32 {
        //find shortest hashmap, dot_product each 
        vec.map.into_iter()
            .map(|(i,n1)|{
                if let Some(n2) = self.map.get(&i){
                    n1 * n2
                } else {
                    0
                }
            })
            .sum()            
    }
}

/**
 * Your SparseVector object will be instantiated and called as such:
 * let v1 = SparseVector::new(nums1);
 * let v2 = SparseVector::new(nums2);
 * let ans = v1.dot_product(v2);
 */

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        let nums1 = vec![1,0,0,2,3];
        let nums2 = vec![0,3,0,4,0];
        let result = 8;

        let v1 = SparseVector::new(nums1);
        let v2 = SparseVector::new(nums2);

        assert_eq!(result, v1.dot_product(v2));
    }

    #[test]
    fn test_2() {
        let nums1 = vec![0,1,0,0,0];
        let nums2 = vec![0,0,0,0,2];
        let result = 0;

        let v1 = SparseVector::new(nums1);
        let v2 = SparseVector::new(nums2);

        assert_eq!(result, v1.dot_product(v2));
    }

    #[test]
    fn test_3() {
        let nums1 = vec![0,1,0,0,2,0,0];
        let nums2 = vec![1,0,0,0,3,0,4];
        let result = 6;

        let v1 = SparseVector::new(nums1);
        let v2 = SparseVector::new(nums2);

        assert_eq!(result, v1.dot_product(v2));
    }
}
