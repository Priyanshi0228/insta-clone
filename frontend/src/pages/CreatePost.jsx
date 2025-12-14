import { useState } from "react";
import { useNavigate } from "react-router-dom";
import API from "../api";
import Navbar from "../components/Navbar";

export default function CreatePost() {
  const [image, setImage] = useState("");
  const [caption, setCaption] = useState("");
  const navigate = useNavigate();

  const handleCreate = async (e) => {
    e.preventDefault();
    try {
      await API.post("/posts/", { image_url: image, caption });
      alert("Post created!");
      navigate("/home");
    } catch (err) { alert("Failed to create post"); }
  };

  return (
    <div>
      <Navbar />
      <h2>Create Post</h2>
      <form onSubmit={handleCreate}>
        <input placeholder="Image URL" value={image} onChange={e=>setImage(e.target.value)} />
        <input placeholder="Caption" value={caption} onChange={e=>setCaption(e.target.value)} />
        <button type="submit">Post</button>
      </form>
    </div>
  );
}
