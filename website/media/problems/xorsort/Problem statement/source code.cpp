#include<cstdio>
#include<cassert>
#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;

#define LL long long
#define MAXN 1000
#define MAXB 60
#define MAXC 200
#define MAXNUM 1000000000000000000LL

int N;
LL arr[MAXN];
bool cut[MAXN+1],myset[MAXN+1];

LL findGoodNumber()
{
    LL ret = 0;
    for(int i=0;i<=N;i++) cut[i] = 0;
    cut[N] = true;
    for(int b=MAXB-1;b>=0;b--){
        for(int i=0;i<N;i++){
            myset[i] = ((arr[i] & (1LL<<b)) > 0);
        }
        int change = 0;
        int startsWith = myset[0];
        int endsWith = -1;
        int pattern = -1;
        for(int i=0;i<N;i++){
            if(cut[i+1]){
                endsWith = myset[i];
                if(change > 1){
                    //printf("change is more than 1 at %d bit\n", b);
                    return -1;
                }
                if(change == 1){
                    if(startsWith == 0){
                        if(pattern == 1){
                            //printf("pattern was zero till now for %d bit\n", b);
                            return -1;
                        }
                        else pattern = 0;
                    }
                    else{
                        if(pattern == 0){
                            //printf("pattern was one till now for %d bit\n", b);
                            return -1;
                        }
                        else pattern = 1;
                    }
                }
                change = 0;
                startsWith = myset[i+1];
            }
            else{
                change += (myset[i] ^ myset[i+1]);
            }
        }
        if(pattern == 1){
            //printf("flipping at %d\n", b);
            ret = ret | (1LL<<b);
        }
        for(int i=0;i<N;i++){
            if(!cut[i+1]){
                if(myset[i] ^ myset[i+1]){
                    //printf("making %d a cut\n", i+1);
                    cut[i+1] = true;
                }
            }
        }
    }
    return ret;
}

int main()
{
    //freopen("input0.txt", "r", stdin);
    //freopen("output0.txt", "w", stdout);
    int cases;
    scanf("%d", &cases);
    assert(cases <= MAXC);
    while(cases--){
        scanf("%d", &N);
        assert(N <= MAXN);
        for(int i=0;i<N;i++){
            scanf("%lld", &arr[i]);
            assert(arr[i] <= MAXNUM);
        }
        LL ans = findGoodNumber();
        if(ans != -1) for(int i=0;i<N-1;i++) assert((arr[i] ^ ans) < (arr[i+1] ^ ans));
        printf("%lld\n", ans);
    }
    return 0;
}
