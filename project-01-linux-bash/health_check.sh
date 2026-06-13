#!/bin/bash


LOGFILE="./health_report.log"

echo "--------------" >> $LOGFILE
echo "SERVER HEALTH REPORT"  >> $LOGFILE
echo "Generated on: $(date)"  >> $LOGFILE
echo "--------------"  >> $LOGFILE

echo ""  >> $LOGFILE
echo "1.Disk usage"  >> $LOGFILE
df -h  >> $LOGFILE

echo ""  >> $LOGFILE
echo "2. RAM usage"  >> $LOGFILE
free -h  >> $LOGFILE

echo ""  >> $LOGFILE
echo "3. System Uptime"  >> $LOGFILE
uptime  >> $LOGFILE

echo ""  >> $LOGFILE
echo "4. Top 5 Memory consuming processes"  >> $LOGFILE
ps aux --sort=%mem | head -6  >> $LOGFILE

echo ""  >> $LOGFILE
