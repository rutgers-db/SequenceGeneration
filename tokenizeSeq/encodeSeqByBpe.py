import sentencepiece as spm

# read the sequences saved in the file
# and the seq length information should be save in seqLen file

sequenceFile = "../arwen-gpt2-medium-topk50/sequences.txt"
seqLenFile = "../arwen-gpt2-medium-topk50/seqLen.txt"
encodedFile = "gpt2-medium-topk50-seq.bin"
sp = spm.SentencePieceProcessor(model_file='../../../SIGMOD23-LMND-code/encoding/bpe_model/openwebtext_64K.model')

seqF = open(sequenceFile,'r')
lenF = open(seqLenFile,'r')
encodedSeqF = open(encodedFile,'wb')

lines = lenF.readlines()
for line in lines:
    tmp_len = int(line)
    str = seqF.read(tmp_len)
    
    tokens = sp.encode(str)

    tokens_len =int(len(tokens))

    encodedSeqF.write(tokens_len.to_bytes(4,byteorder='little',signed=True))
    for i in range(0,tokens_len):
        encodedSeqF.write((tokens[i]).to_bytes(4,byteorder='little',signed=True))

print("sequence number : %d " % (len(lines)))

seqF.close()
lenF.close()
encodedSeqF.close()
