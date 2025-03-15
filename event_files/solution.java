package event_files;
import java.io.*;
import java.util.*;

public class solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());
        int[] stalls = Arrays.stream(br.readLine().trim().split("\\s+"))
                             .mapToInt(Integer::parseInt)
                             .toArray();
        int k = Integer.parseInt(br.readLine().trim());

        System.out.println(maxMinDistance(stalls, n, k));
    }

    private static int maxMinDistance(int[] stalls, int n, int k) {
        Arrays.sort(stalls);
        int low = 1, high = stalls[n - 1] - stalls[0], result = 0;

        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (canPlaceCows(stalls, n, k, mid)) {
                result = mid;
                low = mid + 1; 
            } else {
                high = mid - 1; 
            }
        }
        return result;
    }

    private static boolean canPlaceCows(int[] stalls, int n, int k, int minDist) {
        int cowsPlaced = 1, lastPos = stalls[0];

        for (int i = 1; i < n; i++) {
            if (stalls[i] - lastPos >= minDist) {
                cowsPlaced++;
                lastPos = stalls[i];

                if (cowsPlaced == k) return true;
            }
        }
        return false;
    }
}
