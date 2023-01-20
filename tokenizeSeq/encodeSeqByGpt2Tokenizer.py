from transformers import GPT2TokenizerFast
tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")

print("Gpt2 Tokenizer Vocab Size:"+ str(tokenizer.vocab_size))
print(tokenizer.is_fast)
# read the sequences saved in the file
# and the seq length information should be save in seqLen file

sequenceFile = "../text_generated/gpt-neo/540L_50TOPK_2.7B/sequences.txt"
seqLenFile = "../text_generated/gpt-neo/540L_50TOPK_2.7B/seqLen.txt"
encodedFile = "gpt-neo-540L_50TOPK_2_7B.bin"

seqF = open(sequenceFile,'r')
lenF = open(seqLenFile,'r')
encodedSeqF = open(encodedFile,'wb')

lines = lenF.readlines()
for line in lines:
    tmp_len = int(line)
    str = seqF.read(tmp_len)
    
    tokens = tokenizer.encode(str)

    tokens_len =int(len(tokens))

    encodedSeqF.write(tokens_len.to_bytes(4,byteorder='little',signed=True))
    for i in range(0,tokens_len):
        encodedSeqF.write((tokens[i]).to_bytes(4,byteorder='little',signed=True))

print("sequence number : %d " % (len(lines)))

seqF.close()
lenF.close()
encodedSeqF.close()
