run_mapreduce()
{
  hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mrl-cdh4.1.1.jar -mapper $1 -reducer $2 -file $1 -file $2 -input $3 -output $4
}

alias hs=run_mapreduce


##Run code by using the below
############################################
###hs mappy.py reducer.py myinput output2###
############################################


#find what on your hadoop cluster
############################################
##############hadoop fs -ls#################
############################################


#Upload data to Hadoop
############################################
########hadoop fs -put purchase.txt#########
############################################

