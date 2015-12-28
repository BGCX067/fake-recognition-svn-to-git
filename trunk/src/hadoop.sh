#!/bin/bash
source /home/tbso/conf/set_env.sh
source /home/tbso/conf/common_utils.sh
source /home/tbso/conf/common_tables.sh

INPUT='/group/tbso-dev/lilong.ll/hive/t_ll_fake_cellphone_auctions/'
OUTPUT='/group/tbso-dev/lilong.ll/hive/t_ll_fake_cellphone_auction_titletype/pt=20120820000000'
$HADOOP fs -rmr $OUTPUT

$HADOOP jar $STREAMINGJAR\
    -D mapred.reduce.tasks=0 \
    -D mapred.job.name="Extract_type_from_title_of_auction" \
    -D mapred.map.tasks=200 \
    -files ./map.py,./bands.in \
    -input $INPUT  \
    -output $OUTPUT \
    -mapper map.py

echo "===============\nhadoop jog has finished================\n"

#-D mapred.map.tasks=2000 \
