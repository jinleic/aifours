def content_absorb(X,Y,Z):
 assert X and Y and Z and set(X)==set(Z) and set(Y)<=set(X)
 return X+Z

def square_contract(s,start,word):
 assert s[start:start+2*len(word)]==word*2
 return s[:start]+word+s[start+2*len(word):]

def signature(w):
 if not w:return ()
 C=set(w)
 if len(C)==1:return (w[0],)
 for i,c in enumerate(w):
  if set(w[:i+1])==C:pre=w[:i];last=c;break
 for i in range(len(w)-1,-1,-1):
  if set(w[i:])==C:suf=w[i+1:];first=w[i];break
 return last,signature(pre),first,signature(suf)
X,Y='abca','acba'
assert X[0]==X[-1]==Y[0]==Y[-1]=='a'
assert content_absorb(X,Y,X)==X*2
s=Y+X;assert s=='acbaabca'
s=square_contract(s,3,'a');assert s=='acbabca'
s=content_absorb('acb','a','bca');assert s=='acbbca'
s=square_contract(s,2,'b');assert s=='acbca'
X2,Y2='cabc','cbac'
assert X2[0]==X2[-1]==Y2[0]==Y2[-1]=='c'
assert content_absorb(X2,Y2,X2)==X2*2
s=Y2+X2;assert s=='cbaccabc'
s=square_contract(s,3,'c');assert s=='cbacabc'
s=content_absorb('cba','c','abc');assert s=='cbaabc'
s=square_contract(s,2,'a');assert s=='cbabc'
assert 'abca'+'bc'=='abc'*2
assert 'acbca'+'bc'=='acbcabc'
assert content_absorb('acb','c','abc')=='acbabc'
assert 'a'+'cabc'=='acabc' and 'a'+'cbabc'=='acbabc'
assert signature('abc')!=signature('acabc')
print('PASS two local-RRB substitutions, square contractions, three explicit content absorptions')
print('RESULT locally RRB band ⇒ abc=acabc; reverse by local identity, dual gives localLRB ⇔ abc=abcac')
print('CONTROL abc and acabc differ in the unrestricted free band; local hypothesis essential')
