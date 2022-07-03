### D3 - 2805(농작물 수확하기)
___

[링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GLXqKAWYDFAXB)

시간복잡도 : O(N) 

#### 풀이
1. 각 TC마다 2차원 농장배열, 배열의 크기를 입력받는다.
2. 정사각형 내부의 가장 큰 마름모 형태로 수확이 가능하므로, 각행에서 열 위치가 \[abs(중간위치 - 현재위치) ~ 배열길이 - abs(중간위치 - 현재위치)\] 크기만큼 수확량에 더한다.
3. 정답값을 출력한다.
___
### 참고  