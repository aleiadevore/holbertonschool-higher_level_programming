#!/usr/bin/node
const list = require('./100-data').list;
function multindx(item, index) {
    return index * item;
}
let newlist = list.map(multindx);
console.log(list);
console.log(newlist);
