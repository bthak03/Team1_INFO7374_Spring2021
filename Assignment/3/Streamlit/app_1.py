import streamlit as st 
import numpy as np
import pandas as pd
from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
import boto3
from botocore.exceptions import NoCredentialsError
from PIL import Image
from io import BytesIO

# Defining All the connections
es_conn = {'host': '', 'region' : 'us-east-1'}
# ElasticSearch
def connect_elasticsearch():
    es = None
    es = Elasticsearch([{'host': es_conn['host'], 'port': 9200}])
    if es.ping():
        print('Yupiee  Connected ')
    else:
        print('Awww it could not connect!')
    return es
es = connect_elasticsearch()

# S3 Connections
s3 = boto3.client('s3', aws_access_key_id = '', aws_secret_access_key= '')

bucket_1 = 'localimagesadm'

# Streamlit layout
image = Image.open('sidebarimage.png')
st.sidebar.image(image)

st.title('Image Similarity App')

my_expander = st.beta_expander('About App', expanded= False)

with my_expander:
    text = open('files/aboutapp.txt', 'r')
    st.write(text.read())

#484, 788,1413,613
# Loading image data 
names = pd.read_csv('data.csv')
rnImage  = st.selectbox('Choose Image', names.name, index = 613)
# rnImage = np.array(names.sample().name)[0].split('.')[0]

#  Image fetch funciton
def fetchImage(k,img_name = None, query = None):
    if k ==1:
        img = s3.get_object(Bucket = bucket_1, Key= '%s'%(img_name))['Body'].read()
        img = Image.open(BytesIO(img))
    else:
        img = [(query[i]['_source']['_soucre']['similar_pi']) + '.jpeg' for i in range(len(query))][0:k]
        img = [s3.get_object(Bucket = bucket_1, Key= '%s'%i)['Body'].read() for i in img]
        img = [Image.open(BytesIO(img)) for img in img]
    return img

# Orginal Image 
st.image(fetchImage(1, img_name=rnImage))
# 

##
query = es.search(index = 'image', doc_type= 'doc', body = {'query':{'match':{"master_pi":'%s'%rnImage}}})['hits']['hits']
# To query through elasticsearch
k = st.slider('Select the k values', 2,10)

st.image(fetchImage(k = k, query=query), width  = 150)


