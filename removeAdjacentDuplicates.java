class Solution {
    public String removeDuplicates(String s) {
        Stack stack = new Stack();
        for(int i = 0; i < s.length(); i++) {
            char current = s.charAt(i);
            if(!stack.isEmpty() && stack.peek().equals(current)) {
                stack.pop();
            }
            else {
                stack.push(current);
            }
        }
        StringBuilder result = new StringBuilder();
        while(!stack.isEmpty()) {
            result.insert(0,stack.pop());
        }
        return result.toString();
    }
}