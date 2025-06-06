<!DOCTYPE html>
<html lang="en">
<head>

</head>
<body>

<h1>Python OAuth 2.0 Flow for Kick.com</h1>

<p>This is a simple Python script demonstrating how to perform an OAuth 2.0 authorization code flow with <a href="https://kick.com" target="_blank">Kick.com</a>. It helps you retrieve access and refresh tokens for accessing user-specific APIs.</p>

<h2>⚙️ Requirements</h2>
<ul>
  <li>Python 3.x</li>
  <li><code>requests</code> library (install via <code>pip install requests</code>)</li>
</ul>

<h2>📦 Setup</h2>

<ol>
  <li><strong>Register your application on Kick.com</strong> to obtain:
    <ul>
      <li><code>CLIENT_ID</code></li>
      <li><code>CLIENT_SECRET</code></li>
      <li><code>REDIRECT_URI</code></li>
    </ul>
  </li>
  <li><strong>Update the script</strong> with your credentials:</li>
</ol>

<pre><code>CLIENT_ID = "your_client_id_here"
CLIENT_SECRET = "your_client_secret_here"
REDIRECT_URI = "http://localhost:8000/callback"  # Or your registered URI
</code></pre>

<ol start="3">
  <li><strong>Install dependencies</strong>:</li>
</ol>

<pre><code>pip install requests</code></pre>

<h2>🚀 How to Use</h2>

<ol>
  <li>Run the script:</li>
</ol>

<pre><code>python kick_oauth.py</code></pre>

<ol start="2">
  <li>Visit the authorization URL printed in the terminal.</li>
  <li>After authorizing, you’ll be redirected to your redirect URI with a <code>code</code> in the query params.</li>
  <li>Paste that code back into the terminal when prompted.</li>
  <li>You’ll receive and see:
    <ul>
      <li>Access Token</li>
      <li>(Optional) Refresh Token</li>
    </ul>
  </li>
</ol>

<h2>🧪 Example</h2>

<pre><code>$ python kick_oauth.py
Visit this URL to authorize:
https://kick.com/oauth2/authorize?client_id=...&amp;redirect_uri=...&amp;response_type=code&amp;scope=user_read
Paste the authorization code here: abc123
Access Token: eyJ0eXAiOiJK...
Refresh Token: None
</code></pre>

<h2>🛑 Notes</h2>
<ul>
  <li>Ensure your redirect URI is exactly as registered on Kick.com.</li>
  <li>The <code>scope</code> can be adjusted depending on the permissions you need.</li>
</ul>

<h2>📄 License</h2>
<p>This project is licensed under the <strong>GNU General Public License (GPL)</strong>.</p>
<p>You may copy, distribute, and modify the software as long as you track changes/dates in source files and keep the same license. Any derivative work must also be open-source and licensed under GPL.</p>
<p>See the full license text here: <a href="https://www.gnu.org/licenses/gpl-3.0.en.html" target="_blank">https://www.gnu.org/licenses/gpl-3.0.en.html</a></p>

</body>
</html>
