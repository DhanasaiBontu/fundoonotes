import { useState } from "react";
import { Link } from "react-router-dom";
import { forgotPassword } from "../services/api";
import "../styles/auth.css";

export default function ForgotPassword() {
  const [email, setEmail] = useState("");
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setMessage("");

    try {
      await forgotPassword({ email });
      setMessage("Reset token sent. Check your email.");
      setEmail("");
    } catch (err) {
      setError(
        err.response?.data?.detail ||
        "Unable to send reset email"
      );
    }
  };

  return (
    <div className="auth-page">
      <div className="auth-card">
        <div className="auth-header">✓ Fundoo Notes</div>

        <h2>Forgot password</h2>
        <p className="sub-text">Enter your registered email</p>

        <form onSubmit={handleSubmit}>
          <input
            type="email"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />

          <button type="submit">Send Reset Token</button>
        </form>

        {message && <p className="success-text">{message}</p>}
        {error && <p className="error-text">{error}</p>}

        <p className="link-text">
          Back to <Link to="/login">Login</Link>
        </p>
      </div>
    </div>
  );
}
