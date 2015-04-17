# install build tools 
yum install make automake gcc gcc-c++ kernel-devel git-core -y 

# install python 2.7 and change default python symlink 
yum install python27-devel -y 
rm /usr/bin/python
ln -s /usr/bin/python2.7 /usr/bin/python 

# yum still needs 2.6, so write it in and backup script 
cp /usr/bin/yum /usr/bin/_yum_before_27 
sed -i s/python/python2.6/g /usr/bin/yum 
sed -i s/python2.6/python2.6/g /usr/bin/yum 

# should display now 2.7.5 or later: 
python -V 
