from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)


users = {
    "1": {"name": "IT", "email": "it@email.com"},
    "2": {"name": "Sara", "email": "sara@email.com"},
    "3": {"name": "Nora", "email": "nora@email.com"}
}

flag = "CTF{IDOR_is_fun}"


@app.route('/')
def home():
    html = """
<!DOCTYPE html>
<html>
<head>
<title>CTF Challenge</title>
<style>
body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: linear-gradient(135deg, #0f172a, #020617);
    color: white;
    text-align: center;
}

.container {
    margin-top: 100px;
}

h1 {
    font-size: 40px;
    background: linear-gradient(90deg, #38bdf8, #22c55e);
    -webkit-background-clip: text;
    color: transparent;
}

p {
    color: #94a3b8;
    font-size: 18px;
}

.button {
    margin: 15px;
    padding: 15px 30px;
    font-size: 16px;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    color: white;
    background: linear-gradient(135deg, #3b82f6, #06b6d4);
    box-shadow: 0 0 15px rgba(59,130,246,0.6);
    transition: 0.3s;
}

.button:hover {
    transform: scale(1.1);
    box-shadow: 0 0 25px rgba(6,182,212,0.9);
}

.footer {
    position: fixed;
    bottom: 20px;
    width: 100%;
    color: #64748b;
    font-size: 14px;
}
</style>
</head>

<body>

<div class="container">
    <h1> IDOR Challenge</h1>
    <p>Think like a hacker... find the hidden flag </p>
    <p>Hint: Open DevTools → Network tab</p>

    <button class="button" onclick="getProfile(1)">View Profile 1</button>
    <button class="button" onclick="getProfile(2)">View Profile 2</button>
</div>

<div class="footer">
    Made  by @_secit
</div>

<script>
function getProfile(id){
    fetch('/api/user?id=' + id)
    .then(response => response.json())
    .then(data => {
        alert(JSON.stringify(data, null, 2));
    });
}
</script>

</body>
</html>
"""
    
    return render_template_string(html)

# الـ API
@app.route('/api/user')
def get_user():
    user_id = request.args.get('id')
    if user_id == "3":
        return jsonify({"flag": flag})
    return jsonify(users.get(user_id, {"error": "User not found"}))

app.run(host="0.0.0.0", port=3000, debug=True)
