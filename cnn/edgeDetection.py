class VertialFilters:
	simple_filter = [[1,0,-1], [1,0,-1], [1,0,-1]]
	sobel_filter = [[1,0,-1], [2,0,-2], [1,0,-1]]
	scharr_filter = [[3,0,-3], [10,0,-10], [3,0,-3]]

class HorizontalFilters:
	simple_filter = [[1,1,1], [0,0,0], [-1,-1,-1]]
	sobel_filter = [[1,2,1], [0,0,0], [-1,-2,-1]]
	scharr_filter = [[3,10,3], [0,0,0], [-3,-10,-3]]