100 Most Popular Words
Overview
Multiple factors affect the performance of an application. The assignment aims to analyze such factors -- input size (or load), algorithm efficiency, data structures, system resource utilization (e.g., CPU, Memory), and others. The assignment will allow you to understand the impact of the above factors on performance. And we'll learn how the size of the input dataset impacts performance and what techniques we should use to alleviate the problems introduced by increased input dataset size (the crux of Big Data).

Dataset
The dataset is a zip file that consists of three files with only English words.

data_16GB.txt – A text file of size 16GB.
Another file contains the stop words (https://gist.github.com/sebleier/554280), which are skipped.

Programming Language:
Python

Usage
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.5.jar \
- file /home/hduser/mapper.py -mapper mapper.py \
- file /home/hduser/reducer.py -reducer reducer.py \
- input /user/dir/data_16GB.txt \
- output /user/hduser/output