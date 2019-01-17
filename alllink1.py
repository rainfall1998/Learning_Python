import tensorflow as tf
import input_data
mnist = input_data.read_data_sets("MNIST/",one_hot=True)
#Paramters
learning_rate = 0.001
training_iters = 100000
batch_size = 128
display_step = 30

#Network parameters
n_input = 784
n_classes = 10
dropout = 0.8
#tf Graph input
x = tf.placeholder(tf.float32,[None,n_input])
y = tf.placeholder(tf.float32,[None,n_classes])
keep_prob = tf.placeholder(tf.float32)
#Create model

def all_link(_X,_weights,_biases,_dropout):
    _X = tf.nn.dropout(_X,_dropout)
    d1 = tf.nn.sigmoid(tf.nn.bias_add(tf.matmul(_X, _weights['wd1']),_biases['bd1']),name='d1')
    d2x = tf.nn.dropout(d1,_dropout)
    d2 = tf.nn.sigmoid(tf.nn.bias_add(tf.matmul(d2x,_weights['wd2']),_biases['bd2']),name='d2')
    dout2 = tf.nn.dropout(d2,_dropout)
    d3 = tf.nn.sigmoid(tf.nn.bias_add(tf.matmul(dout2,_weights['wd3']),_biases['bd3']),name='d3')
    dout = tf.nn.dropout(d3,_dropout)
    out = tf.matmul(dout,weights['out'])+_biases['out']
    return out
weights = {
    'wd1':tf.Variable(tf.random_normal([784,600],stddev=0.01)),
    'wd2':tf.Variable(tf.random_normal([600,480],stddev=0.01)),
    'wd3':tf.Variable(tf.random_normal([480,480],stddev=0.01)),
    'out':tf.Variable(tf.random_normal([480,10]))
}
biases = {
    'bd1':tf.Variable(tf.random_normal([600])),
    'bd2':tf.Variable(tf.random_normal([480])),
    'bd3':tf.Variable(tf.random_normal([480])),
    'out':tf.Variable(tf.random_normal([10])),
}
#Construct model
pred = all_link(x, weights, biases, keep_prob)

#Define loss and optimizer
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=pred))#the right percent
optimizer = tf.train.AdamOptimizer(learning_rate = learning_rate).minimize(cost)
#Evaluate model
correct_pred = tf.equal(tf.argmax(pred,1),tf.argmax(y,1))
accuracy = tf.reduce_mean(tf.cast(correct_pred,tf.float32))

init = tf.initialize_all_variables()
saver = tf.train.Saver()
with tf.Session() as sess:
    sess.run(init)
    step = 1
    while step * batch_size < training_iters:
        #update the data 128 per 
        batch_xs,batch_ys = mnist.train.next_batch(batch_size)
        #train
        sess.run(optimizer,feed_dict={x:batch_xs,y:batch_ys,keep_prob:dropout})
        #10 generation output once
        if step % display_step == 0:
            acc = sess.run(accuracy,feed_dict={x:batch_xs,y:batch_ys,keep_prob:1.})
            loss = sess.run(cost,feed_dict = {x:batch_xs,y:batch_ys,keep_prob:1.})
            print("Iter "+str(step*batch_size)+",Minibatch Loss = "+"{:.6f}".format(loss)+", Training Accuracy = "+"{:.5f}".format(acc))
            saver.save(sess,'./model/'+'my_model',global_step=step)
        step += 1
    print("Optimization Finished!")
    print ("Testing Accuracy:", sess.run(accuracy, feed_dict={x: mnist.test.images[:256], y: mnist.test.labels[:256], keep_prob: 1.}))
    