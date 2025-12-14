import { Link, useNavigate } from "react-router-dom";
import { removeToken, isAuthenticated } from "../utils/auth";

export default function Navbar() {
  const navigate = useNavigate();

  const handleLogout = () => {
    removeToken();
    navigate("/");
  };

  return (
    <nav style={{padding: "10px", borderBottom: "1px solid gray"}}>
      <Link to="/home">Home</Link> |{" "}
      <Link to="/create">Create Post</Link> |{" "}
      <Link to="/profile">Profile</Link> |{" "}
      {isAuthenticated() && <button onClick={handleLogout}>Logout</button>}
    </nav>
  );
}
