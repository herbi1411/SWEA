### D2 - 1859(백만장자프로젝트)
___

[링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LrsUaDxcDFAXc)

시간복잡도 : O(N)

#### 풀이
1. 배열에서 판매가격인 최대값을 저장할 sellPrice, 정답을 저장할 answer을 선언한다.
2. 초기 sellPrice값을 0으로 하고, 배열을 거꾸로 순회한다.
3. 순회하며 값이 sellPrice보다 작으면 answer에 sellPrice - 값을 더하고, 아니면 sellPrice를 현재 값으로 update한다.
 
___
### 참고  
* 정답 제출할때 \#number를 붙여야 하는 조건을 못봐서 여러번 틀렸다.