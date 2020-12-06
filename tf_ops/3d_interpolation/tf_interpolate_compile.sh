# TF1.2
#g++ -std=c++11 tf_interpolate.cpp -o tf_interpolate_so.so -shared -fPIC -I /usr/local/lib/python2.7/dist-packages/tensorflow/include -I /usr/local/cuda-8.0/include -lcudart -L /usr/local/cuda-8.0/lib64/ -O2 -D_GLIBCXX_USE_CXX11_ABI=0

# TF1.4
#g++ -std=c++11 tf_interpolate.cpp -o tf_interpolate_so.so -shared -fPIC -I /usr/local/lib/python2.7/dist-packages/tensorflow/include -I /usr/local/cuda-8.0/include -I /usr/local/lib/python2.7/dist-packages/tensorflow/include/external/nsync/public -lcudart -L /usr/local/cuda-8.0/lib64/ -L/usr/local/lib/python2.7/dist-packages/tensorflow -ltensorflow_framework -O2 -D_GLIBCXX_USE_CXX11_ABI=0

# TF2.2
g++-8 -std=c++11 tf_interpolate.cpp -o tf_interpolate_so.so -shared -fPIC -I /home/g800g1/anaconda3/envs/tf-gpu/lib/python3.8/site-packages/tensorflow/include -I /usr/local/cuda-10.1/include -I /home/g800g1/anaconda3/envs/tf-gpu/lib/python3.8/site-packages/tensorflow/include/external/nsync/public -lcudart -L /usr/local/cuda-10.1/lib64 -L /home/g800g1/anaconda3/envs/tf-gpu/lib/python3.8/site-packages/tensorflow -ltensorflow_framework -O2 #-D_GLIBCXX_USE_CXX11_ABI=0
