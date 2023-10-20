import socket

# Client configuration
server_host = '10.30.8.70'  # Server IP address or hostname
server_port = 50003

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_host, server_port))

# Client loop
while True:
    # Get user input
    message = input("Enter message to send (or 'quit' to exit): ")

    # Send the message to the server
    client_socket.send(message.encode())

    if message.lower() == 'quit':
        break

    # Receive and display the response from the server
    response = client_socket.recv(1024).decode()
    print(f"Received from server: {response}")

# Close the socket
client_socket.close()
