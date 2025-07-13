/*

  0 1 2 3 4 5
0 8 0 8 7 9 7
1 9 7 1 2 3 5
2 9 4 2 3 4 5
3 2 2 4 5 2 1
4 1 3 5 2 5 7

*/

// const a = [
//   [8, 0, 0, 7, 9, 7],
//   [9, 7, 1, 2, 3, 5],
//   [9, 4, 2, 3, 4, 5],
//   [2, 2, 4, 5, 2, 1],
//   [1, 3, 5, 2, 5, 7],
// ];

// console.log(a[2][3]);

const a = [9];

console.log(a[1]);

// function f(x) {
//   if (x <= 0) {
//     return 0;
//   }

//   return x + 1;
// }

const f = (x) => {
  if (x <= 0) {
    return 0;
  }

  return x + 1;
};

console.log(f(-123409821));
console.log(f(20));
console.log("alo");
