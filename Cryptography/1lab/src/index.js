const fs = require('fs')

let fileContent = fs.readFileSync("data4", "utf8");
v = []
for (letter in fileContent) {
    v.push(letter)
}
console.log(v);
// console.log(fileContent);
