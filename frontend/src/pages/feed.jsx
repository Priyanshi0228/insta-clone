import { useEffect, useState } from "react";
import api from "../api/axios";
import Navbar from "../components/Navbar";
import PostCard from "../components/PostCard";

export default function Feed() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    api.get("/feed").then((res) => setPosts(res.data));
  }, []);

  return (
    <>
      <Navbar />
      <div className="max-w-md mx-auto mt-6">
        {posts.map((p) => (
          <PostCard key={p.id} post={p} onLike={() => {}} />
        ))}
      </div>
    </>
  );
}
