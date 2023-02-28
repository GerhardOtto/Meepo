import base64

def touchBase(file_path):
    # Open the text file in binary mode and read its contents
    with open(file_path, 'rb') as file:
        file_contents = file.read()

    # Encode the file contents to base64
    encoded_contents = base64.b64encode(file_contents)

    # Convert the bytes to a string and return the result
    return encoded_contents.decode('utf-8')
