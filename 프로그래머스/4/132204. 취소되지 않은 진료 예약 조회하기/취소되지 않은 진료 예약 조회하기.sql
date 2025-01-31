WITH CS_APPOINTMENT AS (

    SELECT *
    FROM APPOINTMENT
    WHERE 
    APNT_CNCL_YN = 'N'
    AND MCDP_CD = 'CS'
    AND DATE_FORMAT(APNT_YMD, '%Y-%m-%d') = '2022-04-13'
)

SELECT APNT_NO, PT_NAME, A.PT_NO, A.MCDP_CD, DR_NAME, APNT_YMD
FROM CS_APPOINTMENT A 
    JOIN PATIENT P
    ON A.PT_NO = P.PT_NO
    JOIN DOCTOR D
    ON A.MDDR_ID = D.DR_ID
ORDER BY APNT_YMD