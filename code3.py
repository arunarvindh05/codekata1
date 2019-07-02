c=str(input())
if((c>='a')and(c<='z'))or((c>='A')and(c<='Z')):
  if((c=='a')or(c=='A')or(c=='e')or(c=='E')or(c=='i')or(c=='I')or(c=='o')or(c=='O')or(c=='u')or(c=='U')):
    print("Vowel")
  
  else:
    print("Consonant")
else:
  print("invalid")
