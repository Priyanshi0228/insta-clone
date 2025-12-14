import { useEffect, useState } from "react";
import API from "../api";
import Navbar from "../components/Navbar";
import PostCard from "../components/PostCard";
import CommentList from "../components/CommentList";

export default function Home() {
  const [posts, setPosts] = useState([]);
  const [selectedPostComments, setSelectedPostComments] = useState([]);

  const fetchFeed = async () => {
    try {
      const res = await API.get("/feed/");
      setPosts(res.data);
    } catch (err) { console.log(err); }
  };

  const fetchComments = async (postId) => {
    try {
      const res = await API.get(`/posts/${postId}/comments`);
      setSelectedPostComments(res.data);
    } catch (err) { console.log(err); }
  };

  useEffect(() => { fetchFeed(); }, []);

  return (
    <div>
      <Navbar />
      <h2>Home Feed</h2>
      {posts.map(post => <PostCard key={post.id} post={post} onComment={fetchComments} />)}
      {selectedPostComments.length > 0 && (
        <div>
          <h3>Comments</h3>
          <CommentList comments={selectedPostComments} />
        </div>
      )}
    </div>
  );
}
