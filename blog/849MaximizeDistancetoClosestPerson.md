![holykiwi_big.png](https://cdn.steemitimages.com/DQmbwuk85jhorPvZoCb13F7gouFg5JH9gKPBWe4H5ecthQT/holykiwi_big.png)

# [코딩문제풀기 2일차] Maximize Distance to Closest Person

## Introduction

- leetcode 849번 문제입니다.

> Talk is cheap. Show me the code.      - 리누스 토발즈


## Problem

난이도: Easy

`seats` 배열에서 1은 좌석에 사람이 앉아있는 것을 의미하고, 0은 좌석이 비었다는 것을 의미한다.

빈 좌석이 적어도 하나 이상 있고, 앉아있는 사람도 적어도 하나 이상 있다.

알렉스는 부끄러움이 많아서 가장 가깝게 앉은 사람과 자신 사이의 거리가 최대가 되도록 앉고 싶다.

가장 가까운 사람과의 최대 거리를 반환해야한다.

**예제 1:**

```
Input: [1,0,0,0,1,0,1]
Output: 2
설명: 
알렉스가 두 번째 빈 좌석(seats[2])에 앉는다면, 가장 가까운 사람과의 거리는 2가 된다.
알렉스가 다른 빈 좌석에 앉는다면, 가장 가까운 사람과의 거리는 1이 된다.
따라서, 가장 가까운 사람과의 최대 거리는 2이다.
```

**예제 2:**

```
Input: [1,0,0,0]
Output: 3
설명: 
If Alex sits in the last seat, the closest person is 3 seats away.
만약 알렉스가 마지막 좌석에 앉는다면, 가장 가까운 사람과의 거리는 3이다.
이것이 가능한 최대 거리로 앉은 것이므로 답은 3이다.
```

**유의사항:**

1. `1 <= seats.length <= 20000`
2. `seats` 오직 0과 1만 포함하며, `0`이 적어도 하나 이상 있고, `1`도 적어도 하나 이상 있다.

## Solution

### My Solution

```javascript
let maxDistToClosest = seats => {
    let max = 0;
    seats.join('').split('1').forEach((v, i, a) => {
        let tmp = (i === 0 || i === a.length - 1) ? v.length : Math.ceil(v.length/2);
        if (tmp > max) max = tmp;
    });
    return max;
};
```

> 2018/06/20 Written by Jon Jee

----------