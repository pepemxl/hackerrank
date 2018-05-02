#include <stdio.h>
#include <stdlib.h>


int main(int argc,char *argv[]){
    int i,j,n,m;
    double max,sum;
    int **queries,*list;
    scanf("%d",&n);
    scanf("%d",&m);
    //printf("%d %d",n,m);
    queries = (int **) malloc(m*sizeof(int*));
    for(i=0;i<m;++i){
        queries[i] = (int *)malloc(3*sizeof(int));
    }
    list = (int *)malloc((n+1)*sizeof(int));
    for(i = 0;i < n+1;++i){
        list[i] = 0;
    }
    for(i = 0;i < m;++i){
        for(j = 0;j < 3;++j){
            scanf("%d",&queries[i][j]);
            //printf("%d ",queries[i][j]);
        }
        //printf("\n");
    }
    for(i = 0;i < m;++i){
        list[queries[i][0]-1] += queries[i][2];
        list[queries[i][1]]   -= queries[i][2];
    }
    //printf("%d %d %d %d %d %d\n",list[0],list[1],list[2],list[3],list[4],list[5]);
    max = 0;
    sum = 0;
    for(i=0;i<n;++i){
        sum += list[i];
        if(sum > max){
            max = sum;
        }
    }
    printf("%.0lf",max);
    for(i=0;i<m;++i){
        free(queries[i]);
    }
    free(queries);
    return 0;
}
