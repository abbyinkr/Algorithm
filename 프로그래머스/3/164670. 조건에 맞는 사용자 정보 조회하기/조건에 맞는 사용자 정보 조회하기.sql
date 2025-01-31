WITH WRITERS AS
(
    SELECT WRITER_ID
    FROM USED_GOODS_BOARD
    GROUP BY WRITER_ID
    HAVING COUNT(BOARD_ID) >= 3 
)

SELECT  USER_ID, 
        NICKNAME, 
        CONCAT(CITY, ' ', STREET_ADDRESS1, ' ' , STREET_ADDRESS2) '전체주소',
        CONCAT(
            LEFT(TLNO, 3), 
            '-',
            MID(TLNO, 4, 4),
            '-',
            RIGHT(TLNO, 4)
        ) '전화번호'
FROM WRITERS W
    LEFT JOIN USED_GOODS_USER U
    ON W.WRITER_ID = U.USER_ID
ORDER BY USER_ID DESC;