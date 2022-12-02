// let  a = 8;
// console.log(Math.pow(a,1/3))
// let b = Math.log(a)/Math.LN2
// console.log(b)
// console.log(Number.MAX_VALUE)

// let a = 0/0;
// console.log(a===NaN) //false
// console.log(Number.isNaN(a)) //true

// let date = Date.now();
// let now = new Date();
// let ms = now.getTime();
// let iso = now.toISOString();

// console.log(ms)
// console.log(iso)
// console.log(date)


let  a = `you are a pig!`;

console.log(a.length)
// console.log(a.split(" "));
console.log(a.slice(1,3))
// console.log(a)
console.log(a.indexOf('a'));
console.log(a.lastIndexOf('a')); //8
console.log(a.includes('are')); //true
// console.log(a.toUpperCase());
// console.log(a.toLowerCase());
a.toUpperCase();
let b = a.replace(" ","");
console.log(b);
