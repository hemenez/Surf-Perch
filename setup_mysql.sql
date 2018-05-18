-- Creating User and giving permissions
CREATE DATABASE IF NOT EXISTS twitter_db;
GRANT ALL PRIVILEGES ON *.*
      TO 'tweet_user'@'localhost'
      IDENTIFIED BY 'tweet_pwd';
FLUSH PRIVILEGES;
