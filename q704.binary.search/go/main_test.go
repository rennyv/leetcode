package q704

import (
	"testing"

	"gotest.tools/assert"
)

func Test_search_1(t *testing.T) {
	nums := []int{-1, 0, 3, 5, 9, 12}
	target := 9
	ans := search(nums, target)
	assert.Equal(t, ans, 4)
}

func Test_search_2(t *testing.T) {
	nums := []int{-1, 0, 3, 5, 9, 12}
	target := 2
	ans := search(nums, target)
	assert.Equal(t, ans, -1)
}
