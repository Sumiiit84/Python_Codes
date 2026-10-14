import java.util.*;

/*
 * 
 * 
 * class time_complexity {
 * public static void main(String[] args) {
 * int arr[] = { 1, 2, 3, 4, 5 };
 * System.out.println(arr[0]);
 * }
 * }
 */
// This is a o(1) time complexity because accessing one element by index takes
// constant time.
/**
 * time_complexity
 */
/*
 * public class time_complexity {
 * 
 * public static void main(String[] args) {
 * int arr[] = { 1, 2, 3, 4, 5 };
 * for (int i = 0; i <= arr.length; i++) {
 * System.out.println(arr[i]);
 * }
 * }
 * }
 */
// this is a O(n) time complexity because it is iterate each elements

class time_complexity {
    public static void main(String[] args) {
        int arr[] = { 1, 2, 3, 4, 5 };
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j <= i; j++) {
                System.out.println(j);
            }
        }
    }
}
// This is a O(n^2) time complexity