from typing import Iterable, Dict

def parseFASTA(dna_strings_fasta_format: Iterable[str]) -> Dict[str, str]:
    result: Dict[str, str] = {}
    cur_key = None
    cur_lines: list[str] = []

    for raw in dna_strings_fasta_format:
        line = raw.rstrip('\r\n') # normalize line endings
        if line.startswith('>'):
            if cur_key is not None:
                result[cur_key] = ''.join(cur_lines).replace(' ', '').strip()
            cur_key = line[1:].strip()
            cur_lines = []
        else:
            cur_lines.append(line)
    if cur_key is not None:
        result[cur_key] = ''.join(cur_lines).replace(' ', '').strip()
    return result

def calculateGCpercentage(dna: str) -> float:
    percentage = 0
    
    cytosineCount = dna.count('C')
    guanineCount = dna.count('G')
    cgCount = cytosineCount + guanineCount
    
    percentage = round((cgCount / len(dna)) * 100, 6)
    
    return percentage

with open('computing_gc_content.fasta', encoding='utf-8') as f:
    dna_strings = parseFASTA(f)

gc_contents = {}
for dnaID, dna in dna_strings.items():
    gc_contents[dnaID] = format(calculateGCpercentage(dna), ".6f")


print(max(gc_contents, key=gc_contents.get))
print(max(gc_contents.values()))