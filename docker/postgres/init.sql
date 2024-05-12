CREATE USER postgres_user WITH PASSWORD 'Suguadsgyugyuqwgy90wqugb';

CREATE DATABASE mysite_db OWNER postgres_user;

ALTER DATABASE mysite_db CONNECTION LIMIT -1;