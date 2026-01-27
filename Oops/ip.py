from flask import Flask, request, redirect

app = Flask(__name__)

# This is the "trap" link
@app.route('/view-meme')
def log_info():
    # 1. Capture the user's Public IP address
    user_ip = request.remote_addr
    
    # 2. Capture Browser/Device info (User-Agent)
    user_agent = request.headers.get('User-Agent')
    
    # 3. Print the data to your console (or save to a file)
    print(f"--- New Connection Captured ---")
    print(f"IP Address: {user_ip}")
    print(f"Device Info: {user_agent}")
    print(f"-------------------------------")

    # 4. Redirect the user to the actual content so they don't suspect anything
    return redirect("https://i.imgur.com/d6H863L.jpg") 

if __name__ == '__main__':
    # Running on port 5000
    app.run(host='0.0.0.0', port=5000)