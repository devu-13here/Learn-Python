#include <iostream>
using namespace std;
/*
int main() {
    int num[] = {1, 2, 3, 4, 5, 6, 7, 8, 9,10};
    int n = sizeof(num) / sizeof(num[0]);
    
    int sum = 0;
    int oddSum = 0;
    int evenSum = 0;
    
    for (int i = 0; i < n; i++) {
        sum += num[i];
        if (i % 2 == 0) {
            evenSum += num[i];
        } else {
            oddSum += num[i];
        }
    }
    
    cout<<sum<<endl;
    cout<<evenSum<<endl;
    cout<<oddSum<<endl;
     return 0;
}
*/

/*
int main()
{
  int num1[]={1,2,3,4,5,6,7};
  int num2[]={4,5,19,78};
   int n1 = sizeof(num1) / sizeof(num1[0]);
   int n2 = sizeof(num2) / sizeof(num2[0]);
  
  
  for (int i=0; i < n1 ; i++){
     for(int j =0 ; j < n2 ; j++){
     
       if (num1[i] == num2[j])
       cout<<num1[i]<<endl;
}
}
   return 0;
}
*/
int main()
{
	int num1[5][5]={{1,2,3,4,5},{6,7,8,9,10},{11,12,13,14,15},{16,17,18,19,20},{21,22,23,24,25}};
	int i,j;
	
	int sum1=0;
	int sum2=0;
	for(int i=0 ; i < 5 ; i++){
	   for(int j =0 ; j < 5 ; j++){
	      if (i==j)
	        {
			cout<<num1[i][j]<<endl;
	        sum1 += num1[i][j];}
	      if ( (i+j)== 4)
	      {
		    cout<<num1[i][j]<<endl;
	        sum2 += num1[i][j]; }
	        
	    
}
		  
		  }
		  	int isum1=0;	 
		  for(int i=0 ; i < 5 ; i++){
		   if (i%2 == 0)	  
		   for(int j =0 ; j < 5 ; j++){   
		   cout<<num1[i][j]<<endl;
	        isum1 += num1[i][j];}
	        else
	        cout<<num1[i][j]<<endl;
	        isum1 += num1[i][j];}
		  return 0;  
}
