import java.util.Arrays;

public class Maxdist{
    public static void main(String[] args) {
        int[] arr = {6, 7, 9, 11, 13, 15};
        int n = arr.length;
        int k = 4;
        
        System.out.println(maxMinDistance(arr, n, k));
    }
    public static int maxMinDistance(int[] arr,int n,int k){
        Arrays.sort(arr);        
        int low = 1;
        int high = arr[n - 1] - arr[0];
        int result = 0;        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (canPlaceCows(arr, n, k, mid)) {
                result = mid;
                low = mid + 1;
            } 
            else 
                high = mid - 1; 
        }
        return result;
    }
    public static boolean canPlaceCows(int[] arr, int n, int k, int dist) {
        int count=1;  
        int lastPosition=arr[0];
        for (int i = 1;i<n;i++) {
            if (arr[i] - lastPosition>=dist) {
                count++;
                lastPosition=arr[i];
                if (count==k) {
                    return true;
                }
            }
        }
        return false;
    }
}
