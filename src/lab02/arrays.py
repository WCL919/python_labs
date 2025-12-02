def min_max(nums:list[float |int]) -> tuple[float | int, float | int]:
  if not nums:
   raise ValueError("Пустой список")
  return(min(nums),max(nums))
def unique_sorted(nums: list[float | int]) -> list[float | int]:
  unique_elements=list(set(nums))
  unique_elements.sort()
  return unique_elements
def flatten(mat: list[list | tuple]) -> list:
  result =[]
  for item in mat:
    if not isinstance(item,(list,tuple)):
      raise TypeError("Элемент не является списком/кортежем")
    result.extend(flatten(item)if isinstance(item,(list,tuple))else[item])
    return result