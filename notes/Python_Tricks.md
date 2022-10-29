# Sorting
- Sort a list of strings by length:
	- strs.sort(key=len)
	- sorted_list = sorted(unsorted_list, key=len)

- Sort a list of pairs where each pair is a tuple of the form (string, int)
	- list_to_sort.sort(key=lambda x: (-x[1], x[0]))
		- This would sort the list in descending order of the int value in the pair and in lexicographicaly increasing order of the string if the integers in comparison are equal.