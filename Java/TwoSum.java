import java.util.HashMap;
import java.util.Map;

public class TwoSum {
	public static void main(String[] args) {
		TwoSum t = new TwoSum();
		int[] numbers = {3,2,4};
		int target = 6;
		int[] res = t.twoSum(numbers, target);
		for(int i = 0 ; i < res.length; i++) {
			System.out.print(i == res.length - 1?res[i]:res[i]+",");
		}
	}
	
	public int[] twoSum(int[] numbers,int target) {
		Map<Integer, Integer> map = new HashMap<Integer,Integer>();
		for(int i = 0; i < numbers.length; i++) {// put all numbers to the map
			map.put(numbers[i], i);
		}
		
		for(int i = 0 ; i < numbers.length; i++) {
			int newtarget = target - numbers[i];
			if(map.containsKey(newtarget) && i != map.get(newtarget)) {
				return new int[] {i+1,map.get(newtarget) + 1};
			}
		}
		
		return null;
	}
}
