def lzw_compress(data):
    # Initialisation du dictionnaire
    dictionary = {chr(i): i for i in range(256)}
    next_code = 256
    result = []

    w = ""
    for c in data:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            dictionary[wc] = next_code
            next_code += 1
            w = c

    if w:
        result.append(dictionary[w])
    return result

def lzw_decompress(codes):
    # Initialisation du dictionnaire
    dictionary = {i: chr(i) for i in range(256)}
    next_code = 256
    result = []

    w = chr(codes[0])
    result.append(w)

    for code in codes[1:]:
        if code in dictionary:
            entry = dictionary[code]
        elif code == next_code:
            entry = w + w[0]
        else:
            raise ValueError("Code invalide.")

        result.append(entry)
        dictionary[next_code] = w + entry[0]
        next_code += 1
        w = entry

    return "".join(result)

# Exemple d'exécution
if __name__ == "__main__":
    data = "décompression se fait simplement en reconstituant pas à pas le dictionnaire"
    compressed = lzw_compress(data)
    decompressed = lzw_decompress(compressed)

    print("Texte original :", data)
    print("Données compressées :", compressed)
    print("Texte décompressé :", decompressed)
