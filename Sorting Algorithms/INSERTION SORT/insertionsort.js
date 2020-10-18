const insertionSort = (arr, reverse = false) => {

  for (let i = 0 ; i < arr.length ; i++) {
    
    currentElement = arr[i]

    while( (i != 0) && arr[i - 1] > currentElement){
      arr[i] = arr[i - 1]
      i -= 1
    }

    arr[i] = currentElement


  }

  reverse ? arr.reverse() : arr
  
  return arr


}

arr = Array.from( {length:100}, () => (Math.floor(Math.random() * 100)) )

let start = new Date().getTime()
console.log(insertionSort(arr, false))
let end = new Date().getTime()

console.log(`Time Elapsed ${end - start}ms`)
// console.log(Math.floor(Math.random() * 40))

// Runs in 19ms