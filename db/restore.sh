#!/usr/bin/env sh

DB_NAME=starter

dropdb $DB_NAME -U $DB_NAME --if-exists
createdb -O $DB_NAME -U $DB_NAME $DB_NAME
psql -U $DB_NAME -d $DB_NAME -f $DB_NAME.sql --no-psqlrc --pset pager=off --set ON_ERROR_STOP=1 --single-transaction > /dev/null

