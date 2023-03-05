class Solution {
public:
    int mySqrt(int x) {
        long i=0;
        if(x==0||x==1)
         return x;
       for(;i<=x;i++)
       {
           if(i*i==x)
            return i;
            if(i*i>x) return i-1;
       } 
       return i;
    }
};
