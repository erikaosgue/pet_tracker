-- prepares a MySQL server for the project

CREATE DATABASE pet_db;
create user cobra_team with password 'cobra';
grant ALL privileges on database pet_db to cobra_team;
