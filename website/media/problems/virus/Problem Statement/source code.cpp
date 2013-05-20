#include<iostream>
#include<cassert>
#include<string>
#include<cstdio>
#include<map>
#include<utility>
#include<cstdlib>
#include<vector>
#include<iomanip>
#include<algorithm>
#include<stack>
#include<queue>
#include<string>
#include<cstring>
#include<cctype>
#include<list>
#include<bitset>
#include<set>

using namespace std;

#define MAX_FAC 2000005
#define LL long long 
#define MOD 100002013
#define MAXQ 100000
#define MAXX 1000000
#define MAXY 1000000
#define MAXZ 2000000
#define MAXB 30

LL fac[MAX_FAC],invfac[MAX_FAC];

LL power_mod(LL a, LL p){
    LL ret=1;
    while(p){
        if(p&1){
            ret*=a;
            ret%=MOD;
        }
        a*=a;
        a%=MOD;
        p=(p>>1);
    }
    return ret;
}                

void pre(){
    fac[0]=1;
    LL i;
    for(i=1;i<MAX_FAC;i++)
    {
        fac[i] = fac[i-1]*i;
        fac[i] %= MOD;
    }    
    invfac[MAX_FAC-1]=power_mod(fac[MAX_FAC-1],MOD-2);
    for(i=MAX_FAC-2;i>=0;i--){
        invfac[i]=invfac[i+1]*(i+1);
        invfac[i]%=MOD;
    } 
}    

LL com(int n,int r){
    LL ret=fac[n];
    ret *= invfac[n-r];
    ret %= MOD;
    ret *= invfac[r];
    ret %= MOD;
    return ret;
}    

int main()
{
    clock_t tim=clock();
    int t,x,y,z;
    LL ans;
    pre();
    freopen("I3.txt","r",stdin);
    freopen("O3.txt","w",stdout);
    scanf("%d",&t);
    assert(t <= MAXQ);
    while(t--){
        scanf("%d%d%d",&x,&y,&z);
        assert(x<=MAXX && x>=-MAXX);
        assert(y<=MAXY && y>=-MAXY);
        assert(z<=MAXZ && z>=0);
        z++;
        if(x<0){
            x=-x;
        }
        if(y<0){
            y=-y;
        }
        if(x+y>z-1){
            printf("0\n");
        }
        else if((x+y)%2==(z-1)%2){
            ans=com(z-1,(z-1-(x+y))/2);
            ans*=com(z-1,(z+x-1-y)/2);
            if(ans>=MOD){
                ans%=MOD;
            }
            x=ans;
            printf("%d\n",x);    
        }
        else{
            printf("0\n");
        }                    
    }    
    tim=clock()-tim;
    //cout<<"Time - "<<float(tim)/float(CLOCKS_PER_SEC)<<endl;
    //system("pause");
    return 0;
}

