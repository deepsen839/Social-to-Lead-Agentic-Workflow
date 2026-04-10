import { useState, useEffect, useRef } from "react";
import axios from "axios";

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const sendMessage = async () => {
    if (!input.trim() || loading) return;

    const userMsg = { role: "user", text: input };
    setMessages((prev) => [...prev, userMsg]);

    setLoading(true);

    try {
      const res = await axios.post("/api/chat", {
        session_id: "user1",
        message: input,
      });

      const botMsg = { role: "bot", text: res.data.response };
      setMessages((prev) => [...prev, botMsg]);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        { role: "bot", text: "⚠️ Error connecting to server" },
      ]);
    }

    setLoading(false);
    setInput("");
  };

  return (
    <div style={styles.container}>
      <h2 style={styles.header}>AutoStream AI 🤖</h2>

      <div style={styles.chatBox}>
        {messages.map((m, i) => (
          <div
            key={i}
            style={{
              display: "flex",
              justifyContent:
                m.role === "user" ? "flex-end" : "flex-start",
              marginBottom: "10px",
            }}
          >
            <div
              style={{
                background:
                  m.role === "user" ? "#4f46e5" : "#e5e7eb",
                color: m.role === "user" ? "white" : "black",
                padding: "10px 14px",
                borderRadius: "15px",
                maxWidth: "70%",
              }}
            >
              <p style={{ margin: 0, whiteSpace: "pre-line" }}>
                {m.text}
              </p>
            </div>
          </div>
        ))}

        {loading && (
          <div style={{ marginBottom: "10px" }}>
            <div style={styles.botBubble}>🤖 Typing...</div>
          </div>
        )}

        <div ref={bottomRef}></div>
      </div>

      <div style={styles.inputArea}>
        <input
          style={styles.input}
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask something..."
          onKeyDown={(e) => e.key === "Enter" && sendMessage()}
        />
        <button style={styles.button} onClick={sendMessage}>
          Send
        </button>
      </div>
    </div>
  );
}

const styles = {
  container: {
    maxWidth: "700px",
    margin: "40px auto",
    fontFamily: "Arial",
  },
  header: {
    textAlign: "center",
    marginBottom: "20px",
  },
  chatBox: {
    height: "500px",
    overflowY: "auto",
    border: "1px solid #ddd",
    borderRadius: "10px",
    padding: "15px",
    background: "#f9fafb",
  },
  botBubble: {
    background: "#e5e7eb",
    padding: "10px 14px",
    borderRadius: "15px",
    maxWidth: "70%",
  },
  inputArea: {
    display: "flex",
    gap: "10px",
    marginTop: "10px",
  },
  input: {
    flex: 1,
    padding: "10px",
    borderRadius: "8px",
    border: "1px solid #ccc",
  },
  button: {
    padding: "10px 16px",
    borderRadius: "8px",
    border: "none",
    background: "#4f46e5",
    color: "white",
    cursor: "pointer",
  },
};

export default App;
