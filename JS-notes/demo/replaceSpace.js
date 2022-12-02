let  a = "you are a pig!";
// let b = "";

function replaceSpace(arr){
  for (let i = 0, len = arr.length; i < len - 1; i++) {
    if (arr[i] === " ") {
      arr[i] = arr[i + 1];
      i--;
    }
    return arr;
  }y
  // return a;
}
// let b = a.replaceSpace();
let b = replaceSpace(a);
console.log(b);

