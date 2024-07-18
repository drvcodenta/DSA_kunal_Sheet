class bubbleSort:
    def __init__(self, array):
        self.array = array
        self.length = len(array)
    
    def __str__(self):
        return " ".join([str(x) for x in self.array])
    
    def bubbleSortRecursive(self, i):
        n = self.length
        if i == n - 1:
            return
        count = 0
        for j in range(0, n-1):
            if self.array[j] > self.array[j+1]:
                self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
                count = count + 1
        
        if (count == 0):
            return
        
        self.bubbleSortRecursive(i=i+1)

def main():
    array = [5, 1, 4, 2, 8]
    sort = bubbleSort(array)
    sort.bubbleSortRecursive(0)
    print("Sorted array: \n", sort)

if __name__ == "__main__":
    main()