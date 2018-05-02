#include <bits/stdc++.h>
#include <stdio.h>
#include <stdlib.h>
#include <queue>

using namespace std;

int main(){
    int i,n,d,aux;
    std::queue<int> myqueue;
    scanf("%d",&n);
    scanf("%d",&d);
    for(i=0;i<n;++i){
        scanf("%d",&aux);
        myqueue.push(aux);
    }
    for(i=0;i<d;++i){
        aux = myqueue.front();
        myqueue.pop();    
        myqueue.push(aux);
    }
    for(i=0;i<n-1;++i){
        printf("%d ",myqueue.front());
        myqueue.pop();    
    }
    printf("%d",myqueue.front());
    return 0;
}