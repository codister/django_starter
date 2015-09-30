#!/usr/bin/env sh

DB_NAME=starter

pg_dump -d $DB_NAME -f $DB_NAME.sql --no-owner --exclude-table-data=django_session --no-privileges

# http://www.postgresql.org/message-id/flat/E1VuYH7-0008Rz-SV@wrigleys.postgresql.org
sed -i.bak '/^COMMENT ON EXTENSION plpgsql/d' $DB_NAME.sql
rm $DB_NAME.sql.bak

 # --clean --if-exists
