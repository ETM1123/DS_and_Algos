## (1)  query occurs somewhere in the middle of the list of cards
test_general_case =  {
  'input' : {
      'cards' : [13, 11, 10, 7, 4, 3, 1, 0],
      'query' : 7
    },
    'output' : 3
}

## (2) query is the first element in the list of cards
test_query_first_element =  {
  'input' : {
      'cards' : [13, 11, 10, 7, 4, 3, 1, 0],
      'query' : 13
    },
    'output' : 0
}

## (3) query is the last element in the list of cards
test_query_last_element =  {
  'input' : {
      'cards' : [13, 11, 10, 7, 4, 3, 1, 0],
      'query' : 0
    },
    'output' : 7
}

## (4) The list of cards containing one element, which is the query
test_one_element =  {
  'input' : {
      'cards' : [13],
      'query' : 13
    },
  'output' : 0
}

## (5) The list of cards does not contain the query number 
test_query_not_in_cards =  {
  'input' : {
      'cards' : [13, 11, 10, 7, 4, 3, 1, 0],
      'query' : 14
    },
  'output' : -1
}

## (6) The list of cards is empty
test_query_not_in_cards =  {
  'input' : {
      'cards' : [13, 11, 10, 7, 4, 3, 1, 0],
      'query' : 14
    },
  'output' : -1
}
## (7) The list of cards contain multiple cards of the same value
test_repeating_cards = test_repeating_numbers =  {
  'input' : {
      'cards' : [13, 13, 11, 10, 10, 7, 4, 3, 1, 0],
      'query' : 7
    },
    'output' : 5
}

## (8) query occurs multiple times in the list of cards
## in this case return the first instance of query
test_repeating_query =  {
  'input' : {
      'cards' : [13, 11, 10, 7, 7, 7, 4, 3, 1, 0],
      'query' : 7
    },
  'output' : 3
}

test_large_file = {
    'input': {
        'cards': list(range(10000000, 0, -1)),
        'query': 2
    },
    'output': 9999998 
}


test_cases =[
    test_general_case, 
    test_query_first_element, 
    test_query_last_element, 
    test_one_element, 
    test_query_not_in_cards, 
    test_query_not_in_cards, 
    test_repeating_numbers, 
    test_repeating_query 
]

large_test = [test_large_file]