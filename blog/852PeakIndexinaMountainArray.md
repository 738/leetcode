# 1일차 산 배열의 꼭대기 인덱스

## Introduction

- 꾸준히 코딩문제를 풀기 위해서 스팀잇에 매일매일 푼 문제의 해설을 적어보려합니다.
- leetcode와 codewars 사이트를 주로 사용할 것입니다.

> Talk is cheap. Show me the code.      - 리누스 토발즈


## Problem

난이도: Easy

다음 속성을 따르는 `A`라는 산 배열이 있다:

- `A.length >= 3`
- `A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]`를 만족하는 `0 < i < A.length - 1`가 존재한다.

산 배열이 주어지면, `A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]`를 만족하는 `i`를 반환해야 한다.

**예제 1:**

```
Input: [0,1,0]
Output: 1
```

**예제 2:**

```
Input: [0,2,1,0]
Output: 1
```

**유의사항:**

1. `3 <= A.length <= 10000`
2. `0 <= A[i] <= 10^6`
3. `A`는 위에서 말했듯이 산이다.

문제 출처: [leetcode 852. Peak Index in a Mountain Array](https://leetcode.com/problems/peak-index-in-a-mountain-array/description/)

## Solution

* Javascript를 사용해서 두 방법으로 풀었습니다.
* 해설로 나온 나머지 두 방법도 설명드리겠습니다.
* [Github solution 코드 보기](https://github.com/JonJee/leetcode/blob/master/js/852PeakIndexinaMountainArray.js)

### Solution 1 : `forEach`를 사용한 기본적인 방법

```javascript
let peakIndexInMountainArray = A => {
    let peak = -1, index = -1;
    A.forEach((v, i) => {
        if (v > peak) {
            peak = v;
            index = i;
        }
    });
    return index;
};
```

* `A` 배열에서 `forEach`를 돌려서 최대값(`peak`)을 찾은 후, `index`에 그 최대값의 인덱스를 저장하고 있습니다.
* 시간복잡도는 *O(N)* 으로 *N*은 `A` 배열의 길이입니다.

### Solution 2 : `Array.indexOf()`와 `Math.max()`를 사용한 방법 (Very Simple!)

```javascript
let peakIndexInMountainArray = A => A.indexOf(Math.max(...A));
```

* `A` 배열에서 최대값을 구한 후, Javascript에 내장된 `indexOf` 함수를 사용해서 최대값의 인덱스를 가져오고 있습니다.
* 시간복잡도는 마찬가지로 *O(N)* 입니다.


// 여기서부터는 사이트에 나와있는 해설입니다.
### Solution 3 : Linear Scan

```javascript
let peakIndexInMountainArray = A => {
    let i = 0;
    while(A[i] < A[i + 1]) i++;
    return i;
}
```

* `i`를 증가시키면서 증가하는 구간에서 감소하는 구간으로 바뀌는 순간에 반복문을 탈출하여 i를 반환합니다.
* 시간복잡도는 마찬가지로 *O(N)* 입니다.

### Solution 4 : Binary Search (Very Important!!!)

```javascript
let peakIndexInMountainArray = A => {
    let lo = 0, hi = A.length - 1
    while (lo < hi) {
        let mi = Math.floor((lo + hi) / 2)
        if (A[mi] < A[mi + 1]) lo = mi + 1
        else hi = mi
    }
    return lo
}
```

* `A` 배열은 `A[i] < A[i+1]`이므로 `[true, true, true, ..., true, false, false, ..., false]`와 같이 나타낼 수 있습니다. (`true`가 1개 이상이고, `false`가 1개 이상입니다.)
* 위 성질을 이용해서 `false`인 부분을 이진검색으로 찾을 수 있습니다.
* 따라서 시간복잡도는 *O(logN)* 으로 위 3개의 solution보다 시간복잡도가 짧습니다.

> 2018/06/19 Written by Jon Jee

----------