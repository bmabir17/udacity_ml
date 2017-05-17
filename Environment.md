Download Anaconda from here:-
https://www.continuum.io/downloads#linux 
In download folder of anaconda file
~$ bash Anaconda2-4.3.0-Linux-x86_64.sh
~$ export PATH=~/anaconda2/bin:$PATH
~$ conda create --name eyeCon scikit-learn theano tensorflow jupyter matplotlib pandas keras opencv

~$ activate eyeCon
~$ jupyter notebook

export all_proxy="https://<proxy>:<port>/"

To install OpenCv
~$ conda config --add channels menpo
~$ conda install opencv #opencv3

To install Tensorflow with GPU(with Linux16.04, Anaconda) (Link for problem)
Download the CUDA toolkit from https://developer.nvidia.com/cuda-toolkit
~$sudo dpkg -i cuda*.deb
~$sudo apt-get update
~$sudo apt-get install cuda

Download cuDNN 4 from
https://developer.nvidia.com/rdp/cudnn-download
Extract. Rename the cuda directory as cudnn. We'll keep cudnn separate from cuda.
$ mv cuda cudnn
$ sudo cp -r cudnn /usr/local

Create symlinks in /usr/local/cuda/lib64 to /usr/local/cudnn/lib64
$ sudo ln -s /usr/local/cuda/lib64/libcudnn.so /usr/local/cudnn/lib64/libcudnn.so
$ sudo ln -s /usr/local/cuda/lib64/libcudnn.so.4 /usr/local/cudnn/lib64/libcudnn.so.4
$ sudo ln -s /usr/local/cuda/lib64/libcudnn.so.4.0.7 /usr/local/cudnn/lib64/libcudnn.so.4.0.7
$ sudo ln -s /usr/local/cuda/lib64/libcudnn_static.a /usr/local/cudnn/lib64/libcudnn_static.a

Set up ~/.bashrc
$ sudo nano ~/.bashrc
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/lib64:/usr/local/cudnn/lib64
export CUDA_HOME=/usr/local/cuda
export PATH=/usr/local/cuda/bin:$PATH

Using Tensorboard:
$ tensorboard --port=7000 --logdir=Hidden_1layer_log/
