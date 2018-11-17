class BinarySearch:
    # given a sorted array, find the key's index
    def search(self, key, a, lo, hi):
        if hi <= lo:
            return -1
        
        mid = (hi + lo) // 2
        
        if key < a[mid]:
            return self.search(key, a, lo, mid)
        if key > a[mid]:
            return self.search(key, a, mid, hi)
        else:
            return mid


key = 4
a = [1,2,3,4,5,6,7,8]
print(BinarySearch().search(key, a, 0, len(a)))