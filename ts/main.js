'use strict';
function a1(b) {
	return b.c + b.d;
}
function a2(b) {
	return b.c + b.d;
}
var test = { c: 0, d: 9, e: 10 };
console.log(a1(test));
console.log(a2(test));
//console.log(a1({c: 0, d: 9, e: 10}));
var x = {
	a: 9,
	b: 10,
};
