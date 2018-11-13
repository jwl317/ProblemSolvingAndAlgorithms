import random

def quick(ds):
    if len(ds) < 2:
        return ds
    else:
        key = ds[0]
        left = [i for i in ds[1:] if i <= key]
        right = [i for i in ds[1:] if i > key]
        return quick(left) + [key] + quick(right)


dataset = []
for a in range(15):
    dataset.append(random.randint(1,15))

print("Before quicksort:")
print(dataset)

print("After quicksort:")
print(quick(dataset))

            
