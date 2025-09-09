data = [1, 2, 8, 2, 9, 0]

def max_item(items):
   if( len(items) == 1):
      return items[0]
   mid = len(items)//2
   left_max = max_item(items[:mid])
   right_max = max_item(items[mid:])
   return left_max if left_max > right_max else right_max


print(f"Max: {max_item(data)}")
