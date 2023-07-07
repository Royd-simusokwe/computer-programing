function isPalindrome(str) {
    var rem = /[\W_]/g;
    var lowCase = str.toLowerCase().replace(rem, '');
    var rev = lowCase.split('').reverse().join('');
    if (rev == lowCase) {
        console.log("true")
    } else {
        console.log("false")
    }
    return;
}
isPalindrome("lol")