run_mapreduce()
{
  hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mrl-cdh4.1.1.jar -mapper $1 -reducer $2 -file $1 -file $2 -input $3 -output $4
}

alias hs=run_mapreduce


##Run code by using the below
############################################
hs mappy.py reducer.py myinput output2###
############################################


#find out what's on hadoop cluster
############################################
hadoop fs -ls
hadoop fs -tail
############################################
---It mirrors standard UNIX command--------


#Upload data to Hadoop, rename and delete
############################################
hadoop fs -put purchase.txt
hadoop fs -mv purchase.txt newname.txt
hadoop fs -rm purchase.txt
hadoop fs -mkdir myinput
############################################

#Get data from Hadoop cluster
############################################
hadoop fs -get purchase.txt
############################################
