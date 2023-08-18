import sys
sys.set_int_max_str_digits(100000)

def addToArrayForm(self, num: List[int], k: int) -> List[int]:
      str_num = ''.join([str(i) for i in num])
      added = int(str_num) + k
      return [int(i) for i in str(added)]
