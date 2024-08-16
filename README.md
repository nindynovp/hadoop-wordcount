# Hadoop Word Count MapReduce
This repository contains scripts for a basic Hadoop Streaming Word Count job using Python for the mapper and reducer.
## Files
- : The Python script used as the mapper.
- : The Python script used as the reducer.
- : Input text file containing the preamble of the Indonesian Constitution.
- : Output file containing the word counts.
## How to Run
1. Ensure Hadoop is installed and configured.
2. Place the scripts and the input file in the appropriate directories.
3. Run the following command:
```bash
hadoop jar /path/to/hadoop-streaming.jar \\
    -input pembukaan_uud1945.txt \\
    -output output \\
    -mapper ./mapper.py \\
    -reducer ./reducer.py
```
4. The results will be available in the `output` directory.
## Example Output
```
Bahwa   1
Kemerdekaan     3
dan     5
```
