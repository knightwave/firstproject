#include<iostream>
#include<string>
using namespace std;

int main()
{
    int i=0,n,count=0;
    string s;
    cin>>n>>s;
    for(i=0;i<s.length()-2;i++)
    {
        if(s[i]==s[i+1])
        {
            count++;
        }
    }
    cout<<count<<endl;
    return 0;
}

