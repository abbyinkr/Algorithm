class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        String answer = "";
        
        // String start = my_string.substring(0, s);
        // String end = my_string.substring(s+overwrite_string.length());
        // return start + overwrite_string + end;
        
        // char to Array 와 반복문을 사용
        char[] my_char = my_string.toCharArray();
        char[] overwrite_char = overwrite_string.toCharArray();
        
        for (int i=0; i<overwrite_char.length; i++) 
            my_char[s + i] = overwrite_char[i];
        
        return new String(my_char);
    }
}