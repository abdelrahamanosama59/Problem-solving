def count_substring(string, sub_string):
  c = 0
  b = len(sub_string)
  for i in range(len(string)):
    s = string[i:i+b]
    c += s.count(sub_string)
  return c
