#Remove duplicate elements from the list.

res=[2,4,2,3,5,2,6,5,2,2,7];

def duprm(ar):
	nu=[]; #temp array to store duplicate values;
	if isinstance(ar,list): #check if the given argument is list of not
		for x in range(len(ar)-1):
			if res.index(ar[x])-ar.index(ar[x+1])>=0:	#by subtacting index of 1st element by 2nd gives the result in positive of negative if negative then its not duplicate and if its positive then the element was appeard before hence its duplicate;
				
				nu.append(ar[x+1]);	#storing it in temp list;
		for x in nu:
			res.pop(ar.index(x)); #removing element that are duplicate
		return ar;
	else:
		print('This function Expect list as an argument!');

print(duprm(res));
