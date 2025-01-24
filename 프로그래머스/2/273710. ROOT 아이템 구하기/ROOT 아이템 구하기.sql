SELECT TREE.ITEM_ID, INFO.ITEM_NAME
FROM ITEM_TREE TREE
    JOIN ITEM_INFO INFO
    ON TREE.ITEM_ID = INFO.ITEM_ID 
WHERE TREE.PARENT_ITEM_ID IS NULL
ORDER BY 1;