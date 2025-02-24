### Project Overview

This project is a Python-based text encoding utility that converts a string into a custom format using a mapping of characters to fixed-width numerical values. The utility applies a two-step process:
1. **Character Conversion**: Each character is mapped to a corresponding 2-digit numerical code based on predefined dictionaries for lowercase letters, uppercase letters, numbers, and symbols.
2. **Run-Length Encoding**: The converted string is then compressed using a form of run-length encoding, where consecutive identical 2-digit segments are replaced by a count and the segment itself (e.g., "3x99.").

The goal is to observe the length change before and after the conversion and encoding, and calculate the percentage increase in size at each stage.

---

### Key Features

- **Character Conversion**: Converts each character of the input string to a 2-digit number based on predefined dictionaries.
- **Run-Length Encoding (RLE)**: Reduces repetitive sequences of characters into a more compact form by using counts.
- **Size Analysis**: Displays the increase in length at each step and calculates the percentage increase after conversion and encoding.
- **Handling Special Characters**: Supports symbols, digits, uppercase, and lowercase letters with unique mappings for each.

---

### Usage

#### Install and run the script:

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Run the script:
   ```bash
   python3 encoder.py
   ```

   This will output the following information:
   - The original password (input string)
   - The string after it is converted into its respective codes
   - The string after it is run-length encoded
   - Length comparison before and after each process

---

### Code Explanation

- **Dictionaries**: The `s_dictionary`, `u_dictionary`, `n_dictionary`, and `sym_dictionary` hold mappings for lowercase letters, uppercase letters, digits, and special characters, respectively. Each character is assigned a unique 2-digit code.
  
- **`convert_string`**: This function converts an input string into a sequence of 2-digit numbers by checking each character against the dictionaries.

- **`encode_helper`**: This function is used to format the run-length encoded segments as `count x segment.`, where `count` is the number of repetitions of a segment, and `segment` is the actual 2-digit pair.

- **`encode_string`**: This function processes the converted string in 2-digit segments, applying run-length encoding to compress the string.

- **Test String**: The test string `"how to hack instagram"` is used in the example. The script converts this string, encodes it, and then provides detailed length analysis for each step.

---

### Example Output

```bash
password before converting:  how to hack instagram
its length is  23 

password after converting:  080920179507949501515251435063050106093920539150420395129
its length is  72
it increased by  49
its increase percentage is  213.04 %

password after encoding:  1x08.1x09.1x20.1x17.1x19.1x05.1x07.1x09.1x49.1x50.1x15.1x15.1x25.1x15.1x42.1x05.1x29.1x50.
its length is  68
it increased by  -4
its increase percentage is  -5.56 %

net increase in length:  45
net increase percentage:  195.65 %
```

In this example, the conversion process significantly increases the string's length, while the encoding step compresses the string slightly.

---

### Analysis

- **Character Conversion**: The transformation from plain text to numeric encoding causes a significant increase in string length. This happens because each character is mapped to a 2-digit number, resulting in more characters in the final output.
  
- **Run-Length Encoding (RLE)**: The run-length encoding can either increase or decrease the length of the converted string. If there are repeating 2-digit segments, the string will be shortened; otherwise, it may remain almost the same or grow slightly due to the extra count information.

---

### License

This project is open-source and licensed under the MIT License. Feel free to contribute or use it in your projects!

---

### Future Enhancements

- **Custom Mappings**: Allow users to define their own mappings for characters to numerical values.
- **Enhanced Compression**: Integrate other compression algorithms to improve the size reduction after conversion and encoding.
- **GUI Interface**: Build a simple user interface to provide easier interaction for non-technical users.

---

Let me know if you need any modifications or additional details!