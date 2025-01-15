
import java.util.Arrays;
import java.util.Comparator;

public class NonOverlappingIntervals {
    public static int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, Comparator.comparingInt(a -> a[0]));
        
        int prev_end = intervals[0][1];
        int count = 0;
        
        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i][0] < prev_end) {
                count++;
                prev_end = Math.min(prev_end, intervals[i][1]);
            } else {
                prev_end = intervals[i][1];
            }
        }

        return count;
    }

    public static void main(String[] args) {
        int[][] intervals = {{1, 2}, {2, 3}, {3, 4}, {1, 3}};
        System.out.println(eraseOverlapIntervals(intervals));
    }
}
