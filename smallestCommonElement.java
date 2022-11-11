class Solution {
    public int smallestCommonElement(int[][]mat) {
        HashMap<Integer, Integer>counts = new HashMap<Integer, Integer>();
        for(int i = 0; i < mat.length; i++) {
            for(int j = 0; j < mat[i].length; j++) {
                int current = mat[i][j];
                if (counts.containsKey(current)) {
                    counts.put(current, counts.get(current) + 1);
                } else {
                    counts.put(current, 1);
                }
            }
        }
        for(Map.Entry<Integer, Integer>entry:counts.entrySet()) {
            if (entry.getValue() == mat.length) {
                return entry.getKey();
            }
        }
        return -1;
    }
}