#include <stdio.h>
int main()
{
    int arr[10],i,key,n;
    printf("Enter the array size:\n");
    scanf("%d",&n);
    printf("Enter the array:\n");
    for(i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    printf("Enter the array to be searched:\n");
    scanf("%d",&key);
    for(i=0;i<n;i++){
        if(key==arr[i]){
            printf("The element is present in index: %d",i);
            break;
        }    
    }
}
