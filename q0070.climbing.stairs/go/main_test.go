package main

import (
	"testing"

	"gotest.tools/assert"
)

func TestClimbStairs1(t *testing.T) {
	assert.Equal(t, 1, climbStairs(1))
}

func TestClimbStairs2(t *testing.T) {
	assert.Equal(t, 2, climbStairs(2))
}

func TestClimbStairs5(t *testing.T) {
	assert.Equal(t, 5, climbStairs(4))
}
