let name = 'bill';
let greetings = `hello ${name}`;
console.log(greetings);

let hello = `hello ${name}\n`.length;
// console.log(hello);
let a = String.raw`bill\nhello`.length;

console.log(a);
let b = `hello \n demo`;
let bLen = String.raw(b);
console.log(bLen);