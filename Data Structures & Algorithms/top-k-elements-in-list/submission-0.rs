impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut freq: HashMap<i32, i32> = HashMap::new();
    
        for num in &nums {
            *freq.entry(*num).or_insert(0)+=1;
        }

        let mut buckets: Vec<Vec<i32>> = vec![vec![]; nums.len()+1];

        for (key, value) in freq {
            buckets[value as usize].push(key);
        }


        let mut result = Vec::<i32>::new();
        for bucket in buckets.iter().rev() {
            for num in bucket {
                result.push(*num);
                if result.len() == k as usize {
                    return result;
                }
            }
        }

        result
    }
}