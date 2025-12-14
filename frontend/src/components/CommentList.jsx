export default function CommentList({ comments }) {
  return (
    <div>
      {comments.map((c) => (
        <div key={c.id} style={{borderTop: "1px solid lightgray", padding: "5px"}}>
          <b>{c.username}</b>: {c.text}
        </div>
      ))}
    </div>
  );
}
