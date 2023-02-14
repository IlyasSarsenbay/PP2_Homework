def spy_game(nums):
    for x in range(0,len(nums)):
        f=nums.index(0)
        s=nums.index(f+1)
        e=nums.index(7)
        if nums[f:s+1]!=e and e>s:
            return True
        else:
            return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))