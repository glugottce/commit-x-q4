import java.util.Arrays;
import java.util.Scanner;
import java.util.*;

class Solution{

    public static boolean isPossible(int[] arr,int mid,int k){
        int count=1;
        int last=arr[0];
        for(int i=1;i<arr.length;i++){
            if(arr[i]-last>=mid){
                count++;
                last=arr[i];
                if(count==k){
                    return true;
                }
            }
        }
        return false;
    }

    public static int maxMinDistance(int[] arr,int k){
        Arrays.sort(arr);
        int max=arr[arr.length-1]-arr[0];
        int low=1;
        int res=0;
        while(low<=max){
            int mid=(low+max)/2;
            if(isPossible(arr,mid,k)){
                res=mid;
                low=mid+1;
            }else{
                max=mid-1;
            }
        }
        return res;

        
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int[] arr=new int[n];
        for(int i=0;i<n;i++){
            arr[i]=sc.nextInt();
        }
        int k=sc.nextInt();

        System.out.print(maxMinDistance(arr,k));
        
    }
}