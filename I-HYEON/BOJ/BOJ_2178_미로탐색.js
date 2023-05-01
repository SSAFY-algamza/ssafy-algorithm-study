let fs = require('fs');
let input = fs.readFileSync('./dev/stdin').toString().split('\n');

const delta = [[-1, 0], [1, 0], [0, 1], [0, -1]];
const [N, M] = input.shift().split(' ').map(Number);  // 4 6 이 각각 들어감
const distance = [...Array(N)].map(e=>Array(M).fill(0));
const graph = [];
for (let i = 0; i<N;i++){
  graph.push([...input[i].replace(/\r/g,'').split('').map(Number)])
}
//bfs이용
// console.log(graph[2][2])
const queue = [[0,0]]  // queue에 첫 좌표를 담음
graph[0][0] = 0  // 방문표시
distance[0][0] = 1  //이동거리를 기록
while(queue.length){
  const [x,y] = queue.shift();  // x,y에 큐의 첫좌표 각각을 할당

  for(let i = 0; i<4; i++){
    const nx = x + delta[i][0];
    const ny = y + delta[i][1];

    if (nx<0 || ny<0 || nx >=N || ny >=M)continue;
    if (graph[nx][ny]){
      queue.push([nx,ny])  //큐에 추가하고
      graph[nx][ny] = 0;  //방문 미리 표시
      distance[nx][ny] = distance[x][y] + 1;
    }
  }
}

console.log(distance[N-1][M-1])