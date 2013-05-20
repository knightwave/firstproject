/* here we generate random sequences of length <= SMALLMAXN */

#include<set>
#include<vector>
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cassert>
#include<cstdio>
using namespace std;

#define LL long long
#define MAXN 1000
#define SMALLMAXN 10
#define MAXB 60
#define MAXC 200
#define MAXNUM 1000000000000000000LL

int getRandom(int n)
{
    return (1+(rand()%n));
}

LL getRandomNumber()
{
    LL ret = 0;
    for(int i=0;i<MAXB;i++){
        if(rand() & 1){
            ret = ret | (1LL<<i);
        }
    }
    return (ret <= MAXNUM) ? ret : getRandomNumber();
}

int main()
{
    srand(789);
    freopen("input1.txt", "w", stdout);
    int cases = MAXC; //getRandom(MAXC);
    printf("%d\n", cases);
    while(cases--){
        int N = getRandom(SMALLMAXN);
        printf("%d\n", N);
        set<LL> myset;
        while(myset.size() < N){
            LL curr = getRandomNumber();
            if(myset.find(curr) == myset.end()){
                myset.insert(curr);
            }
        }
        vector<LL> arr;
        for(set<LL>::iterator it=myset.begin();it!=myset.end();it++){
            arr.push_back(*it);
        }
        random_shuffle(arr.begin(), arr.end());
        for(int i=0;i<arr.size();i++) printf("%lld ", arr[i]); printf("\n");
    }
    return 0;
}
