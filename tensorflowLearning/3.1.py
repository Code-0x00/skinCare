import tensorflow as tf 

a=tf.constant([1.0,2.0],name="a")
b=tf.constant([2.0,3.0],name="b")

result=a+b

print(a.graph is tf.get_default_graph())
print result

weights=tf.Variable(tf.random_normal([2,3],mean=0,stddev=2))

init_op=tf.global_variables_initializer()


sess=tf.Session()
sess.run(init_op)
print(sess.run(result))


v=tf.constant([[1,2,3],[4,5,6]],dtype=tf.float32)
print(sess.run(tf.reduce_mean(v)))


sess.close()