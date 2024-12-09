function a1(b: { c: number; d: number }): number {
  return b.c + b.d;
}

function a2(b: Thing): number {
  return b.c + b.d;
}

interface Thing {
  c: number;
  d: number;
}
let test = { c: 0, d: 9, e: 10 };
console.log(a1(test));
console.log(a2(test));
//console.log(a1({c: 0, d: 9, e: 10}));

let x: {
  a: number;
  b: number;
} = {
  a: 9,
  b: 10,
};
