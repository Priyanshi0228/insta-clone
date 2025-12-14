import { useEffect, useState } from "react";
import API from "../api";
import Navbar from "../components/Navbar";

export default function Profile() {
  const [user, setUser] = useState({});
  const [posts, setPosts] = useState([]);

  const fetchProfile = async () => {
    try {
      const res = await API.get("/users/me");
      setUser(res.data.user);
      setPosts(res.data.posts);
    } catch (err) { console.log(err); }
  };

  useEffect(() => { fetchProfile(); }, []);

  return (
    <div>
      <Navbar />
      <h2>{user.username}'s Profile</h2>
      <p>Email: {user.email}</p>
      <p>Followers: {user.followers_count} | Following: {user.following_count}</p>
      <h3>Posts:</h3>
      {posts.map(post => (
        <div key={post.id} style={{border: "1px solid gray", margin: "5px", padding: "5px"}}>
          <img src={post.image_url} alt="post" style={{width: "100px"}} />
          <p>{post.caption}</p>
        </div>
      ))}
    </div>
  );
}
