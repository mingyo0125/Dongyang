// 1. http 모듈 불러오기
const http = require("http");

// 2. 서버 생성과 요청 처리
const server = http.createServer((req, res) => {
  res.setHeader("Content-Type", "text/plain; charset=utf-8");

  if (req.url === "/") {
    res.end("메인 페이지입니다.");
  } else if (req.url === "/about") {
    res.end("소개 페이지입니다.");
  } else {
    res.statusCode = 404;
    res.end("페이지를 찾을 수 없습니다.");
  }
});

// 3. 포트 리스닝
server.listen(3000, () => {
  console.log("서버 실행 중: http://localhost:3000");
});