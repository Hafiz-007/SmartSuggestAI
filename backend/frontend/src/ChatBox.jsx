import React, { useState } from 'react';

function ChatBox() {
  const [query, setQuery] = useState('');
  const [chat, setChat] = useState([]);

  const sendQuery = async () => {
    const res = await fetch('http://localhost:5000/ask', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query })
    });
    const data = await res.json();
    setChat([...chat, { q: query, a: data.response }]);
    setQuery('');
  };

  return (
    <div>
      <div style={{ marginBottom: '1rem' }}>
        {chat.map((c, i) => (
          <div key={i}>
            <b>You:</b> {c.q}<br/>
            <b>AI:</b> {c.a}
            <hr/>
          </div>
        ))}
      </div>
      <input value={query} onChange={e => setQuery(e.target.value)} placeholder="Ask anything..." />
      <button onClick={sendQuery}>Send</button>
    </div>
  );
}

export default ChatBox;