import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import "../styles/auth.css";

export default function Login() {
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = (e) => {
    e.preventDefault();
    navigate("/notes");
  };

  return (
    <div className="auth-page">
      <div className="auth-card">
        <div className="auth-header">✔ Fundoo Notes</div>

        <div className="auth-body">
          <h2>Welcome back to Fundoo Notes</h2>

          <form onSubmit={handleLogin}>
            <input
              placeholder="Email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />

            <input
              type="password"
              placeholder="Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />

            <button type="submit">Login</button>
          </form>

          <div className="auth-footer">
            New user?
            <Link to="/register">Register</Link>
          </div>
        </div>
      </div>
    </div>
  );
}
