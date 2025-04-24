source_filename = "source.txt"
destination_filename = "output.txt"

# Read from source file and process
with open(source_filename, 'r') as source_file:
    original_content = source_file.read()
    uppercase_content = original_content.upper()

# Write processed content to destination file
with open(destination_filename, 'w') as dest_file:
    dest_file.write(uppercase_content)

print(f"File copied successfully with uppercase conversion to {destination_filename}")
