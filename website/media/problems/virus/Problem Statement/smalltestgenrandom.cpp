#include <algorithm>
#include <cmath>
#include <cstdio>
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

#define SEED 1231
#define MAXQ 1000
#define MAXX 100
#define MAXY 100
#define MAXZ 200
#define MAXB 30


int getRandom(int MOD){
    int ret=0;
    for(int i=0 ; i < MAXB ; i++){
        if(rand() & 1){
            ret = ret | (1<<i);
        }
    }
    ret %= (MOD+1);
    if(rand() & 1)
        ret = -ret;       
    return ret;
}   

int getRandom2(int MOD){
    int ret=0;
    for(int i=0 ; i < MAXB ; i++){
        if(rand() & 1){
            ret = ret | (1<<i);
        }
    }
    ret %= (MOD+1);       
    return ret;
}    
                      
int main(){
    freopen("I4.txt","w",stdout);
    cout<<MAXQ<<endl;
    for(int query=0;query < MAXQ;query++){
        cout<<getRandom(MAXX)<<" "<<getRandom(MAXY)<<" "<<getRandom2(MAXZ)<<endl;    
    }    
    return 0;
}



