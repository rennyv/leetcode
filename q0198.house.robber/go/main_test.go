package main

import (
	"testing"

	"gotest.tools/assert"
)

func Test_1(t *testing.T) {
	nums := []int{1, 2, 3, 1}
	assert.Equal(t, 4, rob(nums))
}

func Test_2(t *testing.T) {
	nums := []int{2, 7, 9, 3, 1}
	assert.Equal(t, 12, rob(nums))
}
