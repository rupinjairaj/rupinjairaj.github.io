## Prefix Sum
- If we need to check if a subarray exists whose sum is divisible by k we can 
	1) Compute the prefix sums of the entire array and at each point calculate the remainder of the current sum when divided by k.
	2) In a dictionary we can store key value pairs of the form (remainder, position in prefix subarray) [if we need to find subarrays of specific lengths] or (remainder, count) [if we need to find the number of subarrays whose sum is divisible by k].
- Why does this work?
	1) Consider we have two sums S1 and S2 in the prefix sum array whose remainders are the same when divided by k.
	2) S1 = k*x + remainder and S2 = k*y + remainder
	3) Subtracting the two equations gives us: S1-S2 = k(x-y)
	4) This shows us that the subarray between S1 and S2 is a perfect multiple of k.
