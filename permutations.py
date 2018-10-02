def permutations(string):
    array = []
    if len(string) <= 1:
        array.append(string)
    else:
        for perm in permutations(string[1:]):
            for i in range(len(string)):
                array.append(perm[:i] + string[0:1] + perm[i:])
    return array

print(permutations('abcd'))
