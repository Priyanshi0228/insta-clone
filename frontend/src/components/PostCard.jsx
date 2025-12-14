import { useState } from "react";
import API from "../api";

export default function PostCard({ post, onComment }) {
  const [liked, setLiked] = useState(post.liked_by_user || false);
  const [likes, setLikes] = useState(post.likes_count || 0);

  const toggleLike = async () => {
    try {
      if (liked) await API.post(`/posts/${post.id}/unlike`);
      else await API.post(`/posts/${post.id}/like`);

      setLiked(!liked);
      setLikes(liked ? likes - 1 : likes + 1);
    } catch (err) { console.log(err); }
  };

  return (
    <div style={{border: "1px solid gray", margin: "10px", padding: "10px"}}>
      <img src={post.image_url} alt="post" style={{width: "100%"}} />
      <p>{post.caption}</p>
      <p>{likes} Likes</p>
      <button onClick={toggleLike}>{liked ? "Unlike" : "Like"}</button>
      <div>
        <button onClick={() => onComment(post.id)}>Comments ({post.comments?.length || 0})</button>
      </div>
    </div>
  );
}
