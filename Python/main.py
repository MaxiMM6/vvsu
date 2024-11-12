odd_result = list(map(lambda y: False, filter(lambda y: y % 2 != 0, new_number)))
even_result = list(map(lambda z: True, filter(lambda z: z % 2 == 0, new_number)))