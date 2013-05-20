#include <algorithm>
#include <cmath>
#include <cstdio>
#include <ctime>
#include <deque>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <stdlib.h>
#include <string>
#include <vector>
 
using namespace std;
 
#define LL long long
#define LD long double
 
#define VI vector<int>
 
#define sd(x) scanf("%d",&x)
 
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define PI pair< int , int >
#define PIP pair< int , PI >
#define MAXN 10000
#define maX(a,b) (a>b?a:b)
 
PI wrt1[MAXN],t[3],temp,ship[MAXN];
PIP wrt0[MAXN];
int p[3],maxarr[MAXN+1],x,y,i,j,vis[MAXN],n;
 
inline int dist(PI p , PI q){
    x = p.F-q.F;
    y = p.S-q.S;
    if(x < 0){
        x = -x;
    }
    if(y < 1){
        y = -y;
    }
    return x+y;
}
 
void verify(){
    for(int i=0;i<n;i++){
        if(dist(t[0],ship[i]) <= p[0]){
            vis[i] = 1;
        }
        if(dist(t[1],ship[i]) <= p[1]){
            vis[i] = 1;
        }
        if(dist(t[2],ship[i]) <= p[2]){
            vis[i] = 1;
        }
        if(vis[i] == 0){
            cout<<"Ship["<<i<<"] is going to drown in the sea.."<<endl;
            return ;
        }
    }
}
 
inline void swapthem(PI &l, PI &r){
    temp = l;
    l = r;
    r = temp;
}
 
inline void check(int p0,int k){
    for(j = k; j > 0; --j){
        if(wrt1[j] < wrt1[j-1]){
            temp = wrt1[j];
            wrt1[j] = wrt1[j-1];
            wrt1[j-1] = temp;
        }
    }
    maxarr[k+1]=0;
    for(j = k;j >= 0; --j){
        if(maxarr[j+1] + wrt1[j].F + p0 < p[0] + p[1] + p[2]){
            p[0] = p0;
            p[1] = wrt1[j].F;
            p[2] = maxarr[j+1];
        }
        maxarr[j] = maX(maxarr[j+1], wrt1[j].S);
    }
    if(maxarr[0]+ p0 < p[0] + p[1] + p[2]){
        p[0] = p0;
        p[1] 
        p[2] = maxarr[0];
    }
}
 
int main(){
    //freopen("input1.txt","r",stdin);
    //freopen("output1.txt","w",stdout);
    //clock_t tt = clock();
    cin>>t[0].F>>t[0].S;
    cin>>t[1].F>>t[1].S;
    cin>>t[2].F>>t[2].S;
    cin>>n;
    int i,j;
    for(i = 0 ;i < n; i++){
        scanf("%d%d",&ship[i].F,&ship[i].S);
    }
    for(i = 0 ;i < n; i++){
        wrt0[i].F = dist(t[0],ship[i]);
        wrt0[i].S.F = dist(t[1],ship[i]);
        wrt0[i].S.S = dist(t[2],ship[i]);
    }
    sort(wrt0,wrt0+n);
    p[0]=wrt0[n-1].F;
    p[1]=0;
    p[2]=0;
    for(i=n-2;i>=0;i--){
        wrt1[n-2-i]=wrt0[i+1].S;
        check(wrt0[i].F,n-2-i);
    }
    wrt1[n-1]=wrt0[0].S;
    check(0,n-1);
    cout<<p[0]+p[1]+p[2]<<endl;
    //verify();
    //tt = clock() - tt;
    //cout<<"Time - "<<float(tt)/float(CLOCKS_PER_SEC)<<endl;
    //system("pause");
    return 0;
}