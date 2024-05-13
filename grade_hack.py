
import string

# ANSI Color codes for output formatting
PURPLE = '\033[95m'
RED = '\033[91m'
YELLOW = '\033[93m'
GREEN = '\033[92m'
WHITE = '\033[97m'  # Bright white color for text
RESET = '\033[0m'   # Reset to default color

def print_ascii_art():
    """Prints ASCII art in purple color at the beginning of the script."""
    ascii_art = """
  _____                               _____ _____ _______ 
 |  __ \                             / ____|  __ \__   __|
 | |__) |_____   _____ _ __ ___  ___| |  __| |__) | | |   
 |  _  // _ \ \ / / _ \ '__/ __|/ _ \ | |_ |  ___/  | |   
 | | \ \  __/\ V /  __/ |  \__ \  __/ |__| | |      | |   
 |_|  \_\___| \_/ \___|_|  |___/\___|\_____|_|      |_|   
    """
    print(PURPLE + ascii_art + RESET)

def unmangle_and_filter(encoded_bytes):
    """
    Unmangles encoded bytes (specific to Level Two) by reversing a transformation.
    Only keeps printable characters after unmangling.
    """
    unmangled_bytes = bytearray()
    for byte in encoded_bytes:
        new_byte = (byte + 19) % 256  # Reverse the transformation by adding 19 to each byte
        if chr(new_byte) in string.printable:
            unmangled_bytes.append(new_byte)
    return unmangled_bytes

def decrypt_level_three_xor_with_ascii(encoded_bytes, user_id):
    """
    Decrypts encoded bytes (specific to Level Three) using XOR operation.
    Each byte is XORed with the ASCII value of a corresponding character in the user ID.
    """
    user_id_ascii_values = [ord(char) for char in user_id]
    decrypted_bytes = bytearray()
    for i, byte in enumerate(encoded_bytes):
        decrypted_byte = byte ^ user_id_ascii_values[i % len(user_id_ascii_values)]
        if chr(decrypted_byte) in string.printable:
            decrypted_bytes.append(decrypted_byte)
    return decrypted_bytes

def read_grade_file(file_path):
    """Reads the entire content of the grade file."""
    with open(file_path, 'rb') as file:
        return file.read()

def format_hex_content(content, start_index, end_index, color):
    """
    Formats the specified part of file content in hex format.
    Applies the given color to the formatted hex content.
    """
    hex_content = ""
    for i in range(start_index, end_index):
        if i % 16 == 0:
            hex_content += '\n'
        if i % 2 == 0:
            hex_content += ' '
        hex_content += format(content[i], '02x')
    return color + hex_content + '\033[0m'

def main():
    """Main function to process the grade file and display the output."""
    print_ascii_art()

    file_path = 'grade.txt'
    user_id = "20232024"

    # Read and process the content of the grade file
    content = read_grade_file(file_path)

    # Define the lengths and start index for each level
    level_one_length = 64  # Level One finishes after 64 bytes
    level_two_length = 47  # Length of Level Two
    level_three_index = 111  # Start index of Level Three

    # Decrypt or process each level
    level_one_grade = content[:level_one_length].decode()
    level_two_grade = unmangle_and_filter(content[level_one_length:level_one_length + level_two_length]).decode()
    decrypted_level_three = decrypt_level_three_xor_with_ascii(content[level_three_index:], user_id)
    level_three_grade = decrypted_level_three.decode('utf-8', 'replace')

    # Hex representation with color
    hex_with_color = format_hex_content(content, 0, level_one_length, RED)
    hex_with_color += format_hex_content(content, level_one_length, level_one_length + level_two_length, YELLOW)
    hex_with_color += format_hex_content(content, level_three_index, len(content), GREEN)

    # Print grades with explanations and color coding
    print(WHITE + "Level One Grade: " + RED + level_one_grade + RESET + "Explanation: Level One ends after 64 bytes, including a newline character" + WHITE + " '0a'" + RESET + ".\n")
    print(WHITE + "Level Two Grade: " + YELLOW + level_two_grade + RESET + "Explanation: Level Two starts immediately after Level One and is 47 bytes long.\n")
    print(WHITE + "Level Three Grade: " + GREEN + level_three_grade + RESET + "\nExplanation: Level Three starts at byte offset 111, immediately after Level Two.")
    print("Level Three can be influenced by creating file named"  + WHITE +' "h4x_those_grades!" ' + RESET + "and specifying grade that we want to get.\n") 

    # Display hex representation of the file with color coding
    print(WHITE + "Hex Representation from grade.txt with color coding:" + RESET)
    print(hex_with_color)

if __name__ == "__main__":
    main()
