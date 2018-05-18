-- Creating User and giving permissions
CREATE DATABASE IF NOT EXISTS twitter_db;
GRANT USAGE ON *.*
      TO 'twitter_user'@'localhost'
      IDENTIFIED BY 'tweet_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.*
      TO 'twitter_user'@'localhost'
      IDENTIFIED BY 'tweet_pwd';
GRANT SELECT ON performance_schema.*
      TO 'twitter_user'@'localhost'
      IDENTIFIED BY 'tweet_pwd';
FLUSH PRIVILEGES;
