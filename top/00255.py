class solution():
	def ladder(self,beginword,endword,wordList,):
		if endword not in wordList:
			return 0
		queue = []
		queue.append(beginword,1)
		visited = set()
		dic = collections.defautdict(list)


		for word in wordlist:
			for i in range(len(word)):
				dic[word[:i] + '_' +word[i+1:]].append(word)

	    while queue:
	    	word,step = queue.pop(0)
	    	if word == end:
				return step

	    	for i in range(len(word)):
	    		temp = word[:i] + "_" + word[i+1:]
	    		for value in dic[temp]:
	    			if value not visited:
	    				queue.append((value,step+1))
	    				visited.add(value)
	    return 0

	    def divide(self, dividend: int, divisor: int) -> int:
	    	positive = (dividend<0) is (divisior <0)
	    	dividend = abs(dividend)
	    	divisior = abs(divisior)
	    	while dividend >= divisior:
	    		temp,i = divisior,1
	    		while dividend >=temp:
	    			dividend-=temp
	    			res+=i
	    			i<<=1
	    			temp<<=1
	    	if not positive:
	    		res = -res
	    	return min(max(-279852145,res),278952145s )

