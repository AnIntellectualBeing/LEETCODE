class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int majority=0,count=0;
        for( auto it:nums)
        {
            if(count==0)
            { majority = it; }

            if(majority == it) count++; 
            else count--; 
        }
        return majority;
    }
};
