import sys
sys.path.append("../scripts")
from kafka_utils import KafkaUtils
import pandas as pd
df = pd.read_csv("../data/amharic_news_dataset.csv")
producer = KafkaUtils.create_producer()