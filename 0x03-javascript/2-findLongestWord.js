function findLongestWord(str) {
    str = str.split(" ")
    return str.sort((a, b) => b.length - a.length)[0]
}

console.log(findLongestWord("you can get cheaper things on ebay" + "other wise alibaba has the best prices"))