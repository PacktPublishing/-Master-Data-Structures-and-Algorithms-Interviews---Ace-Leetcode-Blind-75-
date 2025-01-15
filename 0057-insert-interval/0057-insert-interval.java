
import java.util.ArrayList;
import java.util.List;

public class InsertInterval {
    public static List<int[]> insert(int[][] intervals, int[] newInterval) {
        List<int[]> left = new ArrayList<>();
        List<int[]> right = new ArrayList<>();
        int start = newInterval[0], end = newInterval[1];

        for (int[] i : intervals) {
            if (i[1] < start) {
                left.add(i);
            } else if (i[0] > end) {
                right.add(i);
            } else {
                start = Math.min(start, i[0]);
                end = Math.max(end, i[1]);
            }
        }

        List<int[]> result = new ArrayList<>();
        result.addAll(left);
        result.add(new int[] { start, end });
        result.addAll(right);

        return result;
    }

    public static void main(String[] args) {
        int[][] intervals = {{1, 3}, {6, 9}};
        int[] newInterval = {2, 5};
        List<int[]> result = insert(intervals, newInterval);
        for (int[] interval : result) {
            System.out.println("[" + interval[0] + ", " + interval[1] + "]");
        }
    }
}
