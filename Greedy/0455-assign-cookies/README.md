## Approach

so the idea is greed g[gp], must be <= s[sp] to fit (ans+=1), so sort in asc order skip cookies with lesser size than the greed. 

TC = o(g log g) + o(s log s)
SC = o(1)
