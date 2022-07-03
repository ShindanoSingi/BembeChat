-- settings.sql
CREATE DATABASE bembechat;
CREATE USER bembechatuser WITH PASSWORD 'bembechat';
GRANT ALL PRIVILEGES ON DATABASE bembechat TO bembechatuser;
