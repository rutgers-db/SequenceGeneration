# LLM Sequence Generation

## Purpose

- Generate sequences using LLM in the Huggingface
- Tokenize the generated sequences

## Chosen Models
- GPT2_SMALL
- GPT2_MEDIUM
- GPTNEO_1_3B
- GPTNEO_2_7B

## Usage

Using gen_gpt2.py to generate sequences using gpt2
```
python3 gen_gpt2.py
```

Using gen_gptNeo.py to generate sequences using gpt2

```
python3 gen_gptNeo.py
```

Tokenize the generated sequence using encodeSeqByGpt2Tokenizer.py and the tokenized sequences will be stored in tokenizeSeq/tokenizedSequences

# Generated Sequences

We have generate some sequences by chosen models mentioned above. They are stored in generated_text/model_name/SeqLen_XXTOPK_XXXXXS and we define the format of data using two files: 
- sequences.txt 
- seqLen.txt.

The content of all generated sequences are concatenated in the sequences.txt and each of their length are written in the seqLen.txt line by line. If the file is gzip, that means its raw file is over 100MB and cannot be uploaded to the github(Use it after decompression).