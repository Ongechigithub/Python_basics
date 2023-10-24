jina = "python expt"
for j in jina:
    if (j != 2):
        print(j)
x = ["python", "exception", "try and except"]

try:
    for i in range(4):
        print(f"The index and elements from list is {i, x[i]}")
except:
    print("index out of range")

