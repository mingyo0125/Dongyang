import { useState } from "react";

function TodoList() {
  const [input, setInput] = useState("");
  const [todos, setTodos] = useState([]);

  // 할 일 추가
  const addTodo = () => {
    if (input.trim() === "") return; // 빈 입력 방지
    setTodos([...todos, input]);     // 기존 목록에 새 항목 추가
    setInput("");                    // 입력창 초기화
  };

  // 할 일 삭제
  const removeTodo = (index) => {
    setTodos(todos.filter((_, i) => i !== index)); // 클릭된 인덱스 제외
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>To-Do 리스트</h2>
      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="할 일을 입력"
      />
      <button onClick={addTodo}>추가</button>

      <ul>
        {todos.map((todo, index) => (
          <li key={index}>
            {todo}
            <button onClick={() => removeTodo(index)}>삭제</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default TodoList;