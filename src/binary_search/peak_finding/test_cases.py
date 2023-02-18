"""Test cases"""

# 1. one element array
test_one_element = {
    "input": {
      "nums" : [1]
    },
    "output": 0
}
# 2. two element array, with first element as peak
test_two_element_p1 = {
    "input": {
      "nums" : [1, 0]
    },
    "output": 0
}
# 3. two element array, with second element as peak
test_two_element_p2 = {
    "input": {
      "nums" : [1, 2]
    },
    "output": 1
}
# 4. n element array, with first element as peak
test_n_element_p1 = {
    "input": {
      "nums" : [9, 8, 7, 6, 5, 4, 3, 2, 1]
    },
    "output": 0
}
# 5. n element array, with last element as peak
test_n_element_p2 = {
    "input": {
      "nums" : [1, 2, 3, 4, 5, 6, 7, 8, 9]
    },
    "output": 8
}
# 6. n element array, with last n/2 element as peak
test_n_element_p3 = {
    "input": {
      "nums" : [1, 2, 3, 4, 100, 6, 7, 8, 6]
    },
    "output": 4
}
# 7. n element array, with peak in the first half of the array
test_n_element_p4 = {
    "input": {
      "nums" : [1, 2, 100, 6, 5, 4, 7, 8, 9]
    },
    "output": 2
}
# 8. n element array, with peak in the second half of the array 
test_n_element_p5 = {
    "input": {
      "nums" : [1, 2, 3, 4, 5, 6, 100, 8, 9]
    },
    "output": 6
}

test_cases = [
test_one_element, 
test_two_element_p1, 
test_two_element_p2, 
test_n_element_p1, 
test_n_element_p2, 
test_n_element_p3, 
test_n_element_p4, 
test_n_element_p5 
]