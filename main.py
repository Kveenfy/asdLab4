graph = {}
with open("graph.txt", "r") as f:
    for line in f:
        key, *value = line.split()
        graph[key] = value
print(graph)

matrix=[]
for i in range(len(graph)):
    matrix.append(0)
result =""

for key1 in graph.keys():
    for value in graph.get(key1):
        i = 0
        for key2 in graph.keys():
            if key2 == value:
                matrix[i]=1
            i+=1
    result+= str(matrix) +"\n"
    for i in range(len(matrix)):
        matrix[i]=0
print(result)
with open("result.txt", "w") as f:
    f.write(result)

