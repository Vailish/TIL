// 1.
const colors = ['red', 'blue', 'green']

// const printClr = function (color) {
//   console.log(color)
// }

// colors.forEach(printClr)

// // 2. 파이썬의 map과 동작원리 동일
// colors.forEach(function (color) {
//   console.log(color)
// })

// 3. js에서 사랑하는 구조.. 많이 쓰임
colors.forEach((color) => {
  console.log(color)
})

//  반환이 없으므로 바로 출력