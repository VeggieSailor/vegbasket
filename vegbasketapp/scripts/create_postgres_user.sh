createuser -s vegbasket 
createuser -s veggiesailor
psql -c 'create database vegbasket;' -U postgres
cat scripts/alter_user.sql |psql

