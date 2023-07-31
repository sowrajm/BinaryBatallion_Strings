class Solution(object):
    def longestValidParentheses(self, s):
        x=0
        s=list(s)
        f=[]
        z=0
        q=0
        for _ in s:
            if s[x]=="(":
                s[x]=1
                z=1

            else:
                s[x]=-1
                q=1
            x=x+1
        x=0
        w=0
        c=[]
        if z==0 or q==0:
            return 0
        x=0
        for _ in s:
            y=0
            d=1
            p=1
            if s[x]==-1:
                x=x+1
            else:
                for _ in range( 0,len(s)-x-1):
                    
                    d=d+s[y+x+1]
                    if d<=0:
                        f.append (y+2)       
                        if d<0:
                            break                    
                    y=y+1
                if d==1 and s[y+x]==1:
                    c.append([x,y-1])
                
                if d==-1 or d==0:
                    c.append([x,y])
                x=x+1
        print(f)
        x=0
        k=0
        
        if len(c)==0:
            return (0)
        for _ in c:
            l=c[x][1]
            if l>k:
                k=l+1
                
            x=x+1
        print(k)
        
        if len(f)>0:
            
            x=0
            for _ in f:
                if f[x]%2!=0:
                    f[x]=f[x]-1
                if k<f[x]:
                    k=f[x]
                x=x+1
            
        return(k)
        

