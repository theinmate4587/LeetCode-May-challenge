c1=collections.Counter(ransomNote)
c2=collections.Counter(magazine)
        
for x,y in c1.items():
  if c2[x]<y:
    return False
return True
