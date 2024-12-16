import heapq
from collections import defaultdict

# Étape 1 : Analyse des fréquences
def calculate_frequency(data):
    frequency = defaultdict(int)
    for char in data:
        frequency[char] += 1
    return frequency

# Étape 2 : Création des nœuds
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Pour la comparaison dans le tas
    def __lt__(self, other):
        return self.freq < other.freq

# Étape 3 : Construction de l'arbre de Huffman
def build_huffman_tree(frequency):
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]  # La racine de l'arbre

# Étape 4 : Génération des codes de Huffman
def generate_codes(root, current_code="", codes=None):
    if codes is None:
        codes = {}

    if root is not None:
        if root.char is not None:  # Feuille
            codes[root.char] = current_code
        generate_codes(root.left, current_code + "0", codes)
        generate_codes(root.right, current_code + "1", codes)

    return codes

# Compression
def huffman_encode(data, codes):
    return "".join(codes[char] for char in data)

# Décompression
def huffman_decode(encoded_data, root):
    decoded_output = []
    current = root
    for bit in encoded_data:
        current = current.left if bit == "0" else current.right
        if current.char is not None:
            decoded_output.append(current.char)
            current = root
    return "".join(decoded_output)

# Exemple d'exécution
if __name__ == "__main__":
    data = "BIBBIIIBIBBIIIBIII"
    frequency = calculate_frequency(data)
    root = build_huffman_tree(frequency)
    codes = generate_codes(root)
    encoded = huffman_encode(data, codes)
    decoded = huffman_decode(encoded, root)

    print("Texte original:", data)
    print("Fréquences des caractères:", frequency)
    print("Codes de Huffman:", codes)
    print("Texte encodé:", encoded)
    print("Texte décodé:", decoded)
