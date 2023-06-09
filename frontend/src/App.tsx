import { useState } from "react";

function App() {
  const [input, setInput] = useState<string>();
  const [output, setOutput] = useState<string>("");

  const handleGenerate = (type: string) => {
    if (!input) return alert("Angka belum di input!");
    const regex = /^[0-9]*$/;
    if (!regex.test(input)) return alert("Input hanya boleh angka");
    setOutput("");
    fetch("http://localhost:5000/api", {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({
        type: type,
        data: input,
      }),
    })
      .then((response) => response.json())
      .then((responseData) => {
        const { data, message, status } = responseData;
        if (!status) return alert(message);
        setOutput(data);
      });
  };

  return (
    <div className="bg-white">
      <input
        type="text"
        placeholder="Input Angka"
        style={{ marginBottom: "10px" }}
        value={input}
        onChange={(e) => setInput(e.currentTarget.value)}
      />
      <div>
        <button onClick={() => handleGenerate("segitiga")}>
          Generate Segitiga
        </button>
        <button
          style={{ margin: "0px 10px" }}
          onClick={() => handleGenerate("ganjil")}
        >
          Generate Bilangan Ganjil
        </button>
        <button onClick={() => handleGenerate("prima")}>
          Generate Bilangan Prima
        </button>
      </div>
      <h3>Result</h3>
      <div dangerouslySetInnerHTML={{ __html: output }}></div>
    </div>
  );
}

export default App;
