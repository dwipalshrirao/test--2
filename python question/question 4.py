

def get_quadruplets(nums, target):
 
    quadraplates = []
    nums.sort()

    for i in range(len(nums) - 3):
        for j in range(i + 1, len(nums) - 2):
 
            k = target - (nums[i] + nums[j])

            low = j + 1
            high = len(nums) - 1
 
            while low < high:
                if nums[low] + nums[high] < k:
                    low = low + 1
                elif nums[low] + nums[high] > k:
                    high = high - 1
                else:
                    quadraplates.append([nums[i], nums[j], nums[low], nums[high]])
                    (low, high) = (low + 1, high - 1)
    
    return quadraplates


nums = [2, 7, 4, 0, 9, 5, 1, 5]
target = 20
quadruplets = get_quadruplets(nums, target)
if not quadruplets:
    print("No quadraplates found")
else:
    print("output:- ", quadruplets)