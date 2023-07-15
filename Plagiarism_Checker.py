def calculate_similarity(text1, text2):
    text1 = text1.lower()
    text2 = text2.lower()
    rows = len(text1) + 1
    cols = len(text2) + 1
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        dp[i][0] = i
    for j in range(cols):
        dp[0][j] = j
    for i in range(1, rows):
        for j in range(1, cols):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + 1)
    max_length = max(len(text1), len(text2))
    similarity = (max_length - dp[rows-1][cols-1]) / max_length
    return similarity
def check_plagiarism(text1, text2, threshold=0.8):
    similarity = calculate_similarity(text1, text2)
    if similarity >= threshold:
        return f"Plagiarism detected! Similarity: {similarity * 100:.2f}%"
    else:
        return f"No plagiarism detected. Similarity: {similarity * 100:.2f}%"
text1 = input("Type the first text: ")
#"The cat is on the mat."
text2 = input("Type the second text:")
#"The dog is on the mat."
result = check_plagiarism(text1, text2)
print(result)