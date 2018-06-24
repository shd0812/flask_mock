-- 新建数据库
create database mock_db;

CREATE TABLE mock_user (
 `id`  int(10)  NOT NULL auto_increment,
 `name` VARCHAR(20) DEFAULT null,
 `mobile` VARCHAR(11) DEFAULT NULL,
 `province` VARCHAR(10) DEFAULT '北京',
 `create_time` datetime DEFAULT CURRENT_TIMESTAMP,
 PRIMARY KEY (`id`)
) ENGINE = INNODB ;