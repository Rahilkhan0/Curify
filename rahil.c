#include<stdio.h>


int main(){
    int arr[]={9,5,7,2,1};
    int n;
    n =sizeof(arr)/sizeof(arr[0]);
    array(arr,n);
    Selection(arr,n);
    array(arr,n);
    return 0;

}

//void swap(int *x, int *y){

// int temp=*x;
    //*x=*y;
  //  *y=temp;



 void Selection(int arr[],int n){
    int i,j,min;
    for(i=0;i<n-1;i++){
        min=i;
    

    
    for (j=i+1;j<n;j++){
        if(arr[min]> arr[i]){
            min=j;
        }
    

    
    }
    int temp=arr[i];
    arr[i]=arr[min];
    arr[min]= temp;

    }


 }
    

 int array( int arr[],int n){
    for( int i=0;i<n;i++){
        printf("%d",arr[i]);
        printf("\n");

    }
 }