
# DNA Analyzer System Project


## Description
DNA sequences are composed of four types of nucleotides;
The nucleotides are marked A (Adenine), G (Guanine), C (Cytosine) and T (Thymine).
A full DNA molecule usually consists of two strands, connected to each other in
base-pair connections: As with Ts, and Cs with Gs
The DNA Analyzer System load, analyze, manipulate and save DNA sequences.

## The system design
factory and command design pattern together(Factory.py),
singleton design pattern(Data.py)

## Usage
```bash
python CLI.py
```
Sequence Creation Commands:
   * new <sequence> [@<sequence_name>]
    ```bash
     new ATACTGCCTGAATAC @short_seq
    ```
   * load <file_name> [@<sequence_name>
    ```bash
    load my_dna_seq.rawdna
    ```
   * dup <seq> [@<new_seq_name>]
    ```bash
    dup #22
    ```


Sequence Manipulation Commands:
   * slice <seq> <from_ind> <to_ind> [: [@<new_seq_name>|@@]]
    ```bash
    slice #1 4 9
    ```
   * replace <seq> <index> <new_letter> [: [@<new_seq_name>|@@]]
    ```bash
    replace @short_seq_s1 0 A 3 A : @repl_seq
    ```

Sequence Management Commands:
   * rename <seq> @<new_name>
   * del <seq>
   * reenum
   * save <seq> [filename]

Batch Commands:
Batch mode allows the user to define a series of actions that will take place one after
another.

   * batch <batch_name>
   * run <batchname>
   * batchlist
   * batchshow <batch_name>
   * batchsave <batch_name> [filename]
   * batchload <file_name> @<batch_name>


