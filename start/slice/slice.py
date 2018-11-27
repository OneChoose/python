a = list(range(1,8))
print(a)
print(a[:3])  # [1,2,3]  即索引是 [0,3) => a[0]、a[1]、a[2]
print(a[:-5]) # [1,2]  等价于 a[:(-5+a中元素个数7)] = a[:2] = [1,2]
print(a[:5:2])  # [1,3,5]  先取前5个元素，然后按照间隔2取数
print(a[:4:-1]) # [7,6]  先看interval为负值，故从右往左取，取到下标为4的前一个为止，即能取到a[6]、a[5]
print(a[:3:-2])  # [7,5]  先看interval为负值，故从右往左取，取到下标为3的前一个为止，即能取到a[6]、a[5]、a[4]，然后按照间隔2取数
print(a[:-5:-1]) # [7,6,5,4]  先看interval为负值，故从右往左取，取到下标为-5的前一个为止，即能取到a[-1]、a[-2]、a[-3]、a[-4]
print(a[:10]) # [1,2,3,4,5,6,7]  即索引是 [0,10)，超过不报错
print(a[:10:-1]) # []  先看interval为负值，故从右往左取，取到下标为10的前一个为止，但是从左到右取最大的下标也才是a[6]，故返回[]
print(a[:-100:-1]) # [7,6,5,4,3,2,1]  先看interval为负值，故从右往左取，取到下标为-100的前一个为止，即能取到a[-1]、a[-2]、a[-3]、a[-4]、a[-5]、a[-6]、a[-7]
print(a[::-1]) # [7,6,5,4,3,2,1]  先看interval为负值，故从左往右取，取到头（因为end没有指定）为止，即能取到a[-1]、a[-2]、a[-3]、a[-4]、a[-5]、a[-6]、a[-7] ，该方法也是list反转的方法
print(a[::2]) # [1,3,5,7]  每隔2个元素取数
print(a[3::2]) # [4,6]  从a[3]=4开始，每隔2个元素取数
print(a[1:5:2])
