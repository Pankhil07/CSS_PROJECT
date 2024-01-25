import transformers
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import BertTokenizer, BertForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
finbert = BertForSequenceClassification.from_pretrained('yiyanghkust/finbert-tone',num_labels=3)
model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")