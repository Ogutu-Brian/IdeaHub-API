#!/bin/bash
output=.env
touch $output

echo DATABASE_NAME='ideahub' >> $output
echo USER_NAME='brian' >> $output
echo DATABASE_PASSWORD='ideaHub' >> $output
echo DATABASE_HOST='localhost' >> $output
echo DATABASE_PORT=5432 >> $output
echo SECRET_KEY='your secret key' >> $output
echo DEBUG=True >> $output
echo SENDGRID_API_KEY='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' >> $output
echo EMAIL_HOST_USER='apikey' >> $output
echo EMAIL_HOST='smtp.sendgrid.net' >> $output
echo EMAIL_PASSWORD='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' >> $output
echo EMAIL_PORT=587 >> $output
echo EMAIL_USE_TLS=True >> $output
