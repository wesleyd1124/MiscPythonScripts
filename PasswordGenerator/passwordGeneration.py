
def getList(keywords, length=None):
	combinationLengths = length
	if(length == None):
		combinationLengths = len(keywords)
	passwords = []
	for x in range(2):
		for keywordNum in range(combinationLengths):
			for keyword in keywords:
				indexOfKeyword = keywords.index(keyword)
				adjKeys = keywords[:]
				del(adjKeys[indexOfKeyword])
				password = keyword
				for i in range(keywordNum):
					if (x == 0):
						password = password + adjKeys[i]
					elif(x == 1):#If the password can have some kind of catchy combination
						if(password[-1] == adjKeys[i][0]):
							password = password + adjKeys[i][1:]
						else:
							password = password + adjKeys[i]
				if(password not in passwords):
					passwords.append(password)

	return passwords
