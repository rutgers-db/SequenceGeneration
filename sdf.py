from transformers import GPT2LMHeadModel, GPT2Tokenizer
import time


returnSeqNum = 10 
tokenizer = GPT2Tokenizer.from_pretrained("stanford-crfm/alias-gpt2-small-x21")
model = GPT2LMHeadModel.from_pretrained("stanford-crfm/alias-gpt2-small-x21",device_map="auto", load_in_8bit=True)
#time on
time_start=time.time()
seqLenList =[]
total_len = 0
merged_sequenced=""

sample_output = model.generate(None, num_return_sequences=returnSeqNum, do_sample=True, min_length = 128, max_length=128)

for j in range(0,returnSeqNum):
    tmp_seq = tokenizer.decode(sample_output[j], skip_special_tokens=False)
    print(tmp_seq)
    print("___________________")