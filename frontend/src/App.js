import { useState } from "react";
import axios from "axios";

function App() {
  const [question, setQuestion] = useState("");
  const [response, setResponse] = useState("");

  const askAI = async () => {
    const res = await axios.post("http://localhost:5000/ask", { question });
    setResponse(res.data.answer);
  };

  return (
    <div className="App">
      <h1>AI Personal Tutor</h1>
      <textarea value={question} onChange={(e) => setQuestion(e.target.value)} placeholder="Ask a question..." />
      <button onClick={askAI}>Ask</button>
      <p>{response}</p>
    </div>
  );
}

export default App;
