#include<iostream>
#include<vector>
using namespace std;

/**
 * Given an array of integers, return indices of the two numbers such that they add up to a specific target.

    You may assume that each input would have exactly one solution.

    Example: 
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9, 
    return [0, 1].
 */

class Solution{
public:
    vector<int> TwoSum(vector<int>& numbers,int target)
    {
        vector<int> result;
        int sum = 0;
        for(int i = 0 ; i < numbers.size(); i++)
        {
            for(int j = i + 1 ; j < numbers.size() ; j++)
            {
                sum = numbers[i] + numbers[j];
                if(sum == target)
                {
                    result.push_back(i+1);
                    result.push_back(j+1);
                    break;
                }
            }
        }

        return result;
    }
};

int main(void)
{
    vector<int> numbers;
    numbers.push_back(2);
    numbers.push_back(7);
    numbers.push_back(11);
    numbers.push_back(15);
    int target = 18;
    vector<int> result;
    Solution res;
    result = res.TwoSum(numbers,target);
    for(int i = 0 ; i < result.size(); i++)
    {
        if(i != result.size() - 1)
            cout<<result[i]<<",";
        else
            cout<<result[i]<<endl;
    }
    
    return 0;
}