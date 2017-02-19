import tensorflow as tf

filename_queue=tf.train.string_input_producer(["/home/surya/Desktop/exp_recog/tmp/expre_data/fer2013/fer2013.csv"])
reader = tf.TextLineReader(skip_header_lines=1)
key,values = reader.read(filename_queue)
record_defaults = [[],[],[]]
col1,col2,col3 = tf.decode_csv(values,record_defaults=record_defaults)

sess=tf.InteractiveSession()
coord = tf.train.Coordinator()
threads = tf.train.start_queue_runners(coord=coord)
label,exmp=sess.run([col1,col2])
print label,exmp
label1,exmp1=sess.run([col1,col2])
print label1,exmp1
coord.request_stop()
coord.join(threads)










