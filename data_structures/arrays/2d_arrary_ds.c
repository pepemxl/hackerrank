#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>


int main(){
    int arr[6][6];
    int suma,max_suma=-70;
    for(int arr_i = 0; arr_i < 6; arr_i++){
       for(int arr_j = 0; arr_j < 6; arr_j++){
          scanf("%d",&arr[arr_i][arr_j]);
       }
    }
    for(int arr_i = 0; arr_i < 4; arr_i++){
       for(int arr_j = 0; arr_j < 4; arr_j++){
          suma = arr[arr_i][arr_j]+arr[arr_i][arr_j+1]+arr[arr_i][arr_j+2];
          suma = suma + arr[arr_i+1][arr_j+1];
          suma = suma + arr[arr_i+2][arr_j]+arr[arr_i+2][arr_j+1]+arr[arr_i+2][arr_j+2];
          if(suma > max_suma){
              max_suma = suma;
          }
       }
    }
    printf("%d",max_suma);
    return 0;
}
