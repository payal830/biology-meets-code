# DNA Sequence Analyzer
# A beginner-friendly Biology + Coding project

def analyze_dna(sequence):
    sequence = sequence.upper().replace(" ", "")

    valid_bases = {"A", "T", "G", "C"}

    if not sequence:
        print("Please enter a DNA sequence.")
        return

    if not set(sequence).issubset(valid_bases):
        print("Invalid DNA sequence! Use only A, T, G, and C.")
        return

    length = len(sequence)

    print("\n--- DNA Sequence Analysis ---")
    print("DNA Sequence:", sequence)
    print("Sequence Length:", length)
    print("Adenine (A):", sequence.count("A"))
    print("Thymine (T):", sequence.count("T"))
    print("Guanine (G):", sequence.count("G"))
    print("Cytosine (C):", sequence.count("C"))

    gc_content = (
        (sequence.count("G") + sequence.count("C")) / length
    ) * 100

    print(f"GC Content: {gc_content:.2f}%")


dna = input("Enter a DNA sequence (A, T, G, C): ")
analyze_dna(dna)
