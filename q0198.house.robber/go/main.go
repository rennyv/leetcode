package main

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func rob(nums []int) int {
	L := len(nums)
	if L == 1 {
		return nums[0]
	}

	dp := make([]int, L+1)
	dp[0] = 0
	dp[1] = nums[0]

	for i := 1; i < L; i++ {
		dp[i+1] = max(dp[i], dp[i-1]+nums[i])
	}

	return dp[L]
}
