
keys = ['First Name','Last Name','Email']
values = ['Coding','Mente','codingmente@gmail.com','test']

dict1 = {}
for i in keys:
	for j in values:
		dict1[str(i)] = j
		values.remove(j)
		break

print(dict1)
