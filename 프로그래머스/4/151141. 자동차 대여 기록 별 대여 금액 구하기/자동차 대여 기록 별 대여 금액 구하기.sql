WITH DISCOUNTS AS (

    SELECT HISTORY_ID,
        CASE
            WHEN DATEDIFF(END_DATE, START_DATE) >= 89 THEN '90일 이상'
            WHEN DATEDIFF(END_DATE, START_DATE) >= 29 THEN '30일 이상'
            WHEN DATEDIFF(END_DATE, START_DATE) >= 6 THEN '7일 이상'
            ELSE NULL
        END AS DURATION_TYPE,
        C.DAILY_FEE,
        DATEDIFF(END_DATE, START_DATE) + 1 'PERIOD'
    FROM CAR_RENTAL_COMPANY_CAR C
        JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY H
        ON C.CAR_TYPE = '트럭' AND C.CAR_ID = H.CAR_ID
)

SELECT 
       
    HISTORY_ID,
    CASE
        WHEN D.DURATION_TYPE IS NULL THEN ROUND(DAILY_FEE * PERIOD)
        ELSE ROUND(DAILY_FEE * ((100 - DISCOUNT_RATE) / 100) * PERIOD)
    END AS FEE
FROM DISCOUNTS D
    LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN P
    ON P.DURATION_TYPE = D.DURATION_TYPE AND CAR_TYPE = '트럭'
 ORDER BY FEE DESC, HISTORY_ID DESC