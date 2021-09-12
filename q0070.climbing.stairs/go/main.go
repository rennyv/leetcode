package main

import (
	"fmt"
)

func climbStairs(n int) int {
	if n <= 2 {
		return n
	}
	ans := make([]int, n+1)
	ans[0] = 0
	ans[1] = 1
	ans[2] = 2
	for i := 3; i <= n; i++ {
		ans[i] = ans[i-2] + ans[i-1]
	}
	return ans[n]
}

/*  another solution:
    if n < 3 { return n }

    sum, num := 2, 1
    for i := 3; i <= n; i++ {
        num, sum = sum, sum + num
    }
    return sum;
*/

func main() {
	fmt.Println(climbStairs(4))
}
