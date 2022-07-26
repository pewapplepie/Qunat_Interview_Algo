"""

There is a crowdfunding project hthat you want to support. This project
gives the same reward to every supporter, with one peculiar condition:
the amount you pledge must not be equal to any earlier pledge amount

you are given a list of amounts pledged so far in an array of integers.
You know that there is less than 100,000 of pledgges and the max amount pledged is less than 1,000,000

Implement a function find_min_pledge(pledge_list) that will return 
the amount you should pledge

eg
[1,3,6,4,1,2] => 5
[1,2,3] => 4
[-1,-3] ==> 1
"""

def find_min_pledge(pledge_list):
    for i in range(len(pledge_list)):
        while 0 <= pledge_list[i]-1 < len(pledge_list) and pledge_list[pledge_list[i]-1] != pledge_list[i]:
            tmp = pledge_list[i]-1
            pledge_list[i], pledge_list[tmp] = pledge_list[tmp], pledge_list[i]
        print(pledge_list)
        print("---")
    print(pledge_list)
    for i in range(len(pledge_list)):
        if pledge_list[i] != i+1:
            return i+1
    return len(pledge_list)+1

# find_min_pledge([1,3,6,4,1,2])
find_min_pledge([3,4,1,5,2,1])