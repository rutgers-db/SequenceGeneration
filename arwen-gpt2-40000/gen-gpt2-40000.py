from transformers import GPT2LMHeadModel, GPT2Tokenizer
import time

sequenceFile = "sequences.txt"
seqLenFile = "seqLen.txt"
tmpFile ="template.txt"

genTimes = 391
returnSeqNum = 256 
tokenizer = GPT2Tokenizer.from_pretrained("../../arwen-gpt2-medium-x21")
model = GPT2LMHeadModel.from_pretrained("../../arwen-gpt2-medium-x21",device_map="auto", load_in_8bit=True)

#time on
time_start=time.time()
seqLenList =[]
total_len = 0
merged_sequenced=""

for i in range(0,genTimes):
    sample_output = model.generate(None, num_return_sequences=returnSeqNum, do_sample=True, min_length = 128, max_length=128)

    for j in range(0,returnSeqNum):
        tmp_seq = tokenizer.decode(sample_output[j], skip_special_tokens=True)
        with open(tmpFile, "w") as wFile:
            wFile.write(tmp_seq)
        with open(tmpFile, "r") as rFile:
            tmp_seq = rFile.read()
        total_len += len(tmp_seq)
        tmp_len = str(len(tmp_seq)) +'\n'
        merged_sequenced = merged_sequenced+tmp_seq
        seqLenList.append(tmp_len)
    

n = 0
with open(sequenceFile, "a") as file:
    n = file.write(merged_sequenced) 

with open(seqLenFile,"a") as lenFile:
    lenFile.writelines(seqLenList)

assert(n == total_len)

#time off
time_end=time.time()
print('total generation time cost',time_end-time_start,'s')
print('Sequence generated amount: %d' %  (returnSeqNum))
print("total sequence length sum: %d" % (total_len))