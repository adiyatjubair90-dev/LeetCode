#.type(), .upper(), .lower(), count(), .capitalize(), .isalpha(), .isdigit(), .isupper(), .islower(), .split(), .join(), .find(), .replace()
#and or not
#list [, , ,] len(), .append(), .extend(), .pop(), ordered mutable
#slice [start:end:step]
#set { , , ,} .add(), .remove(), .union(), .intersection(), .items(), del, unordered mutable
#function def name(params): return

def merge(nums1, m, nums2, n):
    nums1[m:] = nums2
    nums1.sort()
print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))