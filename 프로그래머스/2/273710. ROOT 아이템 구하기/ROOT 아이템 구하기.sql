SELECT DISTINCT(PARENT.ITEM_ID), INFO.ITEM_NAME
FROM ITEM_TREE PARENT
    JOIN ITEM_TREE CHILD
    ON PARENT.ITEM_ID = CHILD.PARENT_ITEM_ID
    JOIN ITEM_INFO INFO
    ON PARENT.ITEM_ID = INFO.ITEM_ID 
WHERE PARENT.PARENT_ITEM_ID IS NULL

