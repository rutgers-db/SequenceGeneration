from transformers import GPTNeoForCausalLM, GPT2Tokenizer
import time

# the name of son directory indicates the output_length, topk and training steps of the LM
root_dir = "./text_generated/gpt-neo/540L_50TOPK_1.3B/"
sequenceFile = root_dir+"sequences_2.txt"
seqLenFile = root_dir+"seqLen_2.txt"
tmpFile = root_dir+"template_2.txt"

# check if the directory exists
import os
if os.path.exists(root_dir) == False:
    raise Exception("No directory for saving the generated text.The root Dir does not exist")

genTimes = 160
returnSeqNum = 32

gpt_neo_name = "EleutherAI/gpt-neo-1.3B"

tokenizer = GPT2Tokenizer.from_pretrained(gpt_neo_name)
model = GPTNeoForCausalLM.from_pretrained(gpt_neo_name,device_map="sequential", load_in_8bit=True)

#time on
time_start=time.time()
max_length = 540    # the max length of one sequence generated
merged_sequenced=""
seqLenList =[]

# start generating text
for i in range(0,genTimes):
    sample_output = model.generate(None, num_return_sequences=returnSeqNum, do_sample=True, top_k = 50, max_length=max_length)

    for j in range(0,returnSeqNum):
        tmp_seq = tokenizer.decode(sample_output[j], skip_special_tokens=True)
        with open(tmpFile, "w") as wFile:
            wFile.write(tmp_seq)
        with open(tmpFile, "r") as rFile:
            tmp_seq = rFile.read()
        tmp_len = str(len(tmp_seq)) +'\n'
        merged_sequenced = merged_sequenced+tmp_seq
        seqLenList.append(tmp_len)
    
with open(sequenceFile, "a") as file:
    file.write(merged_sequenced) 

with open(seqLenFile,"a") as lenFile:
    lenFile.writelines(seqLenList)

#time off
time_end=time.time()
print('total generation time cost',time_end-time_start,'s')
print('Sequence generated amount: %d' %  (returnSeqNum))
