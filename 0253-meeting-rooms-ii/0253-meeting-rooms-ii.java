
import java.util.Arrays;

public class MeetingRooms {
    public static int minMeetingRooms(int[][] intervals) {
        int[] start_times = new int[intervals.length];
        int[] end_times = new int[intervals.length];
        
        for (int i = 0; i < intervals.length; i++) {
            start_times[i] = intervals[i][0];
            end_times[i] = intervals[i][1];
        }
        
        Arrays.sort(start_times);
        Arrays.sort(end_times);
        
        int start_pointer = 0, end_pointer = 0, used_rooms = 0, max_rooms = 0;

        while (start_pointer < intervals.length) {
            if (start_times[start_pointer] < end_times[end_pointer]) {
                used_rooms++;
                start_pointer++;
            } else {
                used_rooms--;
                end_pointer++;
            }
            max_rooms = Math.max(max_rooms, used_rooms);
        }

        return max_rooms;
    }

    public static void main(String[] args) {
        int[][] intervals = {{0, 30}, {5, 10}, {15, 20}};
        System.out.println(minMeetingRooms(intervals));
    }
}
