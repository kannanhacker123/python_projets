# Use fixed-width (2-digit) mappings for consistency
s_dictionary = {
    'a': "01", 'b': "02", 'c': "03", 'd': "04", 'e': "05",
    'f': "06", 'g': "07", 'h': "08", 'i': "09", 'j': "10",
    'k': "11", 'l': "12", 'm': "13", 'n': "14", 'o': "15",
    'p': "16", 'q': "17", 'r': "18", 's': "19", 't': "20",
    'u': "21", 'v': "22", 'w': "23", 'x': "24", 'y': "25",
    'z': "26"
}

u_dictionary = {
    "A": "27", "B": "28", "C": "29", "D": "30", "E": "31",
    "F": "32", "G": "33", "H": "34", "I": "35", "J": "36",
    "K": "37", "L": "38", "M": "39", "N": "40", "O": "41",
    "P": "42", "Q": "43", "R": "44", "S": "45", "T": "46",
    "U": "47", "V": "48", "W": "49", "X": "50", "Y": "51",
    "Z": "52"
}

n_dictionary = {
    "0": "53", "1": "54", "2": "55", "3": "56", "4": "57",
    "5": "58", "6": "59", "7": "60", "8": "61", "9": "62"
}

sym_dictionary = {
    "!": "63", "@": "64", "#": "65", "$": "66", "%": "67",
    "^": "68", "&": "69", "*": "70", "(": "71", ")": "72",
    "-": "73", "_": "74", "+": "75", "=": "76", "{": "77",
    "}": "78", "[": "79", "]": "80", ":": "81", ";": "82",
    "'": "83", '"': "84", "<": "85", ">": "86", ",": "87",
    ".": "88", "?": "89", "/": "90", "\\": "91", "|": "92",
    "`": "93", "~": "94", " ": "95"
}


def convert_string(test_str):
    encoded_str = ""
    for char in test_str:
        if char in s_dictionary:
            encoded_str += s_dictionary[char]
        elif char in u_dictionary:
            encoded_str += u_dictionary[char]
        elif char in n_dictionary:
            encoded_str += n_dictionary[char]
        elif char in sym_dictionary:
            encoded_str += sym_dictionary[char]
        else:
            # Handle unexpected characters
            encoded_str += "00"
    return encoded_str

def encode_helper(count, segment):
    return str(count) + "x" + segment +"."

def encode_string(converted_str):
    encoded_str = ""
    # Process the converted string in fixed-length (2-digit) segments
    i = 0
    while i < len(converted_str):
        count = 1
        # Check for consecutive identical segments
        while i + 2 < len(converted_str) and converted_str[i:i+2] == converted_str[i+2:i+4]:
            count += 1
            i += 2
        # Append the encoded representation of this segment
        encoded_str += encode_helper(count, converted_str[i:i+2])
        i += 2
    return encoded_str

# Test the conversion and encoding functions
test_str = input("Enter a string: ")
# Debug prints
converted = convert_string(test_str)    
print("password before converting: ", test_str)
print("its length is ", len(test_str), "\n")

print("password after converting: ", converted)
print("its length is ", len(converted))
print("it increase by ", len(converted) - len(test_str))
print("its increase percentage is ", ((len(converted) - len(test_str)) / len(test_str)) * 100, "%\n")

print("password after encoding: ", encode_string(converted))
print("its length is ", len(encode_string(converted)))
print("it increase by ", len(encode_string(converted)) - len(converted))
print("its increase percentage is ", ((len(encode_string(converted)) - len(converted)) / len(converted)) * 100, "%\n")

print()
print("net increase in length: ", len(encode_string(converted)) - len(test_str))
print("net increase percentage: ", ((len(encode_string(converted)) - len(test_str)) / len(test_str)) * 100, "%")