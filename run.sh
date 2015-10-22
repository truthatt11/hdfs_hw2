hadoop jar /home/hadoopuser/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.1.jar -mapper "python $PWD/mapper.py" -reducer "python $PWD/reducer.py" -input "/hw2/access_log" -output "/log_outdir"
