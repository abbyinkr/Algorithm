WITH main AS (
    SELECT
        d.ID,
        d.EMAIL,
        group_concat(s.NAME) AS NAME,
        group_concat(s.CATEGORY) AS CATEGORY
    FROM DEVELOPERS d
    JOIN SKILLCODES s ON d.SKILL_CODE & s.CODE = s.CODE
    GROUP BY d.ID, d.EMAIL
)
SELECT *
FROM (
    SELECT
        CASE
            WHEN NAME LIKE '%Python%' AND CATEGORY LIKE '%Front End%' THEN 'A'
            WHEN NAME LIKE '%C#%' THEN 'B'
            WHEN CATEGORY LIKE '%Front End%' THEN 'C'
        END AS GRADE,
        ID,
        EMAIL
    FROM main
) A
WHERE GRADE IS NOT NULL
ORDER BY GRADE, ID;
