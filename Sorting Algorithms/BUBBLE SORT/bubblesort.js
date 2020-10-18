// Bubble Sort Algorithm

const bubbleSort = (arr, reverse = false) => {
    let totalSwaps = 0
    for (let i=0 ; i < arr.length ; i++){
      //To compare between adjacent elements
      for (let j=0 ; j < arr.length - i - 1 ; j++){
  
        if (arr[j] > arr[j+1]){
          temp = arr[j+1]
          arr[j+1] = arr[j]
          arr[j] = temp
  
          totalSwaps ++
        }
      }
    }
  
    return [arr, totalSwaps]
  }
  
  
  arr = Array.from( {length: 40}, () => (Math.floor(Math.random()*100)))
  
  start = new Date().getTime()
  const [sorted_arr, totalSwaps] = bubbleSort(arr)
  console.log(sorted_arr)
  console.log(`Total Swaps - ${totalSwaps}`)
  end = new Date().getTime()
  
  console.log(`Time Elapsed - ${end - start} ms`)