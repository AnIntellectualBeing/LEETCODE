class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int majority1=-4,majority2=-4,c1=0,c2=0;

        for(int i=0;i<nums.size();i++)
        {
            if(majority1==nums[i]){
                 c1++; }
            else if(majority2==nums[i]){
                 c2++; }
            else if(c1==0){
                majority1=nums[i];
                c1=1;
            }
            else if(c2==0) {
                majority2=nums[i];
                c2=1;
            }
            else {
                c1--;
                c2--;
            }
        }
        vector<int> v;
        int count1=0;
        int count2=0;
        for(int i=0;i<nums.size();i++)
        {
            if(majority1==nums[i]) count1++;
            if(majority2==nums[i]) count2++;
        }
        if(count1 > nums.size()/3)
        {
            v.push_back(majority1);
        }
        if(count2 > nums.size()/3){
            v.push_back(majority2);
        }

        return v;
        
    }
};
