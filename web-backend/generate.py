
import torch

from transformers import BertLMHeadModel, BertTokenizer, GPT2LMHeadModel, GPT2Tokenizer,StoppingCriteria, StoppingCriteriaList
import re
import jieba.posseg as pseg

# Load the BERT tokenizer and model
# model_name = r"C:\Users\ziyix\Desktop\poetry-generator\backend\models\fine_tuned_model_4"
# model = GPT2LMHeadModel.from_pretrained(model_name, ignore_mismatched_sizes=True)
# tokenizer = GPT2Tokenizer.from_pretrained(model_name)

class SentenceCompletionCriteria(StoppingCriteria):
    def __init__(self, tokenizer, start_length):
        self.tokenizer = tokenizer
        self.start_length = start_length

    def __call__(self, input_ids, scores, **kwargs):
        generated_ids = input_ids[0][self.start_length:]
        generated_text = self.tokenizer.decode(generated_ids, skip_special_tokens=True)
        if generated_text.endswith(('。', '！', '？')):
            return True
        return False
    
class PoemGenerator:
    def __init__(self):
        self.model = GPT2LMHeadModel.from_pretrained(r"/mnt/c/Users/ziyix/Desktop/poetry-generator/web-backend/models/fine_tuned_model_5")
        self.tokenizer = BertTokenizer.from_pretrained(r"/mnt/c/Users/ziyix/Desktop/poetry-generator/web-backend/models/fine_tuned_model_5")
        self.model.resize_token_embeddings(len(self.tokenizer))



    # 生成诗歌函数
    def generate_poem(self,keywords,max_length):
        input_ids = self.tokenizer.encode(keywords, return_tensors='pt')

        stopping_criteria = StoppingCriteriaList([SentenceCompletionCriteria(self.tokenizer, input_ids.shape[-1])])
        
        # 创建 attention mask
        attention_mask = torch.ones(input_ids.shape, dtype=torch.long)

        # 生成文本
        output = self.model.generate(
            input_ids,
            attention_mask=attention_mask,  # 添加 attention_mask
            num_return_sequences=1,
            no_repeat_ngram_size=2,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            temperature=1.0,
            eos_token_id=self.tokenizer.eos_token_id,
            pad_token_id=self.tokenizer.pad_token_id,
            stopping_criteria=stopping_criteria,
            min_length=100,
            max_length=max_length
        )

        # 解码并生成诗句
        generated_text = self.tokenizer.decode(output[0], skip_special_tokens=True)
        poem = generated_text[len(keywords):].strip()
        #在每一个逗号和句号后面加上换行符
        poem = re.sub(r'[,，。,)]', ',\n', poem)
        pattern = r'[^\u4e00-\u9fff\u3400-\u4dbf' \
            r'\u20000-\u2a6df\u2a700-\u2b73f' \
            r'\u2b740-\u2b81f\u2b820-\u2ceaf' \
            r'\u2ceb0-\u2ebe0\u3000-\u303f' \
            r'a-zA-Z0-9，。！？、：；“”‘’（）《》【】—…·\-\"\'' \
            r'\n]'  # Include \n to preserve line breaks

    # Apply the regex substitution to remove unwanted characters while preserving line breaks
        greedy_poem = re.sub(pattern, '', poem)
        word = pseg.cut(greedy_poem)

        sentence = []
        output_sentences = []
        pause_words = ['x', 'uj', 'ul', 'p', 'c', 'd']

        for word, flag in word:
            sentence.append(word)
            if flag in pause_words and len(sentence) > 20:
                output_sentences.append(''.join(sentence))
                sentence = []

        if sentence:
            output_sentences.append(''.join(sentence))

        greedy_poem = '\n'.join(output_sentences)
        return greedy_poem
        


    

