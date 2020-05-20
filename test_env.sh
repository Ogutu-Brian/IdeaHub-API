#!/bin/bash
FILE_NAME=".env2"
echo 'Setting up test environment variables'
touch $FILE_NAME
chmod 777 $FILE_NAME
echo DATABASE_NAME=\'ideahub\' >> $FILE_NAME
echo USER_NAME=\'ideahub\' >> $FILE_NAME
echo DATABASE_PASSWORD=\'ideahub\' >> $FILE_NAME
echo DATABASE_HOST=\'localhost\' >> $FILE_NAME
echo DATABASE_PORT=5432 >> $FILE_NAME
echo SECRET_KEY=\'example secret key\' >> $FILE_NAME
echo DEBUG=True >> $FILE_NAME
