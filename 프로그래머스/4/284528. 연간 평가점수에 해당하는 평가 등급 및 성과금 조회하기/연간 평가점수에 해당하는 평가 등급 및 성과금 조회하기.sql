
WITH GRADES AS (
    SELECT 
        EMP_NO, 
        CASE
            WHEN AVG(SCORE) >= 96 THEN "S"
            WHEN AVG(SCORE) >= 90 THEN "A"
            WHEN AVG(SCORE) >= 80 THEN "B"
            ELSE "C"
        END GRADE
    FROM HR_GRADE
    GROUP BY EMP_NO
)
SELECT  A.EMP_NO, A.EMP_NAME, B.GRADE, 
        CASE
            WHEN GRADE = "S" THEN SAL * 0.2
            WHEN GRADE = "A" THEN SAL * 0.15
            WHEN GRADE = "B" THEN SAL * 0.1
            WHEN GRADE = "C" THEN 0
        END BONUS
FROM HR_EMPLOYEES A
JOIN GRADES B
ON A.EMP_NO = B.EMP_NO
GROUP BY A.EMP_NO
ORDER BY EMP_NO;
