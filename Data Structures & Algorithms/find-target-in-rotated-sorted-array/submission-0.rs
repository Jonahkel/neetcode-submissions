impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let (mut l, mut r) = (0usize, nums.len()-1);
        while nums[l] > nums[r] {
            let mid = (l+r) / 2;
            if nums[mid] < nums[l] {
                r = mid;
            } else {
                l = mid+1;
            }
        }

        if l == 0{
            r = nums.len() - 1;
        } else{
            r = l-1;
        }
        while r != l {
            let mid = if r > l {(r+l)/2} else {((r+nums.len() + l) / 2) % nums.len()};
            if nums[mid] < target {
                l = (mid+1)%nums.len();
            } else if nums[mid] > target{
                r = mid;
            } else {
                return mid.try_into().unwrap();
            }
        }

        if nums[l] == target{
            l.try_into().unwrap()
        } else{
            -1
        }
    }
}
