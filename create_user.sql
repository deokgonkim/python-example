CREATE TABLE user (
    uid NUMBER,
    login VARCHAR(32),
    fullname VARCHAR(128)
);

INSERT INTO user VALUES(1000, 'user', 'Normal User');
INSERT INTO user VALUES(65534, 'nobody', 'Nobody');