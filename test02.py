import tensorflow as tf
import os
os.environ["CUDA_VISIBLE_DEVICES"] = '-1'#禁用GPU
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

tf.compat.v1.disable_eager_execution()
cube_matrix = tf.constant([[[1],[2],[3]],[[4],[5],[6]]])
sess= tf.compat.v1.Session()
print(sess.run(cube_matrix)[0,0,0])
sess.close()
# scalar = tf.constant(100)#标量
# vector = tf.constant([1,2,3,4,5])#一阶矩阵。shape里面是元素个数
# matrix = tf.constant([[1,2,3],[4,5,6]])#二阶矩阵。【2个一阶矩阵，一阶矩阵中有3个元素】
# cube_matrix = tf.constant([[[1],[2],[3]],[[4],[5],[6]]])#【2个二阶矩阵】，每个二阶矩阵有三个一阶矩阵，每个一阶矩阵有一个元素
#
# print(cube_matrix.numpy()[0,0,0])
#
# print(scalar.get_shape())
# print(vector.get_shape())
# print(matrix.get_shape())
# print(cube_matrix.get_shape())