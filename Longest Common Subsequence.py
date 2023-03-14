'''
Given two strings s1 and s2, find the length of the longest subsequence that is common to both strings.
'''


def longest_common_subsequence(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]
  
  '''
  In the above code, we first initialize a 2D list dp of size (m+1) 
  x (n+1) where m and n are the lengths of s1 and s2 respectively. We 
  then iterate over the two strings and fill in the dp table according to the following recurrence relation:
  '''
  
  
  '''
  dp[i][j] = dp[i-1][j-1] + 1    if s1[i-1] == s2[j-1]
           max(dp[i-1][j], dp[i][j-1])    otherwise
           
           The final answer is stored in dp[m][n].
  '''
  
  
