import React, { useState } from "react";
import axiosInstance from "../redux/axiosInstance";

const ShellSuggester = () => {
  const [keyword, setKeyword] = useState("");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

const handleSuggest = async (type) => {
    if (!keyword.trim()) {
    setResult("Please enter a keyword.");
    return;
  }
  setLoading(true);
  setResult(""); // or setResult([])
  try {
    const endpoint = type === "creative" ? "/shells/creative" : "/shells/suggest";
    const response = await axiosInstance.post(endpoint, { keyword });
    // For creative: response.data.suggestion (string)
    // For real: response.data.suggestions (array)
    if (type === "creative") {
      setResult(response.data.suggestion);
    } else {
    setResult(response.data.suggestions);
    }
  } catch (err) {
    setResult("Free API limit reached. Subscribe to unlock creative suggestions.");
  }
  setLoading(false);
};

  return (
    <div className="shell-suggester">
      <input
        type="text"
        placeholder="Keyword (e.g. leafy, fossil, colorful)"
        value={keyword}
        onChange={e => setKeyword(e.target.value)}
        className="shell-suggester-input"
      />
      <div className="shell-suggester-buttons">
        <button onClick={() => handleSuggest("real")}>Find Real Seashell</button>
        <button onClick={() => handleSuggest("creative")}>MAKE Creative Name</button>
      </div>
      {loading && <div className="suggestion-loading">Loading...</div>}
    {Array.isArray(result) ? (
    <ul className="suggestion-result">
  {result.map((s, i) => {
    // Extract the scientific name before the first '(' for a cleaner search
    const searchTerm = s.split('(')[0].trim();
    const wikiUrl = `https://en.wikipedia.org/wiki/Special:Search?search=${encodeURIComponent(searchTerm)}`;
    return (
      <li key={i}>
        <a href={wikiUrl} target="_blank" rel="noopener noreferrer">
          {s}
        </a>
      </li>
    );
  })}
</ul>
    ) : (
    result && <div className="suggestion-result">{result}</div>
    )}
    </div>
  );
};

export default ShellSuggester;