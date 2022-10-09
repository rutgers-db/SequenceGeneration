from transformers import pipeline
from torch.utils.data import Dataset
import torch
import time

sequenceFile = "sequences.txt"
seqLenFile = "seqLen.txt"
genTimes = 1      # iterations number (generating 128 sequence per iteration)
prompts_num = 64
max_length = 128    # the length of one sequence generated

# seqF = open(sequenceFile,'ab')
# lenF = open(seqLenFile,'a')

# class EmptyStringsDataset(Dataset):
#     def __len__(self):
#         return 64
#     def __getitem__(self,i):
#         return ' '

# dataset = EmptyStringsDataset()

print(torch.cuda.is_available())
print(torch.__version__)
print(torch.cuda.device_count())
print(torch.cuda.current_device())

print("Loading pipeline")
generator = pipeline('text-generation',  model='EleutherAI/gpt-neo-125M', device_map="auto")
generator.tokenizer.pad_token_id = generator.model.config.eos_token_id
print("Start Inference")
#time on
time_start=time.time()

# prepare empty prompt
input_list =[]
for i in range(0,prompts_num):
    input_list.append("")

# Generate the sequence and write them into file
output = generator(input_list, do_sample=True, min_length=max_length,max_length=max_length)

seqLenList =[]
total_len = 0
merged_sequenced=""
for j in range(0,prompts_num):
    tmp_seq = str(output[j][0]['generated_text']).encode().decode()
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
print('Sequence generated amount: %d' %  (prompts_num))

print("total sequence length sum: %d" % (total_len))
# seqF.close()
# lenF.close()
# generator.save_pretrained('./generator')
