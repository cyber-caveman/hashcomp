# Import the hashlib and sys modules
import hashlib
import sys

# Define a function to print the help message
def print_help():
    # Print the usage information
    print("Usage: python hashcomp.py file hash_type hash_code")
    print("file: the name of the file to compute the hash")
    print("hash_code: the expected hash code of the file")
    print("hash_type: the type of hash algorithm to use")
    # Print the list of available hash algorithms
    print("Available hash algorithms:")
    for name in hashlib.algorithms_available:
        print(name)

# Check if the script is called without arguments or with -h argument
if len(sys.argv) == 1 or sys.argv[1] == "-h":
    # Print the help message and exit
    print_help()
    sys.exit()
else:
    # Get the file name, the hash code, and the hash type from command line arguments
    file = sys.argv[1]
    hash_type = sys.argv[2]
    hash_code = sys.argv[3]
    
# Open the file in binary mode
with open(file, "rb") as f:
    # Read the file content
    data = f.read()
    # Try to compute the hash using the specified algorithm
    try:
        hash = hashlib.new(hash_type, data).hexdigest()
        # Print the file name, the hashes, and the hash type
        print(f"File: {file}")
        print(f"Given hash: {hash_code}")
        print(f"Computed hash: {hash}")
        print(f"Hash type: {hash_type}")
        # Compare the hashes and print a message
        if hash == hash_code:
            print("The hashes match.")
        else:
            print("The hashes do not match.")
    # Catch the ValueError exception if the hash type is not recognized
    except ValueError as e:
        # Print the error message
        print(f"Error: {e}")