/* here we generate test cases which are extremely large */

#include<set>
#include<vector>
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cassert>
#include<cstdio>
using namespace std;

#define SEED 2014
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
    srand(SEED);
    freopen("input4.txt", "w", stdout);
    int cases = MAXC; //getRandom(MAXC);
    printf("%d\n", cases);
    while(cases--){
        int N = MAXN;//getRandom(SMALLMAXN);
        printf("%d\n", N);
        set<LL> myset;
        LL key = getRandomNumber();
        while(myset.size() < N){
            LL curr = getRandomNumber();
            if((curr ^ key) <= MAXNUM && myset.find(curr) == myset.end()){
                myset.insert(curr);
            }
        }
        for(set<LL>::iterator it=myset.begin();it!=myset.end();it++){
            printf("%lld ", (*it) ^ key);
        }printf("\n");
    }
    return 0;
}
