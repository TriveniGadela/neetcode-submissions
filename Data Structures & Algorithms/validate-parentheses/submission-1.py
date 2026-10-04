class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                st.append(s[i])
            else:
                if len(st)==0:
                    return False
                a=st.pop()
                if (s[i]==')' and a!='(') or (s[i]==']' and a!='[') or (s[i]=='}'and a!='{'):
                    return False
        return len(st)==0