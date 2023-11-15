-- convert to utf-8
USE hbtn_0c_0;
ALTER TABLE first_table MODIFY name VARCHAR(191) CHARACTER SET utf8mb4 collate utf8mb4_unicode_ci;
