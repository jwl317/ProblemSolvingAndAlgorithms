import random

def bub(ds):
    for a in range(len(ds)-1):
        for b in range(len(ds)-a-1):
            if ds[b] > ds[b+1]:
                ds[b], ds[b+1] = ds[b+1], ds[b]

dataset = []
for a in range(15):
    dataset.append(random.randint(1,15))

print("Before bubblesort:")
print(dataset)

print("After bubblesort:")
bub(dataset)
print(dataset)

            
