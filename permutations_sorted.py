

def all_perms(s):
    if len(s) <= 1:
        yield s
    else:
        for i in range(len(s)):
            #for p in permutations(s[:i] + s[i+1:]):
            for p in all_perms(s[:i] + s[i+1:]):
                yield s[i] + p

for i in all_perms('ABCD'):
  print i
