
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class MergeIntervals {
    public static List<int[]> merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        List<int[]> merged = new ArrayList<>();
        merged.add(intervals[0]);

        for (int i = 1; i < intervals.length; i++) {
            int[] lastInterval = merged.get(merged.size() - 1);
            if (intervals[i][0] <= lastInterval[1]) {
                lastInterval[1] = Math.max(lastInterval[1], intervals[i][1]);
            } else {
                merged.add(intervals[i]);
            }
        }

        return merged;
    }

    public static void main(String[] args) {
        int[][] intervals = {{1, 3}, {2, 6}, {8, 10}, {15, 18}};
        List<int[]> result = merge(intervals);
        for (int[] interval : result) {
            System.out.println("[" + interval[0] + ", " + interval[1] + "]");
        }
    }
}
