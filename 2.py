def is_ok(t):
	for i in range(len(t)):
		base = set(t[i])
		for j in range(i + 1, len(t)):
			for thing in t[j]:
				if thing in base:
					return True
	return False


def divide_almost_equally_into_2(arr, limit, cur, index, debris):
	if cur > limit:
		return 0
	
	if index == len(arr):
		if cur != 0:
			if recorder.get(cur) is None:
				recorder[cur] = [debris]
			else:
				recorder[cur].append(debris)
		return 0
	
	divide_almost_equally_into_2(arr, limit, cur + arr[index], index + 1, [index] + debris)
	divide_almost_equally_into_2(arr, limit, cur, index + 1, debris)
	return 0


recorder = dict()

# _arr = [int(i) for i in input().strip().split(' ')]
n = 2
_arr = [1, 2, 3, 6, 7, 7]
arr = [i for i in _arr if i != 0]
total = (sum(arr))
limit = total // 2

divide_almost_equally_into_2(arr, limit, 0, 0, [])

current_max = 0
for key, val in recorder.items():
	print(key, val)
	if key > current_max:
		if is_ok(val):
			current_max = key

print(current_max)
