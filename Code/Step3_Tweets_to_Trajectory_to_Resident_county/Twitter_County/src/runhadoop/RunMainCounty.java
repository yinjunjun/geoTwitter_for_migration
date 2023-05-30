/**
 * RunMainCounty.java
 * @author Junjun Yin
 */

package runhadoop;

import mapper.UCMapper;
import reducer.UCReducer;

import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.mapred.FileInputFormat;
import org.apache.hadoop.mapred.lib.MultipleInputs;
import org.apache.hadoop.mapred.FileOutputFormat;
import org.apache.hadoop.mapred.JobClient;
import org.apache.hadoop.mapred.JobConf;
import org.apache.hadoop.mapred.KeyValueTextInputFormat;
import org.apache.hadoop.mapred.TextInputFormat;
import org.apache.hadoop.mapred.TextOutputFormat;

public class RunMainCounty {

	public static void main(String[] args) throws Exception{
		
		Path in = new Path(args[0]);
		Path out = new Path(args[1]);

		JobConf conf1 = new JobConf(RunMainCounty.class);
		conf1.set("mapred.textoutputformat.separator", ",");
		conf1.setJobName("UserMainCounty");
		conf1.setMapperClass(UCMapper.class);
		conf1.setReducerClass(UCReducer.class);
		conf1.setOutputKeyClass(LongWritable.class);
		conf1.setOutputValueClass(LongWritable.class);
		
		conf1.setInputFormat(TextInputFormat.class);
		FileInputFormat.setInputPaths(conf1, in);

		conf1.setOutputFormat(TextOutputFormat.class);
		FileOutputFormat.setOutputPath(conf1, out);
	
		JobClient.runJob(conf1);
	}
}
