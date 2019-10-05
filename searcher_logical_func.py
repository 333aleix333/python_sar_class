def AND(list1, list2):
	res = []
	i = 0
	j = 0
	while i < len(list1) and j < len(list2):
		if(list1[i] == list2[j]):
			res += [list1[i]]
			i += 1
			j += 1
		elif(list1[i] < list2[j]):
			i += 1
		else:
			j += 1
	return res

def OR(xs, ys):
	res = []
	i = 0
	j = 0
	while i < len(xs) and j < len(ys):
		x = xs[i]
		y = ys[j]
		if x == y:
			res.append(x)
			i += 1
			j += 1
		elif x < y:
			res.append(x)
			i += 1
		else:
			res.append(y)
			j += 1
	while i < len(xs):
		res.append(xs[i])
		i += 1
	while j < len(ys):
		res.append(ys[j])
		j += 1
	return res

def SUB(xs, ys):
	res = []
	i = 0
	j = 0
	while i < len(xs) and j < len(ys):
		x = xs[i]
		y = ys[j]
		if x == y:
			i += 1
			j += 1
		elif x < y:
			res.append(x)
			i += 1
		else:
			j += 2
	while i < len(xs):
		res.append(xs[i])
		i += 1
	return res
