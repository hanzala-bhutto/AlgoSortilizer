def quickSort(draw_info,draw_list, ascending=True):
	lst = draw_info.lst

	def partition(lst, low, high, ascending=True):
		i = (low - 1)
		pivot = lst[high]

		for j in range(low, high):
			if (lst[j] < pivot and ascending) or (lst[j] > pivot and not ascending):
				i = i + 1
				lst[i], lst[j] = lst[j], lst[i]
				draw_list(draw_info, {i: draw_info.GREEN, j: draw_info.RED}, True)
				yield True

		lst[i + 1], lst[high] = lst[high], lst[i + 1]
		draw_list(draw_info, {i + 1: draw_info.GREEN, high: draw_info.RED}, True)
		yield True
		return (i + 1)

	def quickSort(lst, low, high, ascending=True):
		if low < high:
			pi = yield from partition(lst, low, high, ascending)
			yield from quickSort(lst, low, pi - 1, ascending)
			yield from quickSort(lst, pi + 1, high, ascending)

	yield from quickSort(lst, 0, len(lst) - 1, ascending)
	return lst