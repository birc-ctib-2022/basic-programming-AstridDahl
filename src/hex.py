import sys

# This program should take two arguments, a command--either "encode" or "decode"--
# and then a string.

if len(sys.argv) != 3:
    print("Incorrect number of arguments.", file=sys.stderr)
    print(f"Usage: {sys.argv[0]} command string\n", file=sys.stderr)
    sys.exit(1)

command, x = sys.argv[1:3]

match command:
    case "encode":
        # Implement the encoding here
        encoding = ""
        hex_list=[hex(ord(c)) for c in x]
        encoding=''.join(hex_list)
        
        print(encoding)

    case "decode":
        # Implement the decoding here
        decoding = ""
        hex_list=x.split('0x')
        hex_list.pop(0)
        chr_list=[chr(int(string, base=16)) for string in hex_list]
        decoding=''.join(chr_list)

        print(decoding)


