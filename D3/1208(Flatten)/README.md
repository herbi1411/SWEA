### D2 - 1208(Flatten)
___

[링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV139KOaABgCFAYh)

시간복잡도 : O(MN) (M: 박스이동횟수 N:배열길이)

#### 풀이
1. 각 TC마다 상자 이동 가능 횟수 M, 박스 배열을 입력받는다.
2. 각 차수마다 박스 배열에서 최댓값, 최솟값을 가지고 있는 위치를 구한다.
3. 최댓값에서는 1을 빼고, 최솟값에서는 1을 더한다.
4. 총 M번 반복한다.
5. 배열의 최댓값과 최솟값의 차를 answer에 저장하고 출력한다.
6. 10번 반복한다.
___
### 참고  
* 시간복잡도를 더 줄일 수 없을까..?  