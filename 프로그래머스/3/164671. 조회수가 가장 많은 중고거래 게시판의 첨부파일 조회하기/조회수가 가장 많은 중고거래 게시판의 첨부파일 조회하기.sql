WITH MOST_VIEWED AS 
    (
        SELECT *
        FROM USED_GOODS_BOARD
        ORDER BY VIEWS DESC
        LIMIT 1
    )
SELECT 
    CONCAT(
            '/home/grep/src/', 
            MOST_VIEWED.BOARD_ID, 
            '/', 
            F.FILE_ID, 
            F.FILE_NAME, 
            F.FILE_EXT
    ) FILE_PATH
FROM MOST_VIEWED
    JOIN USED_GOODS_FILE F
    ON MOST_VIEWED.BOARD_ID = F.BOARD_ID
ORDER BY FILE_ID DESC;