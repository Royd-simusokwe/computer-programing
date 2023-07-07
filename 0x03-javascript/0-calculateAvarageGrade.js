const grades = [85, 90, 78, 92, 88];
var sum = 0;

function calculateAvarageGrade(grades) {
    for (let i = 0; i < grades.length; i++) {
        sum += grades[i];
    }

    return sum / grades.length
}
console.log(calculateAvarageGrade(grades));