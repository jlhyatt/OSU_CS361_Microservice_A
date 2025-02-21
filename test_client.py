import socket
import json

# Test client program
def test_client():
    def send_request(request_data):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("127.0.0.1", 65432))
        client_socket.send(json.dumps(request_data).encode("utf-8"))
        response = client_socket.recv(1024).decode("utf-8")
        client_socket.close()
        return response
    
    budgets = [
        {"name": "Groceries", "amount": 500},
        {"name": "Rent", "amount": 1200},
        {"name": "Utilities", "amount": 200},
        {"name": "Entertainment", "amount": 100},
        {"name": "Savings", "amount": 300}
    ]
    
    for budget in budgets:
        print("Adding budget:", send_request({"action": "add_budget", "name": budget["name"], "amount": budget["amount"]}))
    
    print("Getting budgets:", send_request({"action": "get_budgets"}))
    
    for budget in budgets:
        print("Removing budget:", send_request({"action": "remove_budget", "name": budget["name"]}))
    
    print("Getting budgets after removal:", send_request({"action": "get_budgets"}))

if __name__ == "__main__":
    test_client()