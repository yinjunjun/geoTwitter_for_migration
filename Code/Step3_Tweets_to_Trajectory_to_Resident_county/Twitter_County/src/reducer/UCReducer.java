/**
 * UCReducer.java
 * @author Junjun Yin
 */


package reducer;

import java.util.HashMap;
import java.util.Map;
import java.util.Iterator;
import java.io.IOException;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.mapred.MapReduceBase;
import org.apache.hadoop.mapred.OutputCollector;
import org.apache.hadoop.mapred.Reducer;
import org.apache.hadoop.mapred.Reporter;

public class UCReducer extends MapReduceBase implements Reducer<LongWritable, LongWritable, LongWritable, Text> {

	@Override
	public void reduce(LongWritable key, Iterator<LongWritable> values, OutputCollector<LongWritable, Text> output, Reporter reporter) throws IOException {
		
		HashMap<Long, Integer> tweetCount = new HashMap<Long, Integer>();

		int totalTweet = 0;

		while(values.hasNext()) {
			long countyID = values.next().get();
			totalTweet ++;

			if(tweetCount.containsKey(countyID)) {
				tweetCount.put(countyID, tweetCount.get(countyID) + 1);
			}
			else {
				tweetCount.put(countyID, 1);
			}
		}

		long mainCounty = -1;
		int maxCount = 0;

		for(long l: tweetCount.keySet()) {
			int cCount = tweetCount.get(l);
			if(cCount > maxCount) {
				mainCounty = l;
				maxCount = cCount;
			}
		}

		output.collect(key, new Text(totalTweet + "," + mainCounty + "," + maxCount));

	}	
}
