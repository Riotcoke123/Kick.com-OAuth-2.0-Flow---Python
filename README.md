<h1>Kick.com OAuth2 Token Handler</h1>

<p>This project implements a FastAPI-based OAuth2 authorization flow with auto-refreshing tokens for Kick.com's API. It securely stores tokens and refreshes them automatically every 30 minutes.</p>

<hr>

<h2>🔧 Prerequisites</h2>
<ul>
  <li>Python 3.7+</li>
  <li>Dependencies:
    <pre><code>pip install fastapi uvicorn apscheduler requests python-dotenv</code></pre>
  </li>
  <li>A Kick Developer App with:
    <ul>
      <li>Client ID</li>
      <li>Client Secret</li>
      <li>Redirect URI (e.g. http://localhost:8000/callback)</li>
    </ul>
  </li>
</ul>

<hr>

<h2>📁 Project Structure</h2>
<pre><code>
kick_oauth/
├── main.py              &lt;-- FastAPI app
├── token_utils.py       &lt;-- Token handling logic
├── .env                 &lt;-- Store secrets (not committed)
├── tokens.json          &lt;-- Stores current access/refresh tokens
</code></pre>

<hr>

<h2>⚙️ .env Example</h2>
<pre><code>
CLIENT_ID=your_kick_client_id
CLIENT_SECRET=your_kick_client_secret
REDIRECT_URI=http://localhost:8000/callback
</code></pre>

<hr>

<h2>🚀 How to Use</h2>
<ol>
  <li>Run the app:
    <pre><code>python main.py</code></pre>
  </li>
  <li>Your browser will open automatically and ask for Kick API authorization.</li>
  <li>After authorization, your tokens are saved in <code>tokens.json</code>.</li>
  <li>Tokens will refresh every 30 minutes using an internal job scheduler (APScheduler).</li>
</ol>

<hr>

<h2>🔁 Token Refresh Logic</h2>
<p>APScheduler runs a background job every 30 minutes that:</p>
<ul>
  <li>Reads <code>refresh_token</code> from <code>tokens.json</code></li>
  <li>Posts it to Kick's token endpoint</li>
  <li>Overwrites <code>tokens.json</code> with the new access and refresh tokens</li>
</ul>

<hr>

<h2>🔒 Security Note</h2>
<ul>
  <li><strong>Never commit</strong> your <code>.env</code> or <code>tokens.json</code> to public repositories.</li>
  <li>Consider encrypting token storage for production use.</li>
</ul>

<hr>

<h2>📚 Useful Links</h2>
<ul>
  <li><a href="https://kick.com/">Kick.com</a></li>
  <li><a href="https://fastapi.tiangolo.com/">FastAPI Documentation</a></li>
  <li><a href="https://apscheduler.readthedocs.io/">APScheduler Docs</a></li>
</ul>
