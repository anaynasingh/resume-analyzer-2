import asyncio

try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

import streamlit as st
from transformers import BertModel, BertTokenizer
import pickle, torch
from constants import EMBEDDING_MODEL_NAME, GEMINI_API_KEY, OUTPUT_PATH

class EmbeddingModel:
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.model = BertModel.from_pretrained('bert-base-uncased')

    def get_embeddings(self, data_dict):
        output_dict = {}
        keys = list(data_dict.keys())
        values = list(data_dict.values())

        # Tokenize and get embeddings
        with torch.no_grad():
            for i, value in enumerate(values):
                inputs = self.tokenizer(value, return_tensors='pt', truncation=True, padding=True)
                outputs = self.model(**inputs)
                embeddings = outputs.last_hidden_state.mean(dim=1).squeeze().tolist()
                output_dict[keys[i]] = embeddings

        return output_dict

    @staticmethod
    def save_embeddings(embedding, file_name):
        with open(file_name, 'wb') as handle:
            pickle.dump(embedding, handle, protocol=pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def read_embeddings(file_name): 
        with open(file_name, 'rb') as handle:
            output_dict = pickle.load(handle)
        return output_dict