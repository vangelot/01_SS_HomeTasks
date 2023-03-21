class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True

        place = 0
        while place < len(flowerbed) - 1:
            if flowerbed[place] == 1:
                place += 2
                continue
            if flowerbed[place+1] == 0:
                n -= 1
                place += 2
                if n == 0:
                    return True
            else:
                place += 3
        if (place == len(flowerbed) - 1) and (flowerbed[place] == 0) and (flowerbed[place - 1] == 0):
            n -= 1
        return n == 0

def main():
    a = Solution()
    print(a.canPlaceFlowers([1,0,0,0,0,1], 2))



if __name__ == '__main__':
    main()