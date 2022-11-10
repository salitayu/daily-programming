class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<Integer> stack = new Stack<Integer>();
        int temperaturesLength = temperatures.length;
        int[] ans = new int[temperaturesLength];
        
        for(int i = 0; i < temperaturesLength; i++) {
            int current = temperatures[i];
            // pop till current day's temperature isn't warmer than temperature at top of stack
            while (!stack.isEmpty() && temperatures[stack.peek()] < current) {
                int previous = stack.pop();
                ans[previous] = i - previous;
            }
            stack.push(i);
        }
        return ans;
    }
}