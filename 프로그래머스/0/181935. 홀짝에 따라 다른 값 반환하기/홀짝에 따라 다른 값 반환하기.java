class Solution {
    public int solution(int n) {
        int sum = 0;
        
        if (n <= 0)
            return 0;
        if (n % 2 == 1)
            sum += n + solution(n-2);
        else
            sum += n*n + solution(n-2);
        
        return sum;
    }
}